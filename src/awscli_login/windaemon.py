import sys
import os

from daemoniker import Daemonizer


def main():
    dummy = "Hello World"
    with Daemonizer() as (is_setup, daemonizer):
        is_parent, dummy = daemonizer(
            os.path.join("C:\\Users\\althor.FC-OME-JEFFERSO", "test.pid"), dummy
        )
        if is_parent:
            print("in parent")
            dummy = "Hello Parent"
        if not is_parent:
            print("in child")
            testFile = os.path.join("C:\\Users\\althor.FC-OME-JEFFERSO", "pyTest.txt")
            f = open(testFile, 'a')
            f.write(dummy)
            f.close()
            dummy = "Hello bob"


if __name__ == '__main__':
    argpath = sys.argv[1]
    main()
