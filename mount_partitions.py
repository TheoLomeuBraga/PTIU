import partition_manager as pmanager
import sys

def create_partitions(dev):
    pmanager.create_partitions(dev)

args = []
if __name__ == "__main__":
    if len(sys.argv) == 2:
        for i, arg in enumerate(sys.argv):
            args.append(arg)
        create_partitions(args[1])
        