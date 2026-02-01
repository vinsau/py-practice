import argparse
import json
import sys

parser = argparse.ArgumentParser(description="A simple program that prettifies json output")
parser.add_argument("filename", help="The name of the file")

args = parser.parse_args()

try:
    with open(args.filename, 'r') as f:
        data = json.load(f)
        out = json.dumps(data, indent=4)
        print(out)
except FileNotFoundError:
    print("Error: file is invalid or nowhere to be found")    