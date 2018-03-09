import os
import sys
import pathlib

cur_work_dir = os.getcwd()

cur_given_dir = sys.argv[1]

cur_dirs = [ "src", "test" ]

for cur_dir in cur_dirs:

  tmp_dir = os.path.join(cur_work_dir, cur_dir, cur_given_dir)

  cur_file = os.path.join(tmp_dir, sys.argv[2])

  if cur_dir == "test":
    cur_file += "_test"

  cur_file += ".py"

  if os.path.exists(cur_file):
      os.remove(cur_file)

  if os.path.exists(tmp_dir):
    os.removedirs(tmp_dir)
