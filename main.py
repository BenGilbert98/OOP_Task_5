from list import List # Importing list from list
from count import Count # Importing count from count

sequence = List() # Creating an object of class List
letter_count = Count() # Creating an object of class Count

sequence.random_dna_sequence()

letter_count.count(sequence.dataset)