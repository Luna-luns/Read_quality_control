class FileContent:
    def __init__(self, data: dict):
        self.data = data
        self.reads_length = [len(key) for key in self.data.keys()]
        self.reads_number = sum(self.data.values())

    def count_average_reads_length(self) -> int:
        return round(sum(self.reads_length) / len(self.reads_length))

    def count_nucleotides(self, n: str) -> list:
        return [key.count(f'{n}') * value for key, value in self.data.items()]

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
        return round(sum(average) / self.reads_number * 100, 2)

    def count_repeats(self) -> int:
        return self.reads_number - len(self.data)

    def calculate_read_n(self):
        n = self.count_nucleotides('N')
        average_read_n = [n[i] / self.reads_length[i] for i in range(len(n))]
        return round(sum(average_read_n) / self.reads_number * 100, 2)

    def count_n_reads(self) -> int:
        count = 0
        for key in self.data.keys():
            if 'N' in key:
                count += 1
        return count
