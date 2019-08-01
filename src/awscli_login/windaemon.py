import base64
import pickle
import sys
import os
import tempfile

from daemoniker import Daemonizer
from daemoniker._daemonize_windows import _NamespacePasser


def main(pidfile):
    dummy = "Hello World"
    print(pidfile)
    fd = open(pidfile, 'w')
    fd.write("test")
    fd.close()
    print(os.access(pidfile,os.R_OK))
    os.remove(pidfile)
    with Daemonizer() as (is_setup, daemonizer):
        is_parent, dummy = daemonizer(
           pidfile, dummy
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
    test = None
    if os.path.exists(argpath):
        with open(argpath, 'rb') as f:
            args = pickle.load(f, fix_imports=True)
        argFile = tempfile.NamedTemporaryFile(delete=False)
        worker_argpath = argFile.name
        os.environ["__AWS_CLI_WINDAEMON__"] = worker_argpath
        # Write an argvector for the 2nd pass.. Store this in the environment.
        with open(worker_argpath, 'wb') as wf:
            # Use the highest available protocol
            pickle.dump(args, wf, protocol=-1)
        test = args[0]
        print(test)
        main(test)
    else:
        testFile = os.path.join("C:\\Users\\althor.FC-OME-JEFFERSO", "pyTest.txt")
        f = open(testFile, 'a')
        argpath = os.environ['__AWS_CLI_WINDAEMON__']
        if os.path.exists(argpath):
            with open(argpath, 'rb') as ft:
                tmpArgs = pickle.load(ft, fix_imports=True)
            f.write("The file was there.. yay?" + argpath)
            f.write("args are" + str(tmpArgs))
            f.close()
            tmp = tmpArgs[0]
            main(tmp)

