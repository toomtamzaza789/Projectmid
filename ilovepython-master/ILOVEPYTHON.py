import os
keroro = list()
def stddata1():
    fdata = open('term1.txt','r')
    data = fdata.read()
    print('{0:-<150}'.format(""))
    print("                      ❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤[ Student List ]❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤                                                 ")
    print('{0:-<150}'.format(""))
    print("No.     \tName \t\t\tClass\t\tNumber\t\tGrade\t\tParent's Tel.")
    print('{0:-<150}'.format(""))
    print(data)
    fdata.close()
    print("A) กลับหน้าหลัก")
    j=input(" ")
    if j == "a": menu()
def menu():
    b = input('********** ประวัติผลการศึกษา ********** \n ครูผู้สอน [t] \n นักเรียน(ดูผลการเรียน) [s] \n ************* \n หมายเหตุ \n ************* \n นักเรียนสามารถเข้าดูผลการเรียนได้เพียงเท่านั้น \n')
    b = b.lower()
    if b == 't': 
        def login():
            loop = 'true'
            while(loop == 'true'):	#ใช้ while เพื่อ ลูปหา username password ในระบบ
                username = input("Enter User: ")
                password = input("Enter Pass: ")
                if(username == "tec1" and password == "1234"):
                    print('ล็อกอินสำเร็จ' + username)
                    loop = 'false'              #เมื่อลูปเจอ username password ในระบบแล้ว จะเปลี่ยนตัวแปล loop = 'false' เพื่อ ออกจากลูป
                    #loop1 = 'true'
                    print("*** ประวัติผลการศึกษา ***")
                    print("o) ดูผลการศึกษา")
                    print("p) กรอกผลการศึกษา")
                    print("e) เพิ่มผลการศึกษานักเรียนใหม่")
                    print("n) กรอกเบอร์ครูผู้สอน")
                    l=input("เลือกเมนูที่ต้องการ: ")
                    if l == 'o':
                        print("o) ดูผลการศึกษาเทอมที่1")
                        print("p) ดูผลการศึกษาเทอมที่2")
                        g=input('เลือกเมนูที่ต้องการ')
                        if g == 'o':#เทอมที่1
                            def stddata1():
                                fdata = open('term1.txt','r')
                                data = fdata.read()
                                print('{0:-<150}'.format(""))
                                print("                      ❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤[ Student List ]❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤                                                 ")
                                print('{0:-<150}'.format(""))
                                print("\tNo.   \tName\t\t\tClass\t\tNumber\t\tGrade\t\tParent's Tel.")
                                print('{0:-<150}'.format(""))
                                print(data)
                                fdata.close()
                                print("A) กลับหน้าหลัก")
                                j=input(" ")
                                if j == "a": menu()
                            stddata1()
                        elif g =='p': #เทอมที่2
                            def stddata2():
                                fdata = open('term2.txt','r')
                                data = fdata.read()
                                print('{0:-<150}'.format(""))
                                print("                      ❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤[ Student List ]❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤                                                 ")
                                print('{0:-<150}'.format(""))
                                print("\tNo.   \tName     \t\t\t\tClass\t\tNumber\t\tGrade\t\tParent's Tel.")
                                print('{0:-<150}'.format(""))
                                print(data)
                                fdata.close()
                                print("A) กลับหน้าหลัก")
                                j=input(" ")
                                if j == "a": menu()
                            stddata2()
                        else : print("\n!!!ไม่พบเมนูที่ต้องการ!!!\n"),login()
                    elif l == 'p':
                        print("o) กรอกผลการศึกษาเทอมที่1")
                        print("p) กรอกผลการศึกษาเทอมที่2")
                        g=input('เลือกเมนูที่ต้องการ')
                        if g == 'o':#กรอกข้อมูลเทอมที่1
                            def kai():
                                fo = open("term1.txt","w")
                                x=k=0
                                k = int(input('\nกรุณาใส่จำนวนข้อมูลที่จะกรอก(คน)\n'))
                                while x < k :
                                    x+=1
                                    x=str(x)
                                    print("No %a"%(x))
                                    name = str(input("Name & Sur name : "))
                                    name.split()
                                    classs = str(input("Class : "))
                                    number = input("Number : ")
                                    grade = str(input("Grade : "))
                                    phone = input("Parent's Tel : ")
                                    fo.write('%s %20s %20s %20s %20s %20s\n'%(x,name,classs,number,grade,phone))
                                    #fo.write("["+x+"] "+name+" \t\t\t\t"+classs+"\t\t\t"+number+"\t\t\t"+grade+"\t\t\t"+phone+"\n")
                                    x=int(x)  
                                fo.close()
                                menu()
                            kai()
                        elif g == 'p':#กรอกข้อมูลเทอมที่2
                            def kai():
                                fo = open("term2.txt","w")
                                x=k=0
                                k = int(input('\nกรุณาใส่จำนวนข้อมูลที่จะกรอก(คน)\n'))
                                while x < k :
                                    x+=1
                                    x=str(x)
                                    print("No %a"%(x))
                                    name = str(input("Name & Sur name : "))
                                    name.split()
                                    classs = str(input("Class : "))
                                    number = input("Number : ")
                                    grade = str(input("Grade : "))
                                    phone = input("Parent's Tel : ")
                                    fo.write('%s %20s %20s %20s %20s %20s\n'%(x,name,classs,number,grade,phone))
                                    #fo.write("["+x+"] "+name+" \t\t\t\t"+classs+"\t\t\t"+number+"\t\t\t"+grade+"\t\t\t"+phone+"\n")
                                    x=int(x)  
                                fo.close()
                                menu()
                            kai()
                        else : print("\n!!!ไม่พบเมนูที่ต้องการ!!!\n"),login()
                    elif l == 'e':
                        print("o) เพิ่มผลการเรียนนักเรียนใหม่เทอมที่ 1")
                        print("p) เพิ่มผลการเรียนนักเรียนใหม่เทอมที่ 2")
                        g=input("เลือกเมนูที่ต้องการ")
                        if g == 'o':#เพิ่มผลการเรียนเทอมที่ 1
                            def kai():
                                fo = open("term1","a")
                                x=k=0
                                k = int(input('\nกรุณาใส่จำนวนข้อมูลที่จะกรอก(คน)\n'))
                                while x < k :
                                    x+=1
                                    x=str(x)
                                    print("No %a"%(x))
                                    name = str(input("Name & Sur name : "))
                                    name.split()
                                    classs = str(input("Class : "))
                                    number = input("Number : ")
                                    grade = str(input("Grade : "))
                                    phone = input("Parent's Tel : ")
                                    fo.write('%s %20s %20s %20s %20s %20s\n'%(x,name,classs,number,grade,phone))
                                    #fo.write("["+x+"] "+name+" \t\t\t\t"+classs+"\t\t\t"+number+"\t\t\t"+grade+"\t\t\t"+phone+"\n")
                                    x=int(x) 
                                fo.close()
                                menu()
                            kai()
                        elif g == 'p':#เพิ่มผลการเรียนเทอมที่ 2
                            def kai():
                                fo = open("term2","a")
                                x=k=0
                                k = int(input('\nกรุณาใส่จำนวนข้อมูลที่จะกรอก(คน)\n'))
                                while x < k :
                                    x+=1
                                    x=str(x)
                                    print("No %a"%(x))
                                    name = str(input("Name & Sur name : "))
                                    name.split()
                                    classs = str(input("Class : "))
                                    number = input("Number : ")
                                    grade = str(input("Grade : "))
                                    phone = input("Parent's Tel : ")
                                    fo.write('%s %20s %20s %20s %20s %20s\n'%(x,name,classs,number,grade,phone))
                                    #fo.write("["+x+"] "+name+" \t\t\t\t"+classs+"\t\t\t"+number+"\t\t\t"+grade+"\t\t\t"+phone+"\n")
                                    x=int(x) 
                                fo.close()
                                menu()
                            kai()
                        else : print("\n!!!ไม่พบเมนูที่ต้องการ!!!\n"),login()
                    elif l == 'n':
                        def kai():
                            fo = open("tectel.txt","w")
                            x=k=0
                            k = int(input('\nกรุณาใส่จำนวนข้อมูลที่จะกรอก(คน)\n'))
                            while x < k :
                                x+=1
                                x=str(x)
                                print("No %a"%(x))
                                name = str(input("Name & Sur name : "))
                                name.split()
                                classs = str(input("Class : "))
                                number = input("Number : ")
                                grade = str(input("Grade : "))
                                phone = input("Parent's Tel : ")
                                fo.write('%s %20s %20s %20s %20s %20s\n'%(x,name,classs,number,grade,phone))
                                #fo.write("["+x+"] "+name+" \t\t\t\t"+classs+"\t\t\t"+number+"\t\t\t"+grade+"\t\t\t"+phone+"\n")
                                x=int(x)  
                            fo.close()
                            menu()
                        kai()
                    else : print("\n!!!ไม่พบเมนูที่ต้องการ!!!\n"),login()
                else : print('รหัสผ่านผิด'), login()
        login()
    elif b == 's':
        def login():
            loop = 'true'
            while(loop == 'true'):	#ใช้ while เพื่อ ลูปหา username password ในระบบ
                username = input("Enter User: ")
                password = input("Enter Pass: ")
                if(username == "std1" and password == "1357"):
                    print('ล็อกอินสำเร็จ' + username)
                    loop = 'false'              #เมื่อลูปเจอ username password ในระบบแล้ว จะเปลี่ยนตัวแปล loop = 'false' เพื่อ ออกจากลูป
                    #loop1 = 'true'
                    print("*** ประวัติผลการศึกษา ***")
                    print("o) ดูผลการศึกษาภาคเรียนที่ 1")
                    print("p) ดูผลการศึกษาภาคเรียนที่ 2")
                    l=input('เลือกเมนูที่ต้องการ: ')
                    if l == 'o':
                        def stddata():
                            fdata = open('term1.txt','r')
                            data = fdata.read()
                            print('{0:-<150}'.format(""))
                            print("                      ❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤[ Student List ]❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤                                                 ")
                            print('{0:-<150}'.format(""))
                            print("\tNo.     \tName \t\t\tClass\t\tNumber\t\tGrade\t\tParent's Tel.")
                            print('{0:-<150}'.format(""))
                            print(data)
                            fdata.close()
                            print("A) กลับหน้าหลัก")
                            j=input(" ")
                            if j == "a": menu()
                        stddata()
                    elif l == 'p':
                        def stddata():
                            fdata = open('term2.txt','r')
                            data = fdata.read()
                            print('{0:-<150}'.format(""))
                            print("                      ❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤[ Student List ]❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤                                                 ")
                            print('{0:-<150}'.format(""))
                            print("\tNo.     \tName \t\t\tClass\t\tNumber\t\tGrade\t\tParent's Tel.")
                            print('{0:-<150}'.format(""))
                            print(data)
                            fdata.close()
                            print("A) กลับหน้าหลัก")
                            j=input(" ")
                            if j == "a": menu()
                        stddata()
                    else : print("\n!!!ไม่พบเมนูที่ต้องการ!!!\n"),menu()
                else : print('รหัสผ่านผิด'), login()
        login()
    else : print("\n!!!ไม่พบเมนูที่ต้องการ!!!\n"),menu()
menu()