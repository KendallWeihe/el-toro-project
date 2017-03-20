### Scrape Twitter's Moments feed

Program to scrape the headlines and information from Twitter's Moments page -- found [here](https://twitter.com/i/moments)

### Requirements:

In any language you choose, create a script to query a social media feed (Ex: twitter,
pinterest, facebook, etc) for any sort of filtered data. Explain why you chose to get that
data, and store the data in a json result file in jsonline format.

### How to run:

**Get help:**
```
kendall@kendall-XPS-8500:~/Development/el-toro-project/scrape-twitter$ python2 scrape-twitter.py -h
usage: scrape-twitter.py [-h] [-l [LINK]] [-o [OUTPUT_FILE]]

optional arguments:
  -h, --help            show this help message and exit
  -l [LINK], --link [LINK]
                        link to Twitter's Moments page
  -o [OUTPUT_FILE], --output_file [OUTPUT_FILE]
                        path to output JSON file
```

**Run with default settings:**
```
kendall@kendall-XPS-8500:~/Development/el-toro-project/scrape-twitter$ python2 scrape-twitter.py
```

**Run with specified links and files:**
```
kendall@kendall-XPS-8500:~/Development/el-toro-project/scrape-twitter$ python2 scrape-twitter.py -l https://twitter.com/i/moments -o user-specified.json
```
