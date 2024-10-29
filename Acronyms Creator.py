def acronyms_creator():
    input_string = input("Enter the string which needs to be acronymized: ")
    words = input_string.split()
    acronym =  ''
    for word in words:
        acronym += word[0].upper()
    print(acronym)

acronyms_creator()
