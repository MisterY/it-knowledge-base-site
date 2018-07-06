""" Iterate through the folder structure and create a full Table of Contents """

import os
from pathlib import Path
from glob import iglob

def iterate_glob():
    """ List all files with glob """
    rootdir_glob = rootdir._str + "/**/*"

    file_list = [f for f in iglob('**/*', recursive=True) if os.path.isfile(f)]
    for f in file_list:
        print(f)

def iterate_walk(rootdir: str):
    """ Iterate all folders/files using os.walk """
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            file_path = os.path.join(subdir, file)
            print(file)

def main():
    #rootdir = __file__
    rootdir = Path(__file__).parent
    print(f"starting in {rootdir}")

    #iterate_glob()
    # iterate_walk(rootdir)

    # todo: each folder is a node in the tree, with a link to "folder/"
    # todo: each file is shown in a parent folder if it is .md and does not start with underscore.

if __name__ == "__main__":
    main()
