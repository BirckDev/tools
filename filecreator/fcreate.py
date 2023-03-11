"""
A tool to create a binary file of a certain size.

This tool is based on (almost an exact copy) the work of Marcin Jakuszko
from: https://marcinjakuszko.medium.com/how-to-create-a-large-file-in-a-seconds-python-7080c8dbeee0
"""
import os
import argparse

def generate_file(size_in_bytes, file_name):
  with open(file_name, 'wb') as file:
    file.write(os.urandom(size_in_bytes))


def main():
  parser = argparse.ArgumentParser(description='Generate file with name and size bytes [python fscreate -n <filename> -s <size in bytes>]')
  parser.add_argument('-s', type=int, required=True, dest='size', help='Size of the file in bytes')
  parser.add_argument('-n', type=str, required=True, dest='name', help='Name of the file')

  arguments = parser.parse_args()
  generate_file(arguments.size, arguments.name)


if __name__ == '__main__':
  main()