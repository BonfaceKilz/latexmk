'''
A sample test for various modules
'''
import os
import sys
sys.path.insert(0, '../templates')
import letter

x = letter.letter()
#x.create_doc()
x.gen_doc()
