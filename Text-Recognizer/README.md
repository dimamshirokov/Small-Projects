<h1 align='center'> Text Recognizer </h1>

___

## ✏️ Description

It is a convolutional neural network (CNN) that can recognize handwritten text and numbers in a photo. 
The project is written in Python.

> [!IMPORTANT]
> The background of the photo should be black, and the text itself should be white and handwritten!

## 🖥 Requirements

- opencv-python
- numpy
- tensorflow-datasets
- tensorflow

## 🛵 Run the program

While in the folder /Small-Projects/Text-Recognizer, run the command below.

```console
pip install -r requirements.txt
```

![](https://drive.google.com/uc?id=1TtD_gAXTMfQlMfFvHAaTM3vERTZ-tr6R)

In the main.py in the PATH_TO_YOUR_IMAGE variable, 
write the path to your image from which you want to get text and numbers.

Meanwhile, in the folder /Small-Projects/Text-Recognizer/src, run the command below.

```console
python3 main.py
```

The result should have been displayed in the console.

![](https://drive.google.com/uc?id=1z9lv4S7PR57OAaBYyF75d3rM1I2p1tAg)

Then, after the model has been trained and saved, you can comment out the lines in the main.py as shown in the screenshot and already use the ready-made model!

## 🤖 Examples

![](https://drive.google.com/uc?id=1YYCbYxEylnF4d2sjbtferkNiSND-L5Fa)

> [!NOTE]
> The result of the neural network was: 1 2 3 O 5 7
> The neural network printed the letter O instead of zero. But it's not a big deal.

![](https://drive.google.com/uc?id=1G84XfJ_0QIr40-2BjZD-xG7h-VD5CReZ)

> [!NOTE]
> The result of the neural network: O I M A
> In principle, it's good because the letters D and O are similar.

## :octocat: Author

**Dima M. Shirokov**
- [GitHub](https://github.com/dimamshirokov)