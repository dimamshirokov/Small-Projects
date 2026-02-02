import cv2 as cv
import numpy as np
from typing import Any, List, Tuple

import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import models
from tensorflow.keras import layers

EMNIST_LABELS = [
 '0','1','2','3','4','5','6','7','8','9',
 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
]

PATH_TO_YOUR_IMAGE = ''

def emnist_model() -> None:
    model = models.Sequential([
        layers.Input(shape = (28, 28, 1)),
        layers.Conv2D(32, (3, 3), activation = 'relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation = 'relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation = 'relu'),
        layers.Dense(62, activation = 'softmax')
    ])

    model.compile(
        optimizer = 'adam',
        loss = 'sparse_categorical_crossentropy',
        metrics = ['accuracy']
    )

    return model

def preprocess(sample: Any) -> Tuple:
    image = tf.cast(sample['image'], tf.float32) / 255.0
    label = sample['label']
    return image, label

def emnist_train(model: Any) -> None:
    dataset_train = tfds.load('emnist/byclass', split = 'train', as_supervised = False)
    dataset_test = tfds.load('emnist/letters', split = 'test', as_supervised = False)

    dataset_train = (
        dataset_train
        .map(preprocess, num_parallel_calls = tf.data.AUTOTUNE)
        .shuffle(10_000)
        .batch(128)
        .prefetch(tf.data.AUTOTUNE)
    )

    dataset_test = (
        dataset_test
        .map(preprocess, num_parallel_calls = tf.data.AUTOTUNE)
        .batch(128)
        .prefetch(tf.data.AUTOTUNE)
    )

    model.fit(
        dataset_train,
        epochs = 10,
        validation_data = dataset_test
    )
    
def emnist_predict_image(model: Any, image: List[Any]) -> str:
    image = image.astype('float32') / 255.0

    image = np.rot90(image, 3)
    image = np.fliplr(image)

    image = image.reshape((1, 28, 28, 1))

    predict = model.predict(image, verbose = 0)
    result = np.argmax(predict, axis = 1)

    return EMNIST_LABELS[result[0]]

def letters_extract(image_file: str, out_size = 28) -> List[Any]:
    image = cv.imread(image_file)

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    _, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    num_labels, labels, stats, centroids = cv.connectedComponentsWithStats(
        thresh,
        connectivity = 8
    )

    letters = []

    for index in range(1, num_labels):
        (x, y, width, height, area) = stats[index]

        if area < 80:
            continue

        letter_crop = thresh[y:y + height, x:x + width]
        letter_crop = cv.medianBlur(letter_crop, 3)

        size = max(width, height)
        pad = int(size * 0.3)

        letter_square = np.zeros((size + 2 * pad, size + 2 * pad), dtype = np.uint8)

        x_offset = pad + (size - width) // 2
        y_offset = pad + (size - height) // 2
        letter_square[y_offset:y_offset + height, x_offset:x_offset + width] = letter_crop

        letter_square = cv.resize(
            letter_square,
            (out_size, out_size),
            interpolation = cv.INTER_AREA
        )

        letters.append((x, width, letter_square))
    
    letters.sort(key = lambda x: x[0])

    return letters

def image_to_string(model: Any, image_file: str) -> str:
    letters = letters_extract(image_file)
    text = ''

    for index in range(len(letters)):
        x, width, image = letters[index]
        text += emnist_predict_image(model, image)

        if index < len(letters) - 1:
            gap = letters[index + 1][0] - x - width
            if gap > width * 0.4:
                text += ' '

    return text

if __name__ == '__main__':
    model = emnist_model()
    emnist_train(model)
    model.save('emnist_byclass.keras')

    model = models.load_model('emnist_byclass.keras')
    text = image_to_string(model, PATH_TO_YOUR_IMAGE)
    print(text)