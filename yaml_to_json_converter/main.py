import json
import sys
import argparse
import yaml
from converter import convert
from pathlib import Path

parser = argparse.ArgumentParser(description="A simple yaml to json or vice versa converter program")

# create argument helper
def create_arg(long_flag, short_flag, help_msg, **kwargs):
    parser.add_argument(
        long_flag,
        short_flag,
        help = help_msg,
        **kwargs
    )



# args declaration
create_arg('--input', '-i', "The path to the input file", metavar = '<input_file>', type = str, required = True)
create_arg('--output', '-o', "The path to the output file", metavar = '<output_file>', type = str, required = True)
create_arg('--reverse', '-r', "Reverse the conversion", action = 'store_true')

def main():
    args = parser.parse_args()

    result = convert(
        input_file=args.input_file,
        output_file=args.output_file,
        isReverse=args.reverse
    )

    if result is None:
        sys.exit(1)

if __name__ == '__main__':
    main()
