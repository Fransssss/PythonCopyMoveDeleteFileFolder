# copy move and delete file and folder
# author: Fransiskus Agapa
import shutil
import os

print("\n== File Menu ==")
print("1. Copy file")
print("2. Move file to directory")
print("3. Delete file / folder")
print("E. Exit")
choice = input("choice: ")

while choice != 'e' and choice != 'E':
    if choice == '1':
        print("\n[ Copy file ]")
        place = input("a. Directory\nb. Project folder\n ")
        if place == 'a' or place == 'A':
            print("\n> Directory")
            change_file_name = input("would you like to rename file (y/n): ")
            if change_file_name == 'y' or change_file_name == 'Y':
                new_name = input("\ninput new name: ")
                new_name += ".txt"
                shutil.copyfile("firstjoke.txt", r"C:\Users\XaveF\Documents" + '\\' + new_name)           # copy file fo directory
                print("\n[ File has been copied to directory ]")
            elif change_file_name == 'n' or change_file_name == 'N':
                shutil.copyfile("firstjoke.txt", r"C:\Users\XaveF\Documents\CopiedFirstJoke.txt")
                print("\n[ File has been copied to directory ]")
            else:
                print("\n[ Invalid input ]")
        elif place == 'b' or place == 'B':
            print("\n> Project folder")
            change_file_name = input("would you like to rename file (y/n): ")
            if change_file_name == 'y' or change_file_name == 'Y':
                new_name = input("\ninput new name: ")
                new_name += ".txt"
                shutil.copyfile("firstjoke.txt", new_name)
                print("\n[ File has been copied into project folder ]")
            elif change_file_name == 'n' or change_file_name == 'N':
                shutil.copyfile("firstjoke.txt", "CopiedFirstJoke.txt")
                print("\n[ File has been copied into project folder ]")
            else:
                print("\n[ Invalid input ]")
        else:
            print("\n[ Invalid input ]")
    elif choice == '2':
        print("\n[ Move file to directory ]")
        path = r"C:\Users\XaveF\Documents"
        change_file_name = input("would you like to rename file (y/n): ")
        if change_file_name == 'y' or change_file_name == 'Y':
            new_name = input("\ninput new name: ")
            new_name += ".txt"
            try:
                path += '\\' + new_name
                if os.path.exists(path):                         # check if file exist in directory
                    print("\n[ File is already exist ]")
                else:
                    os.replace("firstjoke.txt", path)
                    print("\n[ File has been moved to directory ]")
            except FileNotFoundError:
                print("\n[ File is not found ]")
        elif change_file_name == 'n' or change_file_name == 'N':
            try:
                path += "\\" + "MovedFirstJoke.txt"
                if os.path.exists(path):
                    print("\n[ File is already exist ]")
                else:
                    os.replace("firstjoke.txt", path)               # firstjoke.txt will be moved to directory and gone from project folder
                    print("\n[ File has been moved to directory ]")
            except FileNotFoundError:
                print("\n[ File is not found ]")
        else:
            print("\n[ Invalid input ]")
    elif choice == '3':
        print("\n[ Delete file / folder ]")
        print("a. File")
        print("b. Empty folder")
        print("c. Folder")
        path = ""
        to_delete = input()
        if to_delete == 'a':
            try:
                path = "twojoke.txt"
                os.remove(path)
                print("[ File has been deleted ]")
            except FileNotFoundError:
                print("[ File is not found ]")
        elif to_delete == 'b':
            try:
                path = "emptyfolder"
                os.rmdir(path)
                print("[ File is not found ]")
            except FileNotFoundError:
                print("[ File is not found ]")
        elif to_delete == 'c':
            try:
                path = "Jokeinside"
                shutil.rmtree(path)
                print("[ File has been deleted ]")
            except FileNotFoundError:
                print("[ File is not found ]")
        else:
            print("[ Invalid input ]")
    else:
        print("\n[ Invalid input ]")

    print("\n== File Menu ==")
    print("1. Copy file")
    print("2. Move file to directory")
    print("3. Delete file / folder")
    print("E. Exit")
    choice = input("choice: ")

if choice == 'e' or choice == 'E':
    print("\n== Exit Program ==")