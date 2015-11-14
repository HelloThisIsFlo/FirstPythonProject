import os
import shutil


def change_path():
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\Shock\Python\firstProject\prank")
    return saved_path


def restore_path(path):
    os.chdir(path)


def reveal_message():
    # Change the path
    saved_path = change_path()

    # Init the variables
    file_list = os.listdir(".")
    file_name_temp = "temp.jpg"
    dir_name_junk = ".\Junk"
    list_files_message = ["colombo.jpg", "dallas.jpg", "gainesville.jpg", file_name_temp, "houston.jpg"]

    # Copy the gainesville.jpg file (needed 2 times)
    shutil.copyfile("gainesville.jpg", file_name_temp)

    # Make the junk dir
    os.makedirs(".\Junk")

    # Move all the unused files to the junk folder
    for file_name in file_list:
        if not list_files_message.__contains__(file_name):
            shutil.move(file_name, dir_name_junk) # Move only the files not needed

    for i in range(4):
        os.rename(list_files_message[i], i + ".jpg")

    # Restore the path
    restore_path(saved_path)

    # HELLO :
    # colombo.jpg
    # dallas.jpg
    # gainesville.jpg x2 (temp.jpg)
    # houston.jpg

    print "Message revealed :D"


def hide_message():
    # Change the path
    saved_path = change_path()

    # Init the variables
    dir_name_junk = ".\Junk"
    file_name_temp = "temp.jpg"
    file_list_to_move = os.listdir(dir_name_junk)
    print(file_list_to_move)

    # Remove the temp file
    for file_name in file_list_to_move:
        print(file_name)
        if file_name.endswith(".jpg"):
            shutil.move(dir_name_junk + "\\" + file_name, file_name)

    # Remove temp files and directory
    os.remove(file_name_temp)
    os.rmdir(dir_name_junk)

    # Restore the path
    restore_path(saved_path)

    # Change

    print "Message hidden !"


# Code to actually run
hide_message()
