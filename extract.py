#!/usr/bin/env python3

import os
import sys
import argparse

pageCount = 0
noErrors = True

def updatePageCount():
    global pageCount
    pageCount += 1
    sys.stdout.write("\rFound {} pages".format(pageCount))
    sys.stdout.flush()


def printMessage(message):
    sys.stdout.write(message)
    sys.stdout.flush()


def main():
    parser = argparse.ArgumentParser(
        description='Extract data from Wiktionary xml dump'
    )
    parser.add_argument(
        'file',
        type=str,
        help='Wiktionary xml dump of article pages'
    )
    parser.add_argument(
        '-o',
        type=str,
        help='Output file name'
    )
    args = parser.parse_args()
    inputfile = None
    outputfile = None
    if not os.path.isfile(args.file):
        printMessage("File {} does not exist. Exiting...".format(args.file))
        sys.exit()

    try:
        inputfile = open(args.file, 'r', encoding='utf-8')
        outputfile = open(args.file + '.en', 'w+', encoding='utf-8')


        line = inputfile.readline()
        # Find first occurence of <page>
        while line:
            if '<page>' in line:
                updatePageCount()
                break
            line = inputfile.readline()
            
        page = ''
        while line:
            if '</page>' in line:
                page += line
                if '<ns>10</ns>' in page:
                    outputfile.writelines(page)
                page = ''
            elif '<page>' in line:
                updatePageCount()
                page = ''
                page += line
            else:
                page += line

            line = inputfile.readline()
                
    except Exception as e:
        global noErrors
        noErrors = False
        printMessage(e)
        return
    finally:
        inputfile.close()
        outputfile.close()
    
    if noErrors:
        printMessage('English pages extracted successfully')
    return


if __name__ == '__main__':
    main()