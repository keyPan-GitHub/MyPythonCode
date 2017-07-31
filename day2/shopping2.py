# Author:Da pan


product_list = [
    ("iphone",5888),
    ("Mac Pro",10888),
    ("xiaomi",2888),
    ("watch",5888),
    ("bike",58),
    ("coffee",28),
    ("tea",88),
]

shopping_list = []

salary = input("input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index, item in enumerate(product_list):
            print(index,item)
        user_choice = input("选择要买什么>>>:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice > 0:
                p_item = product_list(user_choice)
                if p_item[1] <= salary :
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added (%s) into shopping cart ,your current balance is %s " % (p_item, salary))
                else:
                    print("\033[41;1m你的余额只剩[%s]啦，还买个毛线啊\033[0m" % salary)
            else:
                print("product code [%s] is not exist!" % user_choice)
        elif user_choice == "q":
            print("--------------shopping list-----------------------")
            for p in shopping_list:
                print(p)
            print("Your current balance is", salary)
            exit()
        else:
            print("invalid option")

