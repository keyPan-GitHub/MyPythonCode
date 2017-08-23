

import pickle
acc_file_name = 'accounts.db'

account_file = open(acc_file_name,'rb')

account_dict = pickle.loads(account_file.read())

account_file.close()
account_dict[1000]['balance'] -= 500


f = open(acc_file_name,'wb')
# f.write(pickle.dumps(account_dict))
pickle.dump(account_dict, f)
f.close()

print(account_dict)







