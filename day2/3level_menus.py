# Author:Da pan

data = {'广州': {'天河': {'天河体育馆':['oldboy','test'], '金山大厦':['oldboy','test']},
                '越秀': ['越秀公园', '光孝寺'],
                '番禺': ['长隆欢乐世界', '大夫山']},
        '深圳': {'福田': ['莲花山', '赛格'],
                '龙华': ['元山公园', '龙城广场'],
                '南山': ['世界之窗', '欢乐谷']},
        '佛山': {'禅城': ['梁园', '孔庙'],
                '南海': ['千灯湖', '南国桃园'],
                '顺德': ['清晖园', '西山庙']}}
print('欢迎查询城市信息')
print('--------------------------------')
exit_flag = False
while not exit_flag:
    for i in data:
        print(i)

    choice = input("选择进入>>>:")
    if choice in data:
        while not exit_flag:
            for i2 in data[choice]:
                print("\t",i2)
            choice2 = input("选择进入2>>>:")
            if choice2 in data[choice]:
                while not exit_flag:
                    for i3 in data[choice][choice2]:
                        print("\t\t",i3)
                    choice3 = input("选择进入3>>>:")
                    if choice3 in data[choice][choice2]:
                        for i4 in data[choice][choice2][choice3]:
                            print("\t\t",i4)
                        choice4 = input("最后一层，返回请按b>>>:")
                        if choice4 == 'b':
                            pass
                        elif choice4 == 'q':
                            exit_flag = True
                    if choice3 == 'b':
                        break
                    elif choice3 == 'q':
                        exit_flag = True
            if choice2 == 'b':
                break
            elif choice2 == 'q':
                exit_flag = True