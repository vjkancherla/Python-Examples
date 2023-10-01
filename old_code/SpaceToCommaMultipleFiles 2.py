import glob

for filename in glob.glob('/Users/vija0326/Downloads/tmp/*.log'):
    with open(filename, 'r+') as f:
        text = f.read()
        f.seek(0)
        f.truncate()
        f.write(text.replace(' ', ','))