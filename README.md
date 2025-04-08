### README

## Project Overview

This project consists of two main scripts: `words.py` and `download.py`. The `words.py` script processes a text file containing words and filters out unwanted characters and phrases. The `download.py` script downloads the US pronunciation audio files for the words and combines them into a single audio file with intervals between each word.

## Prerequisites

- Python 3.x
- `requests` library
- `pydub` library
- `ffmpeg` installed and added to the system PATH

## Installation

1. Install the required Python libraries:
    ```sh
    pip install requests pydub
    ```

2. Download and install `ffmpeg` from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html) and ensure it is added to your system PATH.

## Usage

### Step 1: Process the Words File

1. Place your input file (e.g., `单词11.txt`) in the project directory.
2. Update the `input_file` and `output_file` variables in `words.py` to match your input and output file names.
3. Run the `words.py` script to process the words:
    ```sh
    python words.py
    ```

### Step 2: Download Pronunciation Audio Files

1. Ensure the `output_file` from the previous step (e.g., `单词11_new.txt`) is in the project directory.
2. Update the `words` list in `download.py` to read from your processed file.
3. Run the `download.py` script to download the audio files and combine them:
    ```sh
    python download.py
    ```

## Example

### Input File: `单词11.txt`
```text
irrigation       n.灌溉
mining           n.采矿业
contaminants           n.污染物
```

### Processed File: `单词11_new.txt`
```text
irrigation,mining,contaminants,
```

### Combined Audio File: `combined_11_new.mp3`

The `combined_11_new.mp3` file will contain the US pronunciations of the words "irrigation", "mining", and "contaminants" with intervals between each word.
