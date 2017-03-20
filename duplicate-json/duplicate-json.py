import json
import pdb

with open('example.json') as data_file:
    data = json.load(data_file)

for entry in data:
    for i in range(len(data[entry])):
        for j in data[entry][i]:
            data[entry][i][j+"_"] = data[entry][i][j]
            break
            
print("duplicated JSON file:")
print(data)
