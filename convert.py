import argparse
import sox
from os import path
from os import walk

parser = argparse.ArgumentParser(description='Converter')

# Required positional argument
parser.add_argument('raw_dir',
                    help='Path of the raw audio files')

# Required positional argument
parser.add_argument('out_dir',
                    help='Path of the converted audio files', default=None)

# Required positional argument
parser.add_argument('--samplerate',
                    help='Desired sample rate', type=int, default=11025)

# Required positional argument
parser.add_argument('--channels',
                    help='Desired number of channels', type=int, default=1)

# Required positional argument
parser.add_argument('--bitrate', type=int,
                    help='Desired bitrate', default=8)

args = parser.parse_args()

raw_dir = path.abspath(args.raw_dir)
out_dir = path.abspath(args.out_dir)
out_sample_rate=args.samplerate
out_num_channel=args.channels
out_bitrate=args.bitrate

tfm = sox.Transformer()
tfm = tfm.convert(out_sample_rate, out_num_channel, out_bitrate)

def sox_convert(in_path, out_path):
    try:
        tfm.build(in_path, out_path)
        print("Converted: {}".format(out_path))
    except Exception as e:
        print("Could not convert {}".format(in_path))
        print("Reason: {}".format(str(e)))
        exit()

print('Converting...')

raw_files = next(walk(raw_dir), (None, None, []))

for file in raw_files[2]:
    in_path = "{}/{}".format(raw_dir, file)
    out_path = "{}/{}".format(out_dir, file)
    sox_convert(in_path, out_path)