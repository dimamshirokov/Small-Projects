from fpdf import FPDF
from io import BytesIO
import matplotlib
import pandas 

class Report:
    def __init__(self, path: str, name_of_pdf: str) -> None:
        if '.csv' in path:
            self.path_to_file = path.strip()
        elif '.json' in path:
            self.path_to_file = path.strip()
        else:
            self.path_to_file = path.strip() + '.csv'
        self.pdf = FPDF()
        if '.pdf' in name_of_pdf:
            self.name_of_pdf = name_of_pdf.strip()
        else:
            self.name_of_pdf = name_of_pdf.strip() + '.pdf'
        self.data_frame = None

    def read_dataset(self, columns_of_data_frame: list[str]) -> None:
        if '.csv' in self.path_to_file:
            self.data_frame = pandas.read_csv(self.path_to_file)
        elif '.json' in self.path_to_file:
            self.data_frame = pandas.read_json(self.path_to_file)
        self.data_frame = self.data_frame[columns_of_data_frame]

    def save_pdf(self) -> None:
        self.pdf.output(self.name_of_pdf)

    def add_linear_graph_to_pdf(self, column_by_x: str, columns_by_y: str | list[str]) -> None:
        try:
            self.data_frame.plot(x = column_by_x, y = columns_by_y, grid = True)
            matplotlib.pyplot.title('Linear Graph')
            image_buffer = BytesIO()
            matplotlib.pyplot.savefig(image_buffer, dpi = 200)
            self.pdf.add_page()
            self.pdf.image(image_buffer, w = self.pdf.epw)
            image_buffer.close()
        except KeyError as error:
            print(f'- Error finding columns: {error}')
        except TypeError as error:
            print(f'- Error with the data type in the column: {error}')
        else:
            print('- The line graph has been added to the PDF file!')

    def add_bar_chart_to_pdf(self, column_by_x: str, column_by_y: str) -> None:
        try:
            self.data_frame.plot.bar(x = column_by_x, y = column_by_y)
            matplotlib.pyplot.title('Bar Chart')
            matplotlib.pyplot.xlabel('Categories')
            matplotlib.pyplot.ylabel('Values')
            image_buffer = BytesIO()
            matplotlib.pyplot.savefig(image_buffer, dpi = 200)
            self.pdf.add_page()
            self.pdf.image(image_buffer, w = self.pdf.epw)
            image_buffer.close()
        except KeyError as error:
            print(f'- Error finding columns: {error}')
        except TypeError as error:
            print(f'- Error with the data type in the column: {error}')
        else:
            print('- The bar chart has been added to the PDF file!')

    def add_pie_chart_to_pdf(self, column_by_y: str, name_of_labels_column: None | str) -> None:
        try:
            if name_of_labels_column:
                self.data_frame.plot.pie(y = column_by_y, labels = self.data_frame[name_of_labels_column], autopct = '%1.1f%%', shadow = True)
            else:
                self.data_frame.plot.pie(y = column_by_y, autopct = '%1.1f%%', shadow = True)
            image_buffer = BytesIO()
            matplotlib.pyplot.savefig(image_buffer, dpi = 200)
            self.pdf.add_page()
            self.pdf.image(image_buffer, w = self.pdf.epw)
            image_buffer.close()
        except KeyError as error:
            print(f'- Error finding columns: {error}')
        except TypeError as error:
            print(f'- Error with the data type in the column: {error}')
        else:
            print('- The pie chart has been added to the PDF file!')

    def add_data_frame_to_pdf(self) -> None:
        string_data_frame = self.data_frame.applymap(str)
        COLUMNS = [list(string_data_frame)]
        ROWS = string_data_frame.values.tolist()
        DATA = COLUMNS + ROWS
        self.pdf.add_page()
        self.pdf.set_font('Times', size = 10)
        with self.pdf.table(
            borders_layout = 'MINIMAL',
            cell_fill_color = 200,
            cell_fill_mode = 'ROWS',
            line_height = self.pdf.font_size * 2.5,
            text_align = 'CENTER',
            width = 160,
        ) as table:
            for data_row in DATA:
                row = table.row()
                for datum in data_row:
                    row.cell(datum)