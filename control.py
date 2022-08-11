import ui
import gzip
from file_content import FileContent


def get_reads_dict():
    path = ui.ask_file().strip()
    with gzip.open(path, 'rt') as file:
        reads_dict = {}
        for line in file.readlines()[1::4]:
            reads_dict[line.strip()] = reads_dict.get(line.strip(), 0) + 1

    return reads_dict


data_1 = FileContent(get_reads_dict())
data_2 = FileContent(get_reads_dict())
data_3 = FileContent(get_reads_dict())

# _list = [data1, data2, data3]
# data_list = min(_list, key=lambda d: d.count_n_reads())
read_n_dict = {data_1: data_1.count_n_reads(), data_2: data_2.count_n_reads(), data_3: data_3.count_n_reads()}
read_n_dict = {key: value for key, value in sorted(read_n_dict.items(), key=lambda item: item[1])}
ui.print_all(next(iter(read_n_dict)))
