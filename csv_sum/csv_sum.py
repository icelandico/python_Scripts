import csv

inputFile = r"D:\GIS\ROBOCZE\Ulice_wojewodztwa\dane\test\pomorskie.csv"
directory = r"D:\GIS\ROBOCZE\Ulice_wojewodztwa\dane\test"
output = directory + r'\edited.csv'

with open(inputFile) as csvInput, open(output, 'w', newline='') as csvOutput:
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
