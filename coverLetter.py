from docx import Document
import sys

coverLetter = Document("/Users/shrav/Downloads/Cover Letters/Cover Letter Template.docx")
sections = coverLetter.sections

name = 'ShravanHariharan'
docType = 'CoverLetter.docx'
company = sys.argv[1]
desc = sys.argv[2]
#being one of the % out there

for paragraph in coverLetter.paragraphs:
	if '_' in paragraph.text:
		inline = paragraph.runs	
		for i in range(len(inline)):
			if '_' in inline[i].text:
				text = inline[i].text.replace('_', company)
				inline[i].text = text
	if '%' in paragraph.text:
		inline = paragraph.runs	
		for i in range(len(inline)):
			if '%' in inline[i].text:
				text = inline[i].text.replace('%', desc)
				inline[i].text = text

filename = name + '_' + company + '_' + docType
filepath = "/Users/shrav/Downloads/Cover Letters/"
coverLetter.save(filepath + filename)