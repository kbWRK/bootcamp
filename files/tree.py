import pathlib
import sys
import argparse
def print_dir(path, prefix=''):
    items_count = len(list(path.iterdir()))
    for n, x in enumerate(path.iterdir()):
        if n == items_count - 1 or items_count < 1:
            marker = "   ┗ "
            nextmarker = '   '
        else:
             marker = "   ┠ "
             nextmarker = '   │'


        if x.is_dir():
           print(prefix + marker + f' [{x.name}]')
           print_dir(x, prefix + nextmarker)
        else:
            print(prefix + marker + f'{x.name}')

print_dir(pathlib.Path(sys.argv[1]))
  #print_dir(pathlib.Path(r'C:\Users\kurs\workspace\projects\bootcamp\modules'))
if __name__ == '__main__':
    parser = argparse.ArgumentParser
    parser.add_argument()
