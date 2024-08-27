# from tabula import read_pdf
# from tabulate import tabulate
#
# # reads table from pdf file
# df = read_pdf("abc.pdf", pages="all")  # address of pdf file
# print(tabulate(df))


import camelot

# extract all the tables in the PDF file
abc = camelot.read_pdf("foo.pdf")  # address of file location

# print the first table as Pandas DataFrame
print(abc[0].df)