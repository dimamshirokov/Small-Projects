if __name__ == '__main__':
    import application_functions
    from report import Report
    import warnings
    warnings.filterwarnings('ignore')

    CASE_BUILD_LINEAR_GRAPH = 1
    CASE_BUILD_BAR_CHART = 2
    CASE_BUILD_PIE_CHART = 3
    CASE_PRINT_TABLE_TO_CONSOLE = 4 
    CASE_SAVE_PDF = 5
    CASE_GENERATE_PDF_REPORT = 1
    CASE_EXIT = 2

    print('- Hello dear customer! This is a PDF report generation program!', end = '\n\n')
    while True:
        while True:
            try:
                print()
                path = input('- Enter the path to the JSON or CSV file you want to generate a PDF report for (if you do not specify the extension, it will be .csv) >>> ')
                print()
                name_of_pdf = input('- Enter the name of the PDF file that your report will be in >>> ')
                report = Report(path, name_of_pdf)
                list_respond = application_functions.request_columns_for_data_frame()
                application_functions.clear_console()
                report.read_dataset(list_respond)
                report.add_data_frame_to_pdf()
            except ValueError as error:
                print(f'- Error with the existence of such columns: {error}', end = '\n\n')
            except FileNotFoundError as error:
                print(f'- Error with finding a JSON or CSV file: {error}', end = '\n\n')
            except TypeError as error:
                print(f'- Incorrect column type: {error}', end = '\n\n')
            except KeyError as error:
                print(f'Error with the existence of columns in the dataframe: {error}', end = '\n\n')
            else:
                break
        while True:
            print('\n- 1. Build a linear graph.', '- 2. Build a bar chart.', '- 3. Build a pie chart.', '- 4. Output the table to the console.', '- 5. Complete and save the report as a PDF file.', sep = '\n\n', end = '\n\n')
            selected_item = int(input('- Select an item >>> '))
            if selected_item < CASE_BUILD_LINEAR_GRAPH or selected_item > CASE_SAVE_PDF:
                application_functions.clear_console()
                continue
            elif selected_item == CASE_BUILD_LINEAR_GRAPH:
                respond_x, list_respond_y = application_functions.request_columns_for_linear_graph()
                application_functions.clear_console()
                report.add_linear_graph_to_pdf(respond_x, list_respond_y)
            elif selected_item == CASE_BUILD_BAR_CHART:
                respond_x, respond_y = application_functions.request_columns_for_bar_chart()
                application_functions.clear_console()
                report.add_bar_chart_to_pdf(respond_x, respond_y)
            elif selected_item == CASE_BUILD_PIE_CHART:
                respond_y, name_of_labels_column = application_functions.request_columns_for_pie_chart()
                application_functions.clear_console()
                report.add_pie_chart_to_pdf(respond_y, name_of_labels_column)
            elif selected_item == CASE_PRINT_TABLE_TO_CONSOLE:
                print(end = '\n\n')
                application_functions.clear_console()
                print(report.data_frame, end = '\n\n')
                print('\n- The table has been displayed in the console!')
            elif selected_item == CASE_SAVE_PDF:
                report.save_pdf()
                application_functions.clear_console()
                print('\n- The report was saved as a PDF file!')
                break
        selected_item = None
        while True:
            print('\n- 1. Generate another PDF report.', '- 2. Exit.', sep = '\n\n', end = '\n\n')   
            selected_item = int(input('- Select an item >>> '))
            if selected_item < CASE_GENERATE_PDF_REPORT or selected_item > CASE_EXIT:
                application_functions.clear_console()
                continue
            else:
                application_functions.clear_console()
                break
        if selected_item == CASE_GENERATE_PDF_REPORT:
            continue
        elif selected_item == CASE_EXIT:
            break