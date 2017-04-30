import csv

x=1

filename = "world_results.csv"
# opening the file with w+ mode truncates the file
c = open(filename, "w+")
c.close()

with open('world_results.csv', 'a') as csvfile:
    fieldnames = ['World', 'Location']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    csvfile.close()

while x==1:
    try:
        input = raw_input
    except NameError:
        pass

    print("Input 0 to sort!")
    world = input("World: ")

    if world == "0":
        x = 0
        csvfile.close()

    else:
        location = input("location: ")
        with open('world_results.csv', 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'World': world, 'Location': location})

import operator

data = csv.reader(open('world_results.csv'), delimiter=',')
sortedlist = sorted(data, key=operator.itemgetter(1))  # 0 specifies according to first column we want to sort
# now write the sorte result into new CSV file
with open("world_results.csv", "wb") as f:
    fileWriter = csv.writer(f, delimiter=',')
    for row in sortedlist:
        fileWriter.writerow(row)

print("Done! 'world_results' CSV file sorted!")