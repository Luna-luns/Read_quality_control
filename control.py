import ui
from file_content import FileContent


path = ui.ask_file()
with open(path, 'r') as file:
    data_list = FileContent([elem.strip() for elem in file.readlines()])

reads_number = data_list.count_reads()
ui.print_reads_number(reads_number)

reads = data_list.count_reads_length()
ui.print_reads_length(reads)
average_reads_length = data_list.count_average_reads_length()
ui.print_average_reads_length(average_reads_length)
