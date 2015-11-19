# __author__ = 'USER'
import os
import shutil
import sys

source_folder = "D:\document\course_content\Switching_Circuit_and_Logic_Design"
target_folder = "C:\Users\USER\Dropbox\Lecture_Notes\Switching_Circuit_and_Logic_Design"


def syncdir(source_folder, target_folder):

    if(not os.path.exists(target_folder)):
        os.mkdir(target_folder)

    for file in os.listdir(source_folder):

        from_file = os.path.join(source_folder, file)
        to_file = os.path.join(target_folder, file)

        if(os.path.isdir(from_file)):
            syncdir(from_file, to_file)
        else:
            if(iscopy(from_file, to_file)):
                shutil.copy2(from_file, target_folder)
#                print("copy " + file + " from " + from_file + " to " + to_file + ";")
#                print("copy", file, "from", from_file, "to" , to_file , ";")
                print("copy %s from %s to %s;" % (file , from_file , to_file))
            else:
                print("The file %s is exist" % to_file)


def iscopy(from_file, to_file):

    if(not os.path.exists(to_file)):
        return True

    from_file_modify_time = round(os.stat(from_file).st_mtime, 1)
    to_file_modify_time = round(os.stat(to_file).st_mtime, 1)
    if(from_file_modify_time > to_file_modify_time):
        return True

    return False


if __name__ == '__main__':
#    if(not os.path.exists(source_folder) or not os.path.isdir(source_folder)):
    if(not os.path.isdir(source_folder)):
        print("The source folder:%s is not exist" % source_folder)
        sys.exit()
    syncdir(source_folder, target_folder)
    print("All files has been sync")