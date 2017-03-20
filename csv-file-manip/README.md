### CSV file manipulation

### Requirements:
In the language of your choice, write a script to handle a csv file manipulation, and
remove invalid lines (bad formatting, etc) and then display and only output the 4th
column. Try to make it as efficient as possible in the time allowed. Assume you could
have a huge csv file.

### Preliminary notes on performance:
  I went into this project with the idea that `NumPy`'s `genfromtxt()` method performed much better than the standard Python `csv` package. I decided to test the difference. I developed a small program `measure-performance.py` that compares the two packages. To my surprise, the `csv` package performed upwards of 10x faster than `NumPy`'s `genfromtxt()`! Run `python measure-performance.py` for results (note I used an old CSV file I had `Kentucky_Louisville_161221.csv`).

  Output:
```
kendall@kendall-XPS-8500:~/Development/el-toro-project/csv-file-manip$ python measure-performance.py
Performance results:
CSV package time: 0.0023887157440185547
NumPy package time: 0.02461409568786621
NumPy / CSV ratio: 10.304321788601657
```

  Since `csv` performed much better, this is what I decided to use in the main program `csv-file-manip.py`. I'm aware that Python is not the fastest language for most things, so for larger datasets, other languages are probably better suited.

### The following invalid cases are handled:

  - missing element(s) in row
    - i.e. `0,1,2,,4,5` or even `,,,,,`
    - print error message and throws the row out entirely
  - wrong type of data
    - i.e. `-t int` is specified in arguments, but the following row exists: `0,1,2,three,4,5`
    - print error message and throws the row out entirely

### How to run:

**Get help**:
```
kendall@kendall-XPS-8500:~/Development/el-toro-project/csv-file-manip$ python csv-file-manip.py -h
usage: csv-file-manip.py [-h] [-c [CSV_FILE]] [-t [TYPE]] [-e]

optional arguments:
  -h, --help            show this help message and exit
  -c [CSV_FILE], --csv-file [CSV_FILE]
                        path to CSV file
  -t [TYPE], --type [TYPE]
                        type of data in CSV file -- int, float, or string
                        accepted
  -e, --empty           detect empty elements
```

**Argument flags**
  - `-c` or `--csv-file` specifies the path to the CSV file
  - `-t` or `--type` specifies the data type the CSV file is
  - `-e` or `--empty` detects if there are any empty/invalid entries

**Example runs**

Using the example CSV file, `example-small-w-error.csv`

Detect empty entries and convert to integer data type:
```
kendall@kendall-XPS-8500:~/Development/el-toro-project/csv-file-manip$ python csv-file-manip.py -c example-small-w-error.csv -e -t int
Error in converting to your data type or there is an empty entry in row: ['5', '6', '', '8']
Error in converting to your data type or there is an empty entry in row: ['13', 'fourteen', '15', '16']


Entire CSV file data:
[[1, 2, 3, 4], [9, 10, 11, 12]]


Data in column 4:
[4, 12]
```

Do not detect empty entires and convert to string data type:
```
kendall@kendall-XPS-8500:~/Development/el-toro-project/csv-file-manip$ python csv-file-manip.py -c example-small-w-error.csv -t string


Entire CSV file data:
[['1', '2', '3', '4'], ['5', '6', '', '8'], ['9', '10', '11', '12'], ['13', 'fourteen', '15', '16']]


Data in column 4:
['4', '8', '12', '16']
```
