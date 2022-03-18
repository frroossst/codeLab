"""
Only works for python code as of now, and no formal description is given only the output, input and their datatypes
"""

filePath = input("enter file path : ")

with open(filePath,"r") as fobj:
    content = fobj.readlines()
    fobj.close()

for i in content:
    print(i)




docString = f"<insert function description here> \n INPUT : {inputVar} \n OUTPUT : {outputVar}"
