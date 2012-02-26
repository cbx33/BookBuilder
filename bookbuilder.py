import xml.etree.ElementTree as ET

xml = ET.parse("schema.xml")

books = xml.findall("book")

series_name = xml.getroot().attrib['name']
print "Series: " + series_name
books_name = []

print "Books:"
for book in books:
	books_name.append(book.attrib['name'])
	print "\t" + books_name[-1]
