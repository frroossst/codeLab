import json
import git


"""
git_backup.json format
{"name of repo" : "<url>"}
name is just for YOUR reference
"""

def main():

    with open("git_backup.json","r") as fobj:
        content = json.load(fobj)
        fobj.close()

    for i in content.values():
        G = git.cmd.Git(i)
        G.pull()

if __name__ == "__main__":
    if os.path.exists("git_backup.json"):
        main()
    else:
        with open("git_backup.json","w") as fobj:
            json.dump({},fobj)
            fobj.close()
        print("[INITIALISED] Try running the script again")
