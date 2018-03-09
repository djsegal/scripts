import os
import sys
import pathlib

split_args = sys.argv[2].split("/")

massaged_args = [
  '/'.join([sys.argv[1], *split_args[:-1]]),
  split_args[-1]
]

cur_work_dir = os.getcwd()

cur_given_dir = massaged_args[0]

cur_dirs = [ "src", "test" ]

for cur_dir in cur_dirs:

  tmp_dir = os.path.join(cur_work_dir, cur_dir, cur_given_dir)

  pathlib.Path(tmp_dir).mkdir(parents=True, exist_ok=True)

  cur_file = os.path.join(tmp_dir, massaged_args[1])

  if cur_dir == "test":
    cur_file += "_test"

  cur_file += ".py"

  if not os.path.exists(cur_file):
      with open(cur_file, 'w'): pass
