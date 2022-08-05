def ask_file() -> str:
    return input().strip()


def print_reads_number(number: int) -> None:
    print(f'Reads in the file = {number}:')


def print_average_reads_length(average: int) -> None:
    print(f'Reads sequence average length = {average}')


def print_gc_average_content(percentage: float) -> None:
    print(f'\nGC content average = {percentage}%')
