# Dubmeter

This scipt compares durations for two sets of audio files. This is useful when you are doing a dubbing project where you need to monitor length of dubbed audio files, so they are close to the original ones and match the scene.


## Dependencies

Make sure you have Python3 and [SoX](https://sourceforge.net/projects/sox/files/sox/14.4.2/) installed and the binaries(python and sox) are added to your `PATH`.

## Installation

Run the following command from the root of the repository before using the script:

```
pip install -r requirements.txt
```

## Usage

To compare audio datasets run the following command:

```
python analyse.py <original_dir> <dubbed_dir>
```

A CSV file will be generated under the directory from where you run the script. You can specify the output file name by setting the `--output` flag to the path of the file.

If you just want to get the durations of files in a directory you can omit the second argument.