class FileContent:
    READ = 4  # 1 read = 4 lines

    def __init__(self, data: list):
        self.data = data
        self.reads_length = None

    def count_length(self) -> int:
        return len(self.data)

    def count_reads(self) -> int:
        return self.count_length() // self.READ

    def count_reads_length(self) -> dict:
        self.reads_length = [len(elem) for elem in self.data[1::self.READ]]
        len_dict = {}

        for elem in self.reads_length:
            len_dict[elem] = len_dict.get(elem, 0) + 1

        return len_dict

    def count_average_reads_length(self) -> int:
        return round(sum(self.reads_length) / len(self.reads_length))
