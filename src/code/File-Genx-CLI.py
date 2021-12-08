'''
Title: File Genx (CLI version)
License: MIT
GitHub: https://github.com/pedroter7/file-genx

This is a CLI version of File Genx. This script works by simply 'emulating' the GUI input.
'''

import argparse

from Generator import Generator

VALID_CONTENT_PER_STRINGS = [
    'line',
    'char',
    'par'
]

VALID_CONTENT_TYPE_STRINGS = [
    'rand',
    'web-lipsum'
]

def createArgParser():
    argParser = argparse.ArgumentParser(
        description='File-Genx CLI version. Visit https://github.com/pedroter7/file-genx for more info.'
    )

    argParser.add_argument('--files-number', metavar='N', type=int, required=True, help='Number of files to be generated.')
    argParser.add_argument('--content-length', metavar='N', type=int, required=True, help='Length of the content of each file.')
    argParser.add_argument('--content-count-per', metavar='VALUE', type=str, required=False, default='line', help='How to count the content length. Default is line and allowed values are line, par (for paragraphs) and char (for characters).')
    argParser.add_argument('--content-type', metavar='TYPE', type=str, required=True, help='How to generate the content of each file. Allowed values are rand (for random characters) and web-lipsum (to generate some Lorem Ipsum like content from web API calls).')
    argParser.add_argument('--out-dir', metavar='DIR_PATH', type=str, required=True, help='Path to the directory where the generated files should be placed.')

    return argParser

def normalizeString(string):
    return string.strip().lower()

def normalizeArgs(args):
    args.content_count_per = normalizeString(args.content_count_per)
    args.content_type = normalizeString(args.content_type)
    args.out_dir = normalizeString(args.out_dir)

def validateArgs(args):
    if args.files_number < 1:
        return False, 'Invalid --files-number argument. Must be greater than 0.'

    if args.content_length < 1:
        return False, 'Invalid --content-length argument. Must be greater than 0.'

    if args.content_count_per not in VALID_CONTENT_PER_STRINGS:
        return False, 'Invalid --content-count-per argument. Unknown option.'

    if args.content_type not in VALID_CONTENT_TYPE_STRINGS:
        return False, 'Invalid --content-type argument. Unknown option.'

    if len(args.out_dir) == 0:
        return False, 'Invalid --out-dir argument. Must not be empty. Must be the path to some directory.'

    return True,''

def translateArgs(args):
    translated = {
        "nFilesSpinButton":args.files_number,
        "nContentSpinButton":args.content_length,
        "nContentComboBox":args.content_count_per,
        "contentTypeComboBoxText":args.content_type,
        "destinationChooser":args.out_dir
    }

    return translated

def main():
    argParser = createArgParser()
    args = argParser.parse_args()
    normalizeArgs(args)
    validArgs,errorMsg = validateArgs(args)

    if (not validArgs):
        print('Argument error: {error}'.format(error=errorMsg))
        argParser.print_help()
        exit(1)

    translatedArgs = translateArgs(args)

    generator = Generator(translatedArgs)
    generator.generate()

if __name__ == '__main__':
    main()