#!/usr/bin/python

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
import os
import sys
from templates import letter

x = letter.letter()
x.create_doc()
x.gen_doc()
