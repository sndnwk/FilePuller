from colorama import Fore, init
from time import sleep
import shutil
import os
init(autoreset=True)


def showHeader():
    print(f"\n{Fore.CYAN}----------------------------------------")
    print(f"{Fore.WHITE}              FilePuller")
    print(f"{Fore.CYAN}----------------------------------------")
    print(f"{Fore.WHITE}Pull files from subfolders into one folder.")
    print(f"{Fore.WHITE}Enter Q to quit.\n")


def getSourceFolder():
    while True:
        sourceFolder = input(f"{Fore.CYAN}Source Folder: {Fore.WHITE}").strip().strip('"')

        if sourceFolder.lower() == "q":
            return None

        if os.path.exists(sourceFolder) and os.path.isdir(sourceFolder):
            print(f"{Fore.GREEN}Folder Found!\n")
            return os.path.abspath(sourceFolder)
        else:
            print(f"{Fore.RED}Folder not found. Please try again.\n")


def pullFiles(sourceFolder):
    destFolder = sourceFolder
    os.makedirs(destFolder, exist_ok=True)

    pulledFiles = 0
    failedFiles = 0
    renamedFiles = 0

    print(f"{Fore.YELLOW}Pulling Files From: {Fore.WHITE}{sourceFolder}")
    print(f"{Fore.CYAN}----------------------------------------")

    for root, dirs, files in os.walk(sourceFolder):
        if root == destFolder:
            continue

        for file in files:
            sourcePath = os.path.join(root, file)
            destPath = os.path.join(destFolder, file)

            if os.path.exists(destPath):
                destPath = getNewFilename(destFolder, file)
                renamedFiles += 1

            try:
                shutil.move(sourcePath, destPath)
                pulledFiles += 1

                print(f"{Fore.GREEN}[+] {Fore.WHITE}{os.path.basename(destPath)}")
            except Exception as e:
                failedFiles += 1
                print(f"{Fore.RED}[-] {Fore.WHITE}{file} - {str(e)}")

    print(f"{Fore.CYAN}----------------------------------------")
    print(f"{Fore.GREEN}Pulling Complete!\n")
    print(f"{Fore.WHITE}Files Pulled:  {Fore.GREEN}{pulledFiles}")
    print(f"{Fore.WHITE}Files Renamed: {Fore.YELLOW}{renamedFiles}")
    print(f"{Fore.WHITE}Files Failed:  {Fore.RED}{failedFiles}")
    print(f"{Fore.CYAN}----------------------------------------\n")

    sleep(1)

    return


def getNewFilename(destFolder, file):
    name, ext = os.path.splitext(file)
    renameNumber = 1
    newName = f"{name}_r{renameNumber}{ext}"
    newPath = os.path.join(destFolder, newName)

    while os.path.exists(newPath):
        renameNumber += 1
        newName = f"{name}_r{renameNumber}{ext}"
        newPath = os.path.join(destFolder, newName)

    return newPath


if __name__ == "__main__":
    while True:
        showHeader()
        sourceFolder = getSourceFolder()

        if sourceFolder is None:
            print(f"\n{Fore.YELLOW}Exiting FilePuller...")
            break

        pullFiles(sourceFolder)
