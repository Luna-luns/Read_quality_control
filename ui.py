def ask_file() -> str:
    return input().strip()


def print_reads_number(number: int) -> None:
    print(f'Reads in the file = {number}:')


def print_reads_length(length_dict: dict) -> None:
    for key, value in length_dict.items():
        print(f'      with length {key} = {value}')


def print_average_reads_length(average: int) -> None:
    print(f'Reads sequence average length = {average}')
