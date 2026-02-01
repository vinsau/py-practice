import sys
import argparse
import subprocess

parser = argparse.ArgumentParser(description="A system health checker program")

# helper function to create args
def create_args(long_flag, short_flag, help_msg):
    parser.add_argument(
    long_flag,
    short_flag,
    action = 'store_true',
    help = help_msg
)

# execute command with subprocess
def execute_bash(cmd):
    try:
        result = subprocess.run(
            cmd,
            capture_output = True,
            text = True,
            check = True
        )
    except subprocess.CalledProcessError as e:
        print(f"Caught Error: {e}")
        sys.exit(1)
    return result

# output helper
def print_out(out, header, metric):
    print('\n', header)
    
    category = ''
    split_lines = out.splitlines()

    try:
        get_line = None
        if metric == 'disk':
            get_line = '/dev/sda1'
            category = split_lines[0]
        elif metric == 'cpu':
            get_line = 'load average'
        elif metric ==  'memory':
            get_line = 'Mem:'
            category = split_lines[0]
        else:
            raise ValueError
    except ValueError:
        print("Caught Error: line not found")
        sys.exit(1)
    
    result = "Error: error finding metric"
    # find the line then cut
    for line in split_lines:
        pos = line.find(get_line)
        if pos != -1:
            result = line[pos:]
    if category != '':
        print(category)

    print(result, '\n')

# declare args
create_args('--disk', '-d', "Shows disk usage")
create_args('--cpu', '-c', "Shows CPU load")
create_args('--memory', '-m', "Shows memory usage")

args = parser.parse_args()

show_all = (not args.disk) and (not args.cpu) and (not args.memory)

# show results
try:
    if args.disk or show_all:
        disk = execute_bash(['df', '-h'])
        print_out(disk.stdout, 'Disk:', 'disk')
    if args.cpu or show_all:
        cpu = execute_bash(['uptime'])
        print_out(cpu.stdout, 'CPU:', 'cpu')
    if args.memory or show_all:
        memory = execute_bash(['free', '-h'])
        print_out(memory.stdout, 'Memory:', 'memory')
except Exception as e:
    print(f"Caught Error: {e}")
    sys.exit(1)