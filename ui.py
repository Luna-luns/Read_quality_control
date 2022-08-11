from file_content import FileContent


def ask_file() -> str:
    return input().strip()


def print_reads_number(number: int) -> None:
    print(f'Reads in the file = {number}')


def print_average_reads_length(average: int) -> None:
    print(f'Reads sequence average length = {average}')


def print_repeats(num: int) -> None:
    print(f'\nRepeats = {num}')


def print_gc_average_content(percentage: float) -> None:
    print(f'\nGC content average = {percentage}%')


def print_average_read_n(percentage: float) -> None:
    print(f'Ns per read sequence = {percentage}%')


def print_reads_n_number(num: int) -> None:
    print(f'Reads with Ns = {num}')


def print_all(data_list: FileContent) -> None:
    print_reads_number(data_list.reads_number)
    print_average_reads_length(data_list.count_average_reads_length())
    print_repeats(data_list.count_repeats())
    print_reads_n_number(data_list.count_n_reads())
    print_gc_average_content(data_list.mean_value())
    print_average_read_n(data_list.calculate_read_n())
