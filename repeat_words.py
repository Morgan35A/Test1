import argparse
import sys

#print (sys.argv)

parser = argparse.ArgumentParser(description= 'répète mots')
parser.add_argument('--mot', required=True)
parser.add_argument("--n", type=int, required=True, help='nombre de répétitions')
args = parser.parse_args()

for i in range(args.n):
    print(args.mot)

