#!/usr/bin/env python3

# Letter test

import sys
import os
import argparse
sys.path.append('/home/bonface/workspace/learning/latexmk/templates')
import letter
import document_basic as bd

def run(string):
    if string == "letter":
        x = letter.letter()
        x.gen_doc()
    elif string == "bd":
        x = bd.basic()
        x.create_doc()

def clean(string):
    print('Cleaning file')
    if os.path.exists(string+".tex"):
        os.remove(string+".tex")
    if os.path.exists(string+".pdf"):
        os.remove(string+".pdf")

parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.add_argument("--clean", action="store_true")
parser.add_argument("--run", action="store_true")
args = parser.parse_args()

if args.run:
    run(args.file)
if args.clean:
    if args.file=='bd':
        clean('Basic')
    else:
        clean(args.file)
