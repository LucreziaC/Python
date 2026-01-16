filenames = ['doc.txt', 'report.txt', 'presentation.txt']
for files in filenames:
    file = open(f"exercises/module_6/files/{files}", "w")
    file.write("Hello")
    file.close()