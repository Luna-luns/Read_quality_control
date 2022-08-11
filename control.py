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


# data_1 = FileContent(get_reads_dict())
# data_2 = FileContent(get_reads_dict())
# data_3 = FileContent(get_reads_dict())
#
# read_n_dict = {data_1: data_1.calculate_read_n(), data_2: data_2.calculate_read_n(), data_3: data_2.calculate_read_n()}
# read_n_dict = {key: value for key, value in sorted(read_n_dict.items(), key=lambda item: item[1])}
# ui.print_all(next(iter(read_n_dict)))
#
# if next(iter(read_n_dict)) == 'data_1':
#     ui.print_all(data_1)
# elif next(iter(read_n_dict)) == 'data_2':
#     ui.print_all(data_2)
# elif next(iter(read_n_dict)) == 'data_3':
#     ui.print_all(data_3)
# print(data_2.data)
# print(ui.print_all(data_2))
print(get_reads_dict())
