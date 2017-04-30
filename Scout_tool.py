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


f=open('world_results.csv','r')
csv_file=csv.reader(f, delimiter=",")

named = {}
for line in csv_file:
    # in case there are multiple entries with same name
    # assuming names are in the first column
    named[line[0]] = named.get(line[0]) or []
    named[line[0]].append(line)

sorted_name_key = sorted(named)
name_sorted = []
for key in sorted_name_key:
    name_sorted.extend(named[key])

print("Done! 'world_results' CSV file sorted!")