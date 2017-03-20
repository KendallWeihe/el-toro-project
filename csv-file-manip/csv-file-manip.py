import csv
import pdb
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--csv-file', nargs='?', help='path to CSV file')
parser.add_argument('-t', '--type', nargs='?', help='type of data in CSV file -- int, float, or string accepted')
parser.add_argument('-e', '--empty',  help='detect empty elements', action="store_true")

# grab args using argparse and put into dictionary
args = vars(parser.parse_args())

csv_file = args['csv_file']
data = []
with open(csv_file, 'r') as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        if args['type']:
            try:
                if args['type'] == 'int':
                    row = [int(i) for i in row]
                elif args['type'] == 'float':
                    row = [float(i) for i in row]
                elif args['type'] == 'string':
                    row = [str(i) for i in row]
                else:
                    print("Data type not recognized, enter -h flag for help")
            except ValueError:
                # invalid data type -- throw away row
                print("Error in converting to your data type or there is an empty entry in row: " + str(row))
                row = None

        if row != None:
            if args['empty']: # detect empty elements
                if '' not in row:
                    data.append(row)
                else:
                    print("There was an empty entry in row: " + str(row))
            else:
                data.append(row)

print("\n")
print("Entire CSV file data:")
print(data)
print("\n")
print("Data in column 4:")
column_4 = [[row[i] for row in data] for i in range(3,4)]
print(column_4[0])
