import os

entries = os.listdir('./example')
file_path = os.path.abspath('./example')

# for index, name in enumerate(entries):
#     current_name = name
#     new_name = f"File_nr_{index}"
#     if name.path.endswith('.txt'):
#         os.rename(current_name, new_name)
print(file_path)
for index, name in enumerate(entries):
    current_name = name
    _, ext = os.path.splitext(name)
    if name.endswith('.txt'):
        os.rename(os.path.join(file_path, name), os.path.join(file_path, str(index) + ext))
    # new_name = f"File_nr_{index}"
    # if name.path.endswith('.txt'):
    #     print(os.chdir('./example'))
