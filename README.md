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

### Measure

To compare audio datasets run the following command:

```
python measure.py <original_dir> <dubbed_dir>
```

A CSV file will be generated under the directory from where you run the script. You can specify the output file name by setting the `--output` flag to the path of the file.

If you just want to get the durations of files in a directory you can omit the second argument.

### Convert

To change audio quality of multiple files in a batch you can use the following command:

```
python convert.py <source_dir> <output_dir> --samplerate=<samplerate> --bitrate=<bitrate> --channels=<number_of_channels>
```

### Seconds2Timecode

Audacity has a great feature allows users exporting audio labels in a text file.
However, timestamps are exported as seconds which are incompatible with industry-standard DAWs(e.g. Nuendo).
To import the audio labels in those software, timestamps need to be in the `hh:mm:ss:ff` format.
Unfortunately, Audacity does not give an option to configure the format of a generated labels file as of now.
The following command will help you to fix the timecode formats in a label data exported by Audacity:

```
python seconds2timecode.py <path_to_labels_file> --framerate=<framerate_of_timecode> --output=<output_dir_for_generated_csv>
```