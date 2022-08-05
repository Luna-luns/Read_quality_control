import ui
from file_content import FileContent


path = ui.ask_file()
with open(path, 'r') as file:
    data_list = FileContent([elem.strip() for elem in file.readlines()])

ui.print_reads_number(data_list.reads_number)
ui.print_average_reads_length(data_list.count_average_reads_length())
repeats_dict = data_list.make_repeats_dict()
if data_list.check_repeats(repeats_dict):
    ui.print_repeats(data_list.count_repeats(repeats_dict))
ui.print_gc_average_content(data_list.mean_value())
