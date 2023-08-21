import sys
import csv
import datadir

maxInt = sys.maxsize

while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

reader = csv.reader(open(r"" + datadir.ATK_DIR, 'r', encoding='utf-8'))
writer = csv.writer(open(r"" + datadir.FOX_DIR, 'w', encoding='utf-8'))

for row in reader:
    if (row[9] == 'Fox News'):
        writer.writerow(row)