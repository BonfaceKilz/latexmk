'''
This is a formal letter
'''

from pylatex import Document, UnsafeCommand
from pylatex.base_classes import Environment, CommandBase, Arguments, Command, Options

class letter_env(Environment):
    _latex_name = 'letter'
    
class letter():
    def __init__(self, name='John Doe'):
        self.name = name
        self.doc = Document(documentclass="letter")
        
    def preamble_config(self, doc):
        doc.preamble.append(UnsafeCommand('addtolength', arguments=(r'\voffset', r'-0.5in')))
        doc.preamble.append(UnsafeCommand('addtolength', arguments=(r'\hoffset', r'-0.3in')))
        doc.preamble.append(UnsafeCommand('addtolength', arguments=(r'\textheight', r'2cm')))
        doc.preamble.append(UnsafeCommand('signature', arguments=self.name))
        doc.preamble.append(UnsafeCommand('address', arguments=self.name + r'\\P.O. Box 123 \\ Nairobi, Kenya \\ 0707 123 456'))

    def fill_doc(self, doc):
        lorem_text = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit.  Donec hendrerit tempor tellus.  Donec pretium posuere tellus.  Proin quam nisl, tincidunt et, mattis eget, convallis nec, purus.  Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.  Nulla posuere.  Donec vitae dolor.  Nullam tristique diam non turpis.  Cras placerat accumsan nulla.  Nullam rutrum.  Nam vestibulum accumsan nisl.'
        with doc.create(letter_env(arguments=Arguments('Director \nCorporation \nP.O. Box 1234 \nNairobi, Kenya'))) as letter:
            letter.append(UnsafeCommand('opening', arguments=r'\textbf{Dear Sir or Madam,}'))
            letter.append('')
            letter.append(lorem_text)
            letter.append('\n\n')
            letter.append(lorem_text)
            letter.append('\n\nThank you for your time and consideration')
            letter.append('\n\nI look forward to your reply.')
            doc.preamble.append(UnsafeCommand('addtolength', arguments=(r'\voffset', r'-0.5in')))
            doc.append(UnsafeCommand('vspace', arguments=r'2\parskip'))
            doc.append(UnsafeCommand('closing', arguments='Sincerely,'))
            
    def gen_doc(self):
        doc = Document(documentclass='letter')
        self.preamble_config(doc)
        self.fill_doc(doc)
        doc.generate_tex("letter")
        doc.generate_pdf("letter", clean_tex=False)
        print("successful!")
