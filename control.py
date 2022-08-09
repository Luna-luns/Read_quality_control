import ui
from file_content import FileContent


path = ui.ask_file()
with open(path, 'r') as file:
    reads_dict = {}
    for line in file.readlines()[1::4]:
        reads_dict[line.strip()] = reads_dict.get(line.strip(), 0) + 1

data_list = FileContent(reads_dict)

ui.print_reads_number(data_list.reads_number)
ui.print_average_reads_length(data_list.count_average_reads_length())
ui.print_repeats(data_list.count_repeats())
ui.print_reads_n_number(data_list.count_n_reads())
ui.print_gc_average_content(data_list.mean_value())
ui.print_average_read_n(data_list.calculate_read_n())
