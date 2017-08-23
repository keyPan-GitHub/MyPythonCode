

import pickle 


f = open('accounts.db','rb')

# account_db = pickle.loads(f.read())
account_db = pickle.load(f)
print(account_db)
f.close

# load or dump 适用于文件 
# loads or dumps 适用于 字典等等





