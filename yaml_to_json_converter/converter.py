import sys
import json
import yaml

# print output helperssss
def print_output(input_f, output_f):
    print(f"Successfully converted '{input_f}' into '{output_f}'")

def convert(args, input_file, output_file, isReverse, in_ext):
    try:
        
        with open(input_file, 'r') as infile:
            if isReverse and in_ext == '.json':
                input_data = json.load(infile)
            elif in_ext == '.yaml' and not isReverse:
                input_data = yaml.safe_load(infile)
            else:
                raise ValueError(f"input file must be of '{'.json' if isReverse else '.yaml'}' extension.")

        with open(output_file, 'w') as outfile:
            if not isReverse:
                json.dump(input_data, outfile, indent=4)
            else:
                yaml.dump(input_data, outfile)
                print_output(input_file, output_file)
        
        return { 'status': 'success' }
    except FileNotFoundError:
        print(f"Caught Error: the file {args.input} is invalid or nowhere to be found.")
        return None
    except ValueError as e:
        print(f"Caught Error: {e}")
        return None

