import csv
voltage_values = [1,2,3,4,5,6,7,8,9,10]
current_values = [1,2,3,4,5,6,7,8,9,10]
with open('EV\sampleFile.csv', 'w', encoding='UTF8',newline="") as f:
    writer = csv.writer(f)
    writer.writerow(voltage_values)
    writer.writerow(current_values)
with open("EV\sampleFile.csv","r") as f :
    reader = csv.reader(f)
    for row in reader:
        print(row[:])