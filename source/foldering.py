#sort the clusters into different folders
#so how do we do this
import os 
import shutil

#test values this variables only called in test()
fileName=["dataset/Accountant Resume.pdf","dataset/Assitant Manager Resume.pdf","dataset/Audit Memo.pdf","dataset/Branch Manager Resume.pdf","dataset/Civil Engineer Resume.pdf","dataset/Delivery Driver.pdf","dataset/InterOffice Memo for pc upgrade.pdf","dataset/InterOffice Memo Hygiene.pdf","dataset/Policy Update.pdf","dataset/Team Building Event.pdf"]
labels = [0, 0, 1, 0, 0, 0, 1, 1, 1, 1]

def createFolders(folderName):
    try:
        folder_name = folderName  # Replace with your desired name
        path = os.path.join("output", "cluster " + folder_name)  # Specify complete path

        # Create the folder, handling potential errors gracefully
        os.makedirs(path, exist_ok=True)  # Creates intermediate directories if needed
        print(f"Successfully created folder: {path}")

    except OSError as e:
        print(f"Error creating folder: {e}")
    return

#copying documents from clusters to newly created folders based on cluster group
def copyFiles(file, destination):
    try:
        #change to shutil.move to move files
        shutil.copy(file, destination)
        #print(f"File {file} copied successfully.")
    except IOError as e:
        print(f"Unable to copy file {file}. Error: {e}")
    except:
        print(f"Unexpected error occurred while copying file {file}.")
    return

def fileClusterDisplay(files, kmeansLabels):
    #okay so how do we start
    combined = list(zip(files,kmeansLabels))
    print(combined)
    return combined

#main function to be called from other function
def foldering(files, kmeansLabels):
    uniqeCluster=list(set(kmeansLabels))
    fileCluster = fileClusterDisplay(files, kmeansLabels)
    print(uniqeCluster)
    #create folders
    for i in uniqeCluster:
        createFolders(str(i))

    #move files
    print("Copying files")
    for files in fileCluster:
        source, cluster = files
        copyFiles(source, "output/cluster " + str(cluster))
    print("Files Copied")
    return

#test function
def test():
    uniqeCluster=list(set(labels))
    fileCluster = fileClusterDisplay(fileName, labels)
    print(uniqeCluster)
    #create folders
    for i in uniqeCluster:
        createFolders(str(i))

    #move files
    for files in fileCluster:
        source, cluster = files
        copyFiles(source, "output/cluster " + str(cluster))
    
    return

#this is to do in file test, to refer to the main function to be called, see foldering()
if __name__ == "__main__":
    test()