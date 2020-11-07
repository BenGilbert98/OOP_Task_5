from list import List


class Count(List):
    def __init__(self):
        super().__init__()

    def count(self, dna_list):
        a_count = 0
        c_count = 0
        g_count = 0
        t_count = 0
        for i in dna_list:
            if i in "A":
                a_count += 1
            if i in "C":
                c_count += 1
            if i in "G":
                g_count += 1
            if i in "T":
                t_count += 1
        print(f"Number of A values --> {a_count}")
        print(f"Number of C values --> {c_count}")
        print(f"Number of G values --> {g_count}")
        print(f"Number of T values --> {t_count}")