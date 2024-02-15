#checking filetypy
import os
import shutil

def checkFile(file):
    filepaths = file
    for fp in filepaths:
        # Split the extension from the path and normalise it to lowercase.
        ext = os.path.splitext(fp)[-1].lower()
        #ext = Path('my_file.mp3').suffix
        # Now we can simply use == to check for equality, no need for wildcards.
        if ext == ".pdf":
            #print (fp, "is a pdf!")
            moveFile(fp, "pdf")
        elif ext == ".xlsx" | ".csv":
            #print (fp, "is an excel file!")
            moveFile(fp, "sheet")
        elif ext == ".docx" | ".rtf":
            moveFile(fp, "doc")
        elif ext == ".jpeg" | ".png" | ".jpg" | ".gdoc":
            moveFile(fp, "images")
        else:
            print(fp, "is an unknown file format.")
    return ext

def moveFile(file, destination):
    destination = "dataset/" + destination
    try:
        #change to shutil.move to move files
        shutil.move(file, destination)
        print(f"File {file} copied successfully.")
    except IOError as e:
        print(f"Unable to copy file {file}. Error: {e}")
    except:
        print(f"Unexpected error occurred while copying file {file}.")
    return

def test(file):
    checkFile(file)
    return

if __name__=="__main__":
    test()
