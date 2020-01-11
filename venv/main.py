import PyPDF2

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
  page = template.getPage(i)
  page.mergePage(watermark.getPage(0))
  output.addPage(page)

  with open('watermarked_output.pdf', 'wb') as file:
    output.write(file)




# import PyPDF2
# import sys

# ********************************************** attempt adding watermark
# inputs = sys.argv[1:]
#
# with open('wtr.pdf', 'rb') as file: #rb is reading the binary
#     reader = PyPDF2.PdfFileReader(file)
#     watermark = reader.getPage(0)
#     # watermark = reader.getPage(0)
# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#
#     for pdf in pdf_list:
#         print(pdf)
#         watermark.mergePage(pdf)
#         merger.append(pdf)
#         # watermark.mergePage(pdf)
#     merger.write('super.pdf')
#
# pdf_combiner(inputs)


# *****************************             combines pdfs into 1 file
# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('super.pdf')
#
# pdf_combiner(inputs)





# ********************************                  example to read and write pdf dummy
# with open('dummy.pdf', 'rb') as file: #rb is reading the binary
#     # print(file)
#     #
#     reader = PyPDF2.PdfFileReader(file)
#     # print(reader.numPages)
#     #
#     # print(reader.getPage(0))
#     #
#     page = reader.getPage(0)
#     # print(page.rotate(180)) # does not work since not right method
#     # print(page.rotateCounterClockwise(90))
#     # rotate pdf and save
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('crooked.pdf', 'wb') as new_file:
#         writer.write(new_file)