import json
import os



def setup():
    with open("settings.json","w") as fobj:
        content = {"source" : "", "output" : ""}
        sourceF = input("enter source file name : ")
        outputF = input("enter output file name : ")
        content["source"] = sourceF
        content["output"] = outputF
        json.dump(content,fobj)



def main():
    with open("settings.json","r") as fobj:
        content = json.load(fobj)

    outputF = content["output"]
    sourceF = content["source"]
    
    os.system(f"gcc -o {outputF} {sourceF}")

    return outputF



def run(file):
    os.system(f"./{file}")



if __name__ == "__main__":
    if os.path.exists("settings.json"):
        f = main()
        run(f)
    else:
        setup()