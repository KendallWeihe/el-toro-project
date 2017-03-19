### Title

### Requirements:
In the language of your choice, write a script to handle a csv file manipulation, and
remove invalid lines (bad formatting, etc) and then display and only output the 4th
column. Try to make it as efficient as possible in the time allowed. Assume you could
have a huge csv file.

### Preliminary notes on performance:
  I went into this project with the idea that `NumPy`'s `genfromtxt()` method performed much better than the standard Python `csv` package. I decided to test the difference. I developed a small program `measure-performance.py` that compares the two packages. To my surprise, the `csv` package performed upwards of 10x faster than `NumPy`'s `genfromtxt()`! Run `python measure-performance.py` for results (note I used an old CSV file I had `Kentucky_Louisville_161221.csv`).

  Output:
```
kendall@kendall-XPS-8500:~/Development/el-toro-project/csv-file-manip$ python csv-file-manip.py
Performance results:
CSV package time: 0.0023887157440185547
NumPy package time: 0.02461409568786621
NumPy / CSV ratio: 10.304321788601657
```

  Since `csv` performed much better, this is what I decided to use in the main program `csv-file-manip.py`.

  TODO: talk about how a different language could perform better

### The following cases are handled:

  - missing element(s) in row
    - i.e. `0,1,2,,4,5` or even `,,,,,`
    - print error message and throws the row out entirely
  - wrong type of data
    - i.e. `-t int` is specified in arguments, but the following row exists: `0,1,2,three,4,5`
    - print error message and throws the row out entirely

### How to run:
