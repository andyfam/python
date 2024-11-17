import os
import shutil

path = "test.txt"
empty_directory = "empty"
directory = "test"

try:
    os.remove(path)
    os.rmdir(empty_directory)
    shutil.rmtree(directory)
except FileNotFoundError as e:
    print("That file was not found!")
except PermissionError as e:
    print("You don't have permission to do that!")
except OSError as e:
    print("You can't delete that using that function!")
else:
    print("file/directory was deleted successfully!")