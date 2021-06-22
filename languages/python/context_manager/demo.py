import os
from contextlib import contextmanager


class Change_Dir():
  def __init__(self, destination):
    pass
  def __enter__(self):
    pass
  def __exit__(self):
    pass
  
  
@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir('Sample-Dir-One'):
    print(os.listdir())

with change_dir('Sample-Dir-Two'):
    print(os.listdir())
