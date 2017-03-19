import sys
import argparse
import numpy as np
import pdb

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--list', nargs='?', help='path to CSV file with single list of N+1 ints between 1 and N')
parser.add_argument('-s', '--stdin',  help='enter the list yourself', action="store_true")
parser.add_argument('-d', '--default',  help='default list (hardcoded into program)', action="store_true")

# grab args using argparse and put into dictionary
args = vars(parser.parse_args())

if not (args['list'] or args['stdin'] or args['default']):
    print("You did not select an option")
    sys.exit(0)

def find_duplicate(int_list):
    duplicates = []
    for i in int_list:
        if i in duplicates:
            print("duplicate: " + str(i))
            return
        duplicates.append(i)

if args['list']:
    int_list = np.genfromtxt(args['list'][0], delimiter=",", dtype=np.int)
    if len(int_list.shape) > 1:
        print("This program only accepts a single list of ints")
    else:
        find_duplicate(int_list)

if args['stdin']:
    print("Enter each integer separately and enter q or Q to quit")
    int_list = []
    user_input = ""
    while user_input != "q" and user_input != "Q":
        user_input = input("> ")
        if user_input.isdigit():
            int_list.append(int(user_input))
        elif user_input != "q" and user_input != "Q":
            print("Input not recognized")
    find_duplicate(int_list)

if args['default']:
    default_list = [1,3,3,1]
    print("The default list is: " + str(default_list))
    find_duplicate(default_list)
