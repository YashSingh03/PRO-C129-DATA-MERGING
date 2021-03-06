import csv
import pandas as pd

file1 = 'c127.csv'
file2 = 'c128.csv'

d1 = []
d2 = []
with open(file1, 'r', encoding='utf8') as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        d1.append(i)

with open(file2, 'r', encoding='utf8') as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        d2.append(i)

h1 = d1[0]
h2 = d2[0]

p_d1 = d1[1:]
p_d2 = d2[1:]

h = h1+h2

p_d = []

for i in p_d1:
    p_d.append(i)
for j in p_d2:
    p_d.append(j)
with open("Data_merged.csv", 'w', encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)
    csvwriter.writerows(p_d)

df = pd.read_csv('Data_merged.csv')
df.tail(8)
print('Your both files merged sucessfully')

with open("Data_merged.csv") as input, open("Data_merged01.csv", "w", newline='') as output:
    csvwriter = csv.writer(output)
    csvreader = csv.reader(input)
    for row in csvreader:
        if any(field.strip() for field in row):
            csvwriter.writerow(row)
