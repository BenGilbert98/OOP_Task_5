import random # importing the random module


class List:

    def __init__(self):
        self.dataset = [] # Blank dataset list

    def random_dna_sequence(self):
        # for every value in the range 1 - 1000 a number between 1 and 4 is generated
        for i in range(1, 1000):
            dna_value = random.randrange(1, 5)
            # the value produced from random range corresponds to a letter
            if dna_value == 1:
                self.dataset.append("A")
            if dna_value == 2:
                self.dataset.append("C")
            if dna_value == 3:
                self.dataset.append("G")
            if dna_value == 4:
                self.dataset.append("T")
        print(self.dataset)