import os
import argparse

import serializer

args_parser = argparse.ArgumentParser()
args_parser.add_argument('--path', type=str, help="Path for your file")
args_parser.add_argument('--format', type=str, help="Format of your file", choices=["json", "yaml"])

args_parser.add_argument('--save', type=str, help="Path for your file")

args = args_parser.parse_args()

formats = ["json", "yaml"]

path = args.path
format_ = args.format

formats.remove(format_)

save_path = args.save

print(f"{path} {format_}")

if not os.path.exists(path):
    print('File not found')

fp = path

obj = serializer.load(fp, format_)

serializer.dump(obj, formats[0], save_path)

# save

print("saved")

