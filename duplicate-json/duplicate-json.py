import json
import pdb
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', nargs='?', help='path to JSON file')
args = vars(parser.parse_args())

if not args['file']:
    print("You did not enter a path to the JSON file")
    sys.exit(0)

with open('example.json') as data_file:
    data = json.load(data_file)

for entry in data:
    for i in range(len(data[entry])):
        for j in data[entry][i]:
            data[entry][i]["_"+j] = data[entry][i][j]
            break

print("duplicated JSON file:")
print(data)
