import sys
import argparse
import logging
from s3_ops import upload_to_s3
from ec2_ops import find_and_tag_instances

# create logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s %(message)s',
    handlers = [
        logging.FileHandler('../../logs/app.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

log = logging.getLogger(__name__)
parser = argparse.ArgumentParser(
    description="A simple program that manages aws services",
    usage="aws_manager.py [-h] [--upload <filepath>] [--bucket <bucket_name>] | [--tag-instances] [--key <keyname>][--value <value>]"
)

# argument creation helper
def create_arg(long_flag, short_flag, help_msg, **kwargs):
    parser.add_argument(
        long_flag,
        short_flag,
        help = help_msg,
        **kwargs
    )

# create arguments

# bucket flags
create_arg('--upload', '-u', "Add the file path of the file to be uploaded", type=str, metavar='<filepath>')
create_arg('--bucket', '-b', "Name of the bucket", type=str, metavar='<bucket_name>')

# ec2 flags
create_arg('--tag-instances', '-t', 'Tag instances', action='store_true')
create_arg('--key', '-k', 'Add the tag key', type=str, metavar='<keyname>')
create_arg('--value', '-v', 'Add the tag value', type=str, metavar='<value>')

# load args
args = parser.parse_args()

# group related flags
bucket_flags = [args.upload, args.bucket]
ec2_flags = [args.tag_instances, args.key, args.value]

# Handle errors
if not any(bucket_flags) and not any(ec2_flags):
    parser.error("Flags must be used to run the program, refer to the usage")
if any(bucket_flags) and any(ec2_flags):
    parser.error("Bucket and EC2 flags cannot be used together")

if any(bucket_flags) and not all(bucket_flags):
    parser.error("Bucket management requires both (--upload | -u) and (--bucket | -b) to work.")

if any(ec2_flags) and not all (ec2_flags):
    parser.error("EC2 tagging requires (--tag-instances | -t), (--key | -k) and (--value | -v) to work.")

# run
def main():
    log.info("Starting application...")
    if all(bucket_flags):
        upload_to_s3(args.upload, args.bucket)
    elif all(ec2_flags):
        find_and_tag_instances(args.key, args.value)
    log.info("Stopping application...")

if __name__ == '__main__':
    main()