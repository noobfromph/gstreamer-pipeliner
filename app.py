import argparse
import os
import subprocess
import gi
gi.require_version('Gst', '1.0')

from gi.repository import Gst
Gst.init(None)

from pipeline import Pipeline

parser = argparse.ArgumentParser(description='Create Gstreamer pipeline from JSON')
parser.add_argument('file', type=argparse.FileType('r'), help='JSON file pipeline to process')
parser.add_argument('--exec', action='store_true', help='Execute pipeline after')
args = parser.parse_args()

file_path = args.file.name

if not file_path:
    raise ValueError('File is required')

if not os.path.exists(file_path):
    raise FileNotFoundError('File not found')

if __name__ == '__main__':
    pipe = Pipeline(file_path)
    result = pipe.get()
    print(result)

    if args.exec:
        subprocess.Popen(f'{result}', shell=True)