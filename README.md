## WIKTIONARY-EXTRACTOR-PY

**WIKTIONARY-EXTRACTOR-PY** is a work-in-progress Python program that is meant to extract useful data from the Wiktionary XML dump available at [this link](https://dumps.wikimedia.org/enwiktionary/latest/).

The extracted data will be stored in a SQLite database. The end goal is to use this database in a dictionary app for Android.

## WORK IN PROGRESS

The project is currently a work in progress and doesn't yet achieve its goal of extracting useful data.

## Setting up

### Clone this repository
Clone this repository into your local machine.

    https://github.com/davidaik/wiktionary-extractor-py.git

### Get the relevant Wiktionary XML dump file

This program is meant to extract data from a file available at [this link](https://dumps.wikimedia.org/enwiktionary/latest/), particularly the `enwiktionary-latest-pages-articles.xml.bz2`.

Download the file and extract it into the same location as the `extract.py` file that you got upon cloning the repository.


## Usage

The program is written for Python 3.

To use the program, cd into the directory containing the `extract.py` file and execute it with the available query types.

The basic structure of commands for running the program is shown below.

`$ python3 extract.py XML_FILE_NAME`

`XML_FILE_NAME` is the full name of the Wiktionary XML dump that you extracted.


## License
> MIT License

> Copyright (c) 2019 David Heisnam

> Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

> The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
