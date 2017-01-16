'''
This is a basic document
'''
from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape

class basic:
    def __init__(self, nme='Basic', author='John Doe', title='Awesome Title', date=True, sect_no='1', pdf_generate=False):
        self.nme = nme
        self.author = author
        self.title = title
        self.date = date
        self.sect_no = int(sect_no)
        self.pdf_generate = pdf_generate
        
    def fill_document(self, doc):
        for x in range(0, self.sect_no):
            section_name = 'Section %d' % (x+1)
            with doc.create(Section(section_name)):
                doc.append('Pellentesque dapibus suscipit ligula.  Donec posuere augue in quam.  Etiam vel tortor sodales tellus ultricies commodo.  Suspendisse potenti.  Aenean in sem ac leo mollis blandit.  Donec neque quam, dignissim in, mollis nec, sagittis eu, wisi.  Phasellus lacus.  Etiam laoreet quam sed arcu.  Phasellus at dui in ligula mollis ultricies.  Integer placerat tristique nisl.  Praesent augue.  Fusce commodo.  Vestibulum convallis, lorem a tempus semper, dui dui euismod elit, vitae placerat urna tortor vitae lacus.  Nullam libero mauris, consequat quis, varius et, dictum id, arcu.  Mauris mollis tincidunt felis.  Aliquam feugiat tellus ut neque.  Nulla facilisis, risus a rhoncus fermentum, tellus tellus lacinia purus, et dictum nunc justo sit amet elit.')
                with doc.create(Subsection('A subsection')):
                    doc.append('Lorem ipsum dolor sit amet, consectetuer adipiscing elit.  Donec hendrerit tempor tellus.  Donec pretium posuere tellus.  Proin quam nisl, tincidunt et, mattis eget, convallis nec, purus.  Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.  Nulla posuere.  Donec vitae dolor.  Nullam tristique diam non turpis.  Cras placerat accumsan nulla.  Nullam rutrum.  Nam vestibulum accumsan' )
        return doc

    def create_doc(self):
        doc = Document()
        doc = self.fill_document(doc)
        doc.preamble.append(Command('title', self.title))
        doc.preamble.append(Command('author', self.author))
        doc.preamble.append(NoEscape(r'\maketitle'))
        if self.date:
            doc.preamble.append(Command('date',NoEscape(r'\today')))
        if self.pdf_generate:
            doc.generate_pdf(self.nme, clean_tex=True)
        else:
            doc.generate_tex("output/"+self.nme)


