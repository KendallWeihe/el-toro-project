### Algorithm to find the first duplicate entry in a list of integers

###### Note python version:
```
kendall@kendall-XPS-8500:~/Development/el-toro-project/duplicate-ints$ python --version
Python 3.4.3
```

###### Requirements:
Let's say you have a list of N+1 integers between 1 and N. You know there's at least one
duplicate, but there might be more. For example, if N=3, your list might be 3, 1, 1, 3 or it
might be 1, 3, 2, 2. Print out a number that appears in the list more than once. (That is, in
the first example, you can print '1' or '3' -- you don't have to print both.)

###### How to run:

**Get help**
```
kendall@kendall-XPS-8500:~/Development/el-toro-project/duplicate-ints$ python duplicate-ints.py -h
usage: duplicate-ints.py [-h] [-l [LIST [LIST ...]]] [-s] [-d]

optional arguments:
  -h, --help            show this help message and exit
  -l [LIST [LIST ...]], --list [LIST [LIST ...]]
                        path to CSV file with single list of N+1 ints between
                        1 and N
  -s, --stdin           enter the list yourself
  -d, --default         default list (hardcoded into program)
```

**Read a list of integers from a CSV file**
```
kendall@kendall-XPS-8500:~/Development/el-toro-project/duplicate-ints$ python duplicate-ints.py -l example.csv
duplicate: 3
```

**Enter a list of integers into STDIN**
```
kendall@kendall-XPS-8500:~/Development/el-toro-project/duplicate-ints$ python duplicate-ints.py -s
Enter each integer separately and enter q or Q to quit
> 1
> 3
> 3
> 1
> q
duplicate: 3
```

**Use the default list -- hardcoded into the program**
```
kendall@kendall-XPS-8500:~/Development/el-toro-project/duplicate-ints$ python duplicate-ints.py -d
The default list is: [1, 3, 3, 1]
duplicate: 3
```
