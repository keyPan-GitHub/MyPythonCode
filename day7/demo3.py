import os
from os import makedirs

db = "file/users/199"
if not os.path.exists(db):
    os.makedirs(db)

print("操作文件夹下的内容", db)
