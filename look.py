#! /usr/bin/env python

import argparse
import datetime
import stat
from pathlib import Path

parser = argparse.ArgumentParser(
    prog="look",
    description="Look into a directory; A pretty-printed ls",
    epilog="Made by @daikondev, 2023",
)
parser.add_argument("path", nargs="?", default=".")
args = parser.parse_args()

target_dir = Path(args.path)


def build_output(entry):
    perm = stat.filemode(entry.stat().st_mode)
    size = entry.stat().st_size
    date = datetime.datetime.fromtimestamp(
        entry.stat().st_mtime).strftime(
        "%b %d %H:%M:%S"
    )
    return f"{perm} {size:>6d}   {date}  {entry.name}"


if not target_dir.exists():
    print("Target directory doesn't exist")
    raise SystemExit(1)


print("==================================================================")
if args.path == ".":
    print(f"Current working directory")
else:
    print(target_dir)
print("==================================================================")
print("Permissions | Size | Last Modified | Name")
print("==================================================================")
for entry in target_dir.iterdir():
    print(build_output(entry))
print("==================================================================")

