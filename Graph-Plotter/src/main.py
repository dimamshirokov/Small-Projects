import tkinter as tk
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from math import *

def is_number(string: str) -> bool:
    try:
        float(eval(string))
        return True
    except:
        return False
    
def clear_third_frame() -> None:
    for widget in third_frame.winfo_children():
        widget.destroy()

def add_canvas_and_toolbar_to_the_third_frame() -> None:
    canvas = FigureCanvasTkAgg(master = third_frame)
    canvas.get_tk_widget().pack(fill = tk.BOTH, padx = PADX, pady = PADY, expand = True)

    toolbar = NavigationToolbar2Tk(canvas, third_frame)
    canvas.get_tk_widget().pack(fill = tk.BOTH, padx = PADX, pady = PADY, expand = True)

def display_state_in_log_label(state: str, color: str) -> None:
    current = tk.StringVar()
    log_label['textvariable'] = current
    current.set(state)
    log_label['foreground'] = color

def build_function() -> None:
    try:
        global function, left_border, right_border
        function = eval('lambda x: ' + enter_function_widget.get())
        left_border = enter_left_border_widget.get()
        right_border = enter_right_border_widget.get()
        if function != None and is_number(left_border) and is_number(right_border) and eval(left_border) <= eval(right_border):
            clear_third_frame()

            plt.close('all')

            left_border_number = eval(left_border)
            right_border_number = eval(right_border)

            x = np.linspace(left_border_number, right_border_number, ceil(np.abs(right_border_number - left_border_number) * 50))
            y = list(map(function, x))

            figure = plt.figure(figsize = (5, 5))

            axes = figure.add_axes([0, 0, 1, 1])
            axes.plot(x, y, color = '#023EFF')

            axes.spines['left'].set_position('center')
            axes.spines['bottom'].set_position('center')
            axes.spines['top'].set_visible(False)
            axes.spines['right'].set_visible(False)

            axes.grid(alpha = 0.3)
            plt.legend([f'$f(x) = {enter_function_widget.get()}$'], facecolor = '#E6E6FA', edgecolor = '#000000')

            canvas = FigureCanvasTkAgg(figure, master = third_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill = tk.BOTH, padx = PADX, pady = PADY, expand = True)

            toolbar = NavigationToolbar2Tk(canvas, third_frame)
            toolbar.update()
            canvas.get_tk_widget().pack(fill = tk.BOTH, padx = PADX, pady = PADY, expand = True)

            display_state_in_log_label('The function was built successfully!', 'green')
        else:
            display_state_in_log_label('Couldn\'t build a function', 'red')
    except NameError as error:
        clear_third_frame()

        plt.close('all')
        
        add_canvas_and_toolbar_to_the_third_frame()

        display_state_in_log_label(error, 'red')
    except SyntaxError as error:
        clear_third_frame()

        plt.close('all')

        add_canvas_and_toolbar_to_the_third_frame()

        display_state_in_log_label(error, 'red')
    except TypeError as error:
        clear_third_frame()

        plt.close('all')

        add_canvas_and_toolbar_to_the_third_frame()

        display_state_in_log_label(error, 'red')
    except ValueError as error:
        clear_third_frame()

        plt.close('all')

        add_canvas_and_toolbar_to_the_third_frame()

        display_state_in_log_label(error, 'red')
    except IndexError as error:
        clear_third_frame()

        plt.close('all')

        add_canvas_and_toolbar_to_the_third_frame()

        display_state_in_log_label(error, 'red')

if __name__ == '__main__':
    FONT = 'ARIAL BLACK'
    FONTSIZE = 18
    LOG_LABEL_FONTSIZE = 9
    WINDOW_MIN_WIDTH = 480
    WINDOW_MIN_HEIGHT = 760
    PADX = 3
    PADY = 3
    

    function = None
    left_border, right_border = None, None

    matplotlib.use('Agg')

    root = tk.Tk()
    root.title('Graph-Plotter')
    root.minsize(WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)
    root.lift()

    first_frame = tk.Frame(root, bg = 'black')
    first_frame.pack(fill = tk.BOTH, padx = PADX, pady = PADY, expand = True)

    function_label = tk.Label(first_frame, text = 'f(x) = ', width = 7, height = 1, font = (FONT, FONTSIZE))
    function_label.pack(side = tk.LEFT, padx = PADX, pady = PADY, fill = tk.BOTH)

    enter_function_widget = tk.Entry(first_frame, font = (FONT, FONTSIZE))
    enter_function_widget.pack(side = tk.LEFT, padx = PADX, pady = PADY, fill = tk.BOTH, expand = True)

    second_frame = tk.Frame(root, bg = 'black')
    second_frame.pack(fill = tk.BOTH, padx = PADX, pady = PADY, expand = True)

    enter_left_border_widget = tk.Entry(second_frame, width = 5, font = (FONT, FONTSIZE))
    enter_left_border_widget.pack(side = tk.LEFT, padx = PADX, pady = PADY, fill = tk.BOTH, expand = True)

    borders_label = tk.Label(second_frame, text = ' <= x <= ', width = 9, height = 1, font = (FONT, FONTSIZE))
    borders_label.pack(side = tk.LEFT, padx = PADX, pady = PADY, fill = tk.BOTH)

    enter_right_border_widget = tk.Entry(second_frame, width = 5, font = (FONT, FONTSIZE))
    enter_right_border_widget.pack(side = tk.LEFT, padx = PADX, pady = PADY, fill = tk.BOTH, expand = True)

    third_frame = tk.Frame(root, bg = 'black')
    third_frame.pack(fill = tk.BOTH, padx = PADX, pady = PADY, expand = True)

    canvas = FigureCanvasTkAgg(master = third_frame)
    canvas.get_tk_widget().pack(fill = tk.BOTH, padx = PADX, pady = PADY, expand = True)

    toolbar = NavigationToolbar2Tk(canvas, third_frame)
    canvas.get_tk_widget().pack(fill = tk.BOTH, padx = PADX, pady = PADY, expand = True)

    fourth_frame = tk.Frame(root, bg = 'black')
    fourth_frame.pack(fill = tk.BOTH, padx = PADX, pady = PADY, expand = True)

    build_graph_button = tk.Button(fourth_frame, text = 'BUILD', command = build_function, font = (FONT, FONTSIZE))
    build_graph_button.pack(side = tk.LEFT, padx = PADX, pady = PADY, fill = tk.BOTH, expand = True)

    fifth_frame = tk.Frame(root)
    fifth_frame.pack(fill = tk.BOTH, padx = PADX, pady = PADY, expand = True)

    log_label = tk.Label(fifth_frame, font = (FONT, LOG_LABEL_FONTSIZE))
    log_label.pack(side = tk.LEFT, padx = PADX, pady = PADY, fill = tk.BOTH, expand = True)

    root.update_idletasks()

    screen_width = root.winfo_screenmmwidth()
    screen_height = root.winfo_screenmmheight()

    window_width = root.winfo_width()
    window_height = root.winfo_height()

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    root.geometry(f'{window_width}x{window_height}+{x}+{y}')

    root.mainloop()