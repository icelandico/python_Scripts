import csv
import os

csvDir = os.listdir(r"D:\GIS\ROBOCZE\Ulice_wojewodztwa\dane\test")
pathBase = r"D:\GIS\ROBOCZE\Ulice_wojewodztwa\dane"
directory = r"D:\GIS\ROBOCZE\Ulice_wojewodztwa\dane\test"

def writeCsv(name):
    with open(pathBase + '/test/' + name + '.csv') as csvInput, open(pathBase + '/result' + r'\edited_' + name + '.csv', 'w', newline='') as csvOutput:
        reader = csv.reader(csvInput, delimiter=';')
        writer = csv.writer(csvOutput, delimiter=';')
        streets = []
        streetsCount = {}

        for row in reader:
            column = list(row[i] for i in [7, 8])
            streets.append((f'{column[1]} {column[0]}').strip())

        for street in streets:
            if street in streetsCount:
                streetsCount[street] += 1
            else:
                streetsCount[street] = 1

        for key in streetsCount:
            writer.writerow([key, streetsCount[key]])

for file in csvDir:
    filename = os.path.splitext(file)[0]
    writeCsv(filename)
