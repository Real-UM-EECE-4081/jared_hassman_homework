import os

fileType = {}
for root, directory, files in os.walk('venv'):
    for file in files:
        split = os.path.splitext(file)
        for extension in split:
            if len(extension) < 1:
                continue
            elif extension[0] == '.':
                if extension not in fileType.keys():
                    fileType.setdefault(extension, 1)
                else:
                    fileType[extension] += 1

print(fileType)