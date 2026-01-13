import tkinter as tk
from tkinter import colorchooser
from tkinter import filedialog
from PIL import Image, ImageDraw

GRID_SIZE = 16
GRID_COUNT = 32

cells = {}
draw_color = 'black'
eraser_color = 'white'
fill_color = 'red'

root = tk.Tk()
root.title('Pixel Art Studio')
root.resizable(False, False)

canvas = tk.Canvas(
    root, 
    width = GRID_SIZE * GRID_COUNT,
    height = GRID_SIZE * GRID_COUNT,
    bg = 'white'
)
canvas.pack()

def draw_grid() -> None:
    for x in range(GRID_COUNT):
        for y in range(GRID_COUNT):
            x_1 = x * GRID_SIZE
            y_1 = y * GRID_SIZE
            x_2 = x_1 + GRID_SIZE
            y_2 = y_1 + GRID_SIZE

            canvas.create_rectangle(
                x_1, y_1, x_2, y_2,
                outline = 'lightgray',
                fill = 'white',
                tags = f'cell_{x}_{y}'
            )

            cells[(x, y)] = 'white'

def paint(event: 'tk.Event', color: str) -> None:
    x = event.x // GRID_SIZE
    y = event.y // GRID_SIZE

    if 0 <= x < GRID_COUNT and 0 <= y < GRID_COUNT:
        canvas.itemconfig(f'cell_{x}_{y}', fill = color)
        cells[(x, y)] = color 

def draw(event: 'tk.Event') -> None:
    paint(event, draw_color)

def erase(event: 'tk.Event') -> None:
    paint(event, eraser_color)

def fill_background() -> None:
    global eraser_color
    for (x, y), color in cells.items():
        if color == eraser_color:
            canvas.itemconfig(f'cell_{x}_{y}', fill = fill_color)
            cells[(x, y)] = fill_color
    eraser_color = fill_color

def clear_canvas() -> None:
    global fill_color, eraser_color
    for (x, y) in cells:
        canvas.itemconfig(f'cell_{x}_{y}', fill = 'white')
        cells[(x, y)] = 'white'
    eraser_color = 'white'

def choose_draw_color() -> None:
    global draw_color
    color = colorchooser.askcolor(title = 'Choose a pencil color')[1]
    if color:
        draw_color = color
        draw_color_button.configure(foreground = color)

def choose_fill_color() -> None:
    global fill_color
    color = colorchooser.askcolor(title = 'Choose the background fill color')[1]
    if color:
        fill_color = color
        fill_color_button.configure(foreground = color)

def save_to_file() -> None:
    file_path = filedialog.asksaveasfilename(
        defaultextension = '.png',
        filetypes = [('PNG files', '*.png')],
        title = 'Save as'
    )
    if not file_path:
        return 

    image = Image.new('RGB', (GRID_COUNT, GRID_COUNT), 'white')
    draw_image = ImageDraw.Draw(image)

    for (x, y), color in cells.items():
        draw_image.point((x, y), fill = color)

    image = image.resize((GRID_COUNT * GRID_SIZE, GRID_COUNT * GRID_SIZE), resample = Image.NEAREST)
    image.save(file_path)
    print(f'Save: {file_path}')

canvas.bind('<Button-1>', draw)
canvas.bind('<B1-Motion>', draw)

canvas.bind('<Button-2>', erase)
canvas.bind('<B2-Motion>', erase)

draw_grid()

toolbar = tk.Frame(root)
toolbar.pack(pady = 5)

draw_color_button = tk.Button(
    toolbar,
    text = 'Pencil Color',
    command = choose_draw_color,
    foreground = draw_color
)
draw_color_button.pack(side = tk.LEFT, padx = 5)

fill_color_button = tk.Button(
    toolbar,
    text = 'Background Color',
    command = choose_fill_color,
    foreground = fill_color
)
fill_color_button.pack(side = tk.LEFT, padx = 5)

fill_button = tk.Button(toolbar, text = 'Fill', command = fill_background)
fill_button.pack(side = tk.LEFT, padx = 5)

clear_button = tk.Button(toolbar, text = 'Clear', command = clear_canvas)
clear_button.pack(side = tk.LEFT, padx = 5)

save_button = tk.Button(toolbar, text = 'Save', command = save_to_file)
save_button.pack(side = tk.LEFT, padx = 5)

root.update_idletasks()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = root.winfo_width()
window_height = root.winfo_height()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f'{window_width}x{window_height}+{x}+{y}')

root.mainloop()