import os

entries = os.listdir('./example')
file_path = os.path.abspath('./example')

# Removes the files from directory and moves to one folder up
# for index, name in enumerate(entries):
#     current_name = name
#     new_name = f"File_nr_{index}"
#     if name.path.endswith('.txt'):
#         os.rename(current_name, new_name)

# Fixed version, renames the files in place
for index, name in enumerate(entries):
    current_name = name
    _, ext = os.path.splitext(name)
    if name.endswith('.txt'):
        os.rename(os.path.join(file_path, name), os.path.join(file_path, str(index) + ext))