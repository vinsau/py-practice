import argparse

parser = argparse.ArgumentParser(description="A friendly greeter program")

parser.add_argument('name', help="The name of the person to greet")
parser.add_argument(
    '-s',
    '--shout',
    action='store_true',
    help="Print the greeting in uppercase"
)

args = parser.parse_args()

greet = f"Hello, {args.name}"
if not args.shout:
    print(greet)
else:
    print(greet.upper() + '!')
    