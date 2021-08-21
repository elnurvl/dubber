import argparse
import sox
from os import walk
from os import path
import csv

parser = argparse.ArgumentParser(description='Measurer')

# Required positional argument
parser.add_argument('original',
                    help='Path of the original audio files')

# Optional positional argument
parser.add_argument('replicated', nargs='?',
                    help='Path of the replicated audio files', default=None)

# Optional positional argument
parser.add_argument('--output',
                    help='Output path for the generated CSV file', default=None)

args = parser.parse_args()

original_path = path.abspath(args.original)
output = path.abspath(args.output or 'durations.csv')

def sox_length(path):
    try:
        length = sox.file_info.duration(path)
        return length
    except Exception as e:
        print("Error getting the file info: {}".format(str(e)))
        return None


def add_to_csv(rows, files, original=True):
    if (files is None):
        return
    original_path = files[0]
    for file in files[2]:
        name = path.splitext(file)[0].split('-')[0]
        length = sox_length(path.join(original_path, file))
        if (any(e[0] == name for e in rows)):
            [e for e in rows if e[0] == name][0].append(length)
        else:
            if (original):
                rows.append([name, length])
            else:
                rows.append([name,None,length])

original_files = next(walk(original_path), (None, None, []))  # [] if no file

headings = ['Name', 'Original']

if (args.replicated is not None):
    replicated_path = path.abspath(args.replicated)
    replicated_files = next(walk(replicated_path), (None, None, []))
    headings += ['Replicated'] * 10
else:
    replicated_files = None


rows = list()

print('Measuring...')

add_to_csv(rows, original_files)
add_to_csv(rows, replicated_files, False)

print('Ready for writing.')

print('Writing to a file...')

try:
    with open(output, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(headings)
        writer.writerows(rows)
        
        print('Done.')
except Exception as e:
    print("Error occured during writing to a file: {}".format(str(e)))


