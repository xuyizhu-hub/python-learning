def add_contact():
    name=input("请输入姓名:")
    phone=input("请输入手机号:")
    email=input("请输入邮箱:")
    contact={
        "name":name,
        "phone":phone,
        "email":email
    }
    contacts.append(contact)
    print("添加联系人成功")

def del_contact():
        name=input("请输入姓名:")
        for index,contact in enumerate(contacts):
            if contact["name"]==name:
                del contacts[index]
                print("删除联系人成功!")
                return
        print("未找到要删除的联系人")
            
         
    
def update_contact():
        name=input("请输入要修改的姓名")
        for contect in contacts:
            if contect["name"]==name:
                new_name=input("请输入新姓名:")
                new_phone=input("请输入新手机号:")
                new_email=input("请输入新邮箱:")
                contect["name"]=new_name
                contect["phone"]=new_phone
                contect["email"]=new_email

                print("修改成功")
                return
            
        print("该联系人不存在")

    

def search_contact():
        name=input("请输入要查询的姓名:")
        for contect in contacts:
            if contect["name"]==name:
                print("姓名:",contect["name"])
                print("手机号:",contect["phone"])
                print("邮箱:",contect["email"])
                return
        
        print("该联系人不存在")

def show_contact():
    if len(contacts)==0:
        print("当前通讯录为空")
    else:
        for contect in contacts:
                print("姓名:",contect["name"])
                print("手机号:",contect["phone"])
                print("邮箱:",contect["email"])
       

contacts = []
while True:
    print(
            """
        1. 添加联系人
        2. 删除联系人
        3. 修改联系人
        4. 查询联系人
        5. 显示所有联系人
        6. 退出系统
        """
        )
    try:
        choice = int(input("请输入你要使用的操作:"))
    except:
        print("输入错误，请输入数字")
        continue
    match choice:
        case 1:
            add_contact()
            continue
        case 2:
            del_contact()
            continue
        case 3:
            update_contact()
            continue
        case 4:
            search_contact()
            continue
        case 5:
            show_contact()
            continue
        case 6:
            print("退出系统成功")
            break 
        case _:
              print("非法操作,请重新输入:")


