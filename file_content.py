class FileContent:
    READ = 4  # 1 read = 4 lines

    def __init__(self, data: list):
        self.data = data
        self.sequence = self.data[1::self.READ]
        self.reads_length = [len(elem) for elem in self.sequence]
        self.reads_number = len(self.data) // self.READ

    def count_average_reads_length(self) -> int:
        return round(sum(self.reads_length) / len(self.reads_length))

    def count_nucleotides(self, n: str) -> list:
        return [elem.count(f'{n}') for elem in self.sequence]

    def calculate_read_gc(self) -> list:
        c = self.count_nucleotides('C')
        g = self.count_nucleotides('G')
        cg = [c[i] + g[i] for i in range(len(c))]

        return cg

    def calculate_average_read_gc(self) -> list:
        cg = self.calculate_read_gc()
        return [cg[i] / self.reads_length[i] for i in range(len(cg))]

    def mean_value(self) -> float:
        average = self.calculate_average_read_gc()
        return round(sum(average) / len(average) * 100, 2)

    def check_repeats(self, _dict) -> bool:
        return bool(self.reads_number > len(_dict))

    def make_repeats_dict(self) -> dict:
        repeats_dict = {}
        for elem in self.sequence:
            repeats_dict[elem] = repeats_dict.get(elem, 0) + 1

        return repeats_dict

    def count_repeats(self, _dict: dict) -> int:
        return self.reads_number - len(_dict)
