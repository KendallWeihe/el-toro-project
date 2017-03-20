import requests
from bs4 import BeautifulSoup
import pdb
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--link', nargs='?', help='link to Twitter\'s Moments page')
parser.add_argument('-o', '--output_file', nargs='?', help='path to output JSON file')
args = vars(parser.parse_args())

if args['link']:
    link = args['link']
else:
    link = "https://twitter.com/i/moments"
r = requests.get(link)
soup = BeautifulSoup(r.text, "html.parser")

tweets = soup.findAll('div', class_='MomentCapsuleSummary-details')
json_output = {'tweets': []}
for tweet in tweets:
    try:
        headline = str(tweet.findAll('a')[0].string).strip()
        subtitle = str(tweet.findAll('div', class_='MomentCapsuleSubtitle')[0].findAll('span')[0].string).strip()
        description = str(tweet.findAll('div', class_='MomentCapsuleSummary-description')[0].string).strip()
        num_likes = str(tweet.findAll('div', class_='MomentCapsuleLikesCount')[0].string).strip()

        line = {'headline': headline, 'subtitle': subtitle, 'description': description, 'num_likes': num_likes}
        json_output['tweets'].append(line)
    except:
        pass

if args['output_file']:
    output_file = args['output_file']
else:
    output_file = "./default-output.json"

with open(output_file, 'w') as outfile:
    json.dump(json_output, outfile, indent=2)
