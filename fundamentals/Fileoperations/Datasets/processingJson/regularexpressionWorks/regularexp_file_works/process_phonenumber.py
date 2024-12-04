from re import fullmatch

f=open("C:\\Users\\HP\\Desktop\\Pythonworks\\fundamentals\\Fileoperations\\Datasets\\processingJson\\regularexpressionWorks\\regularexp_file_works\\phone_numbers.txt")

for line in f:
    phone=line.rstrip("\\n")
    pattern="(91)?[0-9]{10}"
    matcher=fullmatch(pattern,phone)
    if matcher !=None:
        print(phone)
