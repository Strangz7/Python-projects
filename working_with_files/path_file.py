import pathlib
# path = pathlib.Path("C:/Users/David/Desktop/hello.txt")
# print(path)
# print(path.exists())
# file_path = pathlib.Path.cwd() / "my_folder" / "my_file.txt"
# # print(list(home.parents))
# print(file_path)
# print(file_path.exists())


# new_dir = pathlib.Path.cwd()/"new_directory"
# new_dir.mkdir(exist_ok=True)
#
# if not new_dir.exists():
#      new_dir.mkdir()


# nested_dir = pathlib.Path.cwd() / "folder_a" / "folder_b"
# nested_dir.mkdir(parents=True, exist_ok=True)
# file_path = pathlib.Path.cwd() / "fil1.txt"
# file_path.touch(exist_ok=True)
# path = pathlib.Path("C:/Users/David/Desktop/hello.txt")
# print(path)
home = pathlib.Path.cwd()
# print(home)

# file = open("test.txt", "a")
# file.write("This will add this line")
# file.close()
# with open("file.txt") as file:
#     data = file.read()

path = pathlib.Path.home()/ "hello.txt"
path.touch()
# file = pathlib.Path.open(mode="r", encoding="utf-8")
file = open(path, mode="r", encoding="ascii")
file.close()
print(file)
