import xml.etree.ElementTree as ET
import os, os.path
import shutil

def processpart(part, path, count):
	start_chap = int(part.find("chapters").attrib['start'])
	end_chap = int(part.find("chapters").attrib['end'])

def processbook(book):
	book_name = book.attrib['name']
	book_id = book.attrib['id']
	path = "source/" + book_id
	
	print "\tProcessing: " + book_name
	shutil.rmtree(path + "/tmp")
	os.mkdir(path + "/tmp")
	count = 1
	parts = book.findall("part")
	for part in parts:
		processpart(part, path, count)
		count += 1

xml = ET.parse("schema.xml")

books = xml.findall("book")

formats = xml.find("parameters/formats")

formats_required = []

series_name = xml.getroot().attrib['name']
print "Series: " + series_name
books_name = []

print "Books:"
for book in books:
	books_name.append(book.attrib['name'])
	print "\t" + books_name[-1]

print "Formats:"
for forma in formats:
	formats_required.append(forma.tag)
	print "\t" + formats_required[-1]
	
print "Processing Books:"
for book in books:
	processbook(book)
