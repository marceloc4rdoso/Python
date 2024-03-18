#from pathlib2 import Path

raw_file = ("I:\\IVALIX\\AA-Holerites\\data\\022024-C.txt")
final_file = ("I:\\IVALIX\\TXT\\mainetti\\dados\\in\\A-MS\\202402-slb.txt")
output = ""
with open(raw_file, encoding="utf8") as file:
    for line in file:
        if not line.isspace():
            output += line
file = open(final_file, 'w')
file.write(output)