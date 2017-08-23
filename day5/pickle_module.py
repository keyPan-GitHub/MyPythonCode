


import pickle



accounts = {
	1000:{
		'name':"Alex Li",
		'email':'lijie@163.com',
		'passwd':"abc123",
		'balance':15000,
		'phone':13651054608,
		'bank_acc':{
			'ICBC'	: 17465498716576,
			'CBC'	: 74984413876548,
			'ABC'	: 85498761346574, 
		}
	},
	1001:{
		'name':"Caixia Guo",
		'email':'Caixia@163.com',
		'passwd':"abc123",
		'balance':-15000,
		'phone':13651056508,
		'bank_acc':{
			'ICBC'	: 98765413549872,

		}
	}
}



print(pickle.dumps(accounts))

with open('accounts.db','wb') as f:
	f.write(pickle.dumps(accounts))









