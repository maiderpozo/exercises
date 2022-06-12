import sys
import csv


with open(sys.argv[1], encoding="utf-8") as tsv_file:
csv_reader = csv.reader(tsv_file, delimiter="\t")

counter = Counter()

for entry in csv_reader:

    title = entry[1]
    counter [title] += len(title)