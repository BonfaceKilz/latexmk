#!/usr/bin/env python3

'''
Supported templates are:
1. Letter
2. CV
3. Lab Report
4. Essay
5. Book
6. Competition Submission
7. Essay Collection
8. Invoice
'''
import argparse
from templates import letter
import data.details as info
import data.help_messages as help_message

# Create the doc
def createDoc(string):
    if string == 'l':
        x = letter.letter()
        x.gen_doc()
    elif string == 'bd':
        x = bd.basic()
        x.create_doc()
    else:
        print("This document type is not supported")

parser = argparse.ArgumentParser(prog=info.programName, description=info.programDescription, epilog=info.programEpilog)

# Make options mutually exclusive
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-c", "--create", choices=info.choices)
group.add_argument("-ls", "--list", help=help_message.listMessage, action="store_true")
args = parser.parse_args()

if args.create:
    createDoc(args.create)

if args.list:
    print(info.supportedTemp)

