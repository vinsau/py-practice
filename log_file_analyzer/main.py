import sys
import os
import platform
import subprocess

default_log_file = os.environ.get("DEFAULT_LOG_FILE")

# get default log path
def get_default_log():
    os_name = platform.system()
    default_log_path = None

    if os_name == 'Windows':    
        default_log_path = os.path.join("C:\\", "Windows", "System32", "drivers", "etc", "hosts")
    elif os_name == "Linux":
        default_log_path = os.path.join(os.sep, 'var', 'log', 'pacman.log')
    elif os_name == "Darwin":
        default_log_path = os.path.join(os.sep, 'var', 'log', 'system.log')
    else:
        print(f"Unknown OS: {os_name}")
    
    return default_log_path

# run shell command
def execute_bash(cmd):
    try:
        result = subprocess.run(
        cmd,
        capture_output = True,
        text = True,
        check = True
        )
    except FileNotFoundError:
        print(f"Caught Error: '{cmd}' is invalid or nowhere to be found")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Caught Error: {e}")
    
    return result.returncode



# check for file validity
if len(sys.argv) > 1:
    filename = sys.argv[1]
elif default_log_file:
    filename = default_log_file
else:
    filename = get_default_log()



# Analyze file stats
try:
    print(f"Analyzing {filename}...")
    count = word1_count = word2_count = 0
    word1 = "ERROR"
    word2 = "WARNING"
    
    with open(filename, 'r') as f:
        for line in f:
            count += 1
            if word1 in line:
                word1_count += 1
            if word2 in line:
                word2_count += 1

    # print results
    print(f"File name: {filename}")
    print(f"Total Lines: {count}")
    print(f"'{word1}' count: {word1_count}")
    print(f"'{word2}' count: {word2_count}")

    # archive file if second argument is detected
    if len(sys.argv) > 2 and (sys.argv[2] == '--archive'):
        log_dir = 'log_backups'
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
        print(f"Archiving {filename}...")
        gzip_code = execute_bash(['gzip', filename])
        if gzip_code == 0:
            gz_file = filename + '.gz'
            move_log_code = execute_bash(['mv', gz_file, log_dir])
            if move_log_code == 0:
                log_backup_path = os.path.join(os.sep, log_dir, gz_file)
                print(f"Successfully archived to {log_backup_path}")
            else:
                print(f"Error moving the file to {log_dir}")
        else:
            print(f"Archiving failed... {gzip_code}")

except FileNotFoundError:
    print(f"Error: the file {filename} is invalid")
    sys.exit(1)