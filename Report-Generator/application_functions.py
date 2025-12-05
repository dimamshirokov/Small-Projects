def request_columns_for_data_frame() -> list[str]:
    print()
    respond = input('- Enter the names of the columns that you want to take from the dataframe separated by a space >>> ').strip()
    print()
    list_respond = respond.split()
    return list_respond

def request_columns_for_linear_graph() -> tuple[str, list[str]]:
    print()
    respond_x = input('- Enter the column name that you want to take by x axis >>> ').strip()
    print()
    respond_y = input('- Enter the names of the columns that will be on the y axis separated by a space >>> ')
    print()
    list_respond_y = respond_y.split()
    return (respond_x, list_respond_y)

def request_columns_for_bar_chart() -> tuple[str, str]:
    print()
    respond_x = input('- Enter the name of the column you want to use as a category >>> ').strip()
    print()
    respond_y = input('- Enter the name of the column you want to take as values >>> ').strip()
    print()
    return (respond_x, respond_y)

def request_columns_for_pie_chart() -> tuple[str, None | str]:
    CASE_SELECT_LABELS = 1
    CASE_TAKE_INDEXES = 2
    print()
    respond_y = input('- Enter the name of the column to be used for visualization >>> ').strip()
    print()
    while True:
        print('\n- 1. Select one of the dataframe columns as labels', '- 2. Take dataframe indexes as labels', sep = '\n\n', end = '\n\n')
        selected_item = int(input('- Select an item >>> '))
        print()
        if selected_item < CASE_SELECT_LABELS or selected_item > CASE_TAKE_INDEXES:
            continue
        elif selected_item == CASE_SELECT_LABELS:
            name_of_labels_column = input('- Enter the name of the dataframe column that you want to use as labels >>> ').strip()
            print()
            return (respond_y, name_of_labels_column)
        elif selected_item == CASE_TAKE_INDEXES:
            return (respond_y, None)
        
def clear_console() -> None:
    print('\033c', end = '')