import random


class List:

    def __init__(self):
        self.dataset = []

    def random_dna_sequence(self):
        for i in range(1, 1000):
            dna_value = random.randrange(1, 5)
            if dna_value == 1:
                self.dataset.append("A")
            if dna_value == 2:
                self.dataset.append("C")
            if dna_value == 3:
                self.dataset.append("G")
            if dna_value == 4:
                self.dataset.append("T")
        print(self.dataset)