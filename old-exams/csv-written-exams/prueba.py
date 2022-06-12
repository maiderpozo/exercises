import csv
import sys


result = {}

with open('exam-schedule.csv') as file:
    data = csv.DictReader(file)

    for row in data:
        parts=row.split