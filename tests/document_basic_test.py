'''
A sample test for the document_basic module
'''
import sys
sys.path.insert(0, '../templates')
import document_basic

# Without setting anything
basic_test = document_basic.basic()
basic_test.create_doc()
#basic_test.hello_world()
