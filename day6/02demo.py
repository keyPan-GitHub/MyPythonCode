import os

path = 'D:\\'
text = os.listdir(path=path)

for item in text:
    if item.endswith('.zip') or 'C' in item:
        print(item)
        print(os.name)



