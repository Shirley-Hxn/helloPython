# 记录所有的名片字典
card_list = []

def show_menu():
    """显示功能菜单"""
    print('*' * 50)
    print('欢迎使用【名片管理系统】V 1.0')
    print("")
    print("1、新建名片")
    print("2、显示全部")
    print("3、查询名片")
    print("")
    print("0、退出系统")
    print('*' * 50)


def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")

    # 1、提示输入名片详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入邮箱：")

    # 2、根据输入信息建立一个名片字典
    card_dict = {
        "name": name_str,
        "phone_str": phone_str,
        "qq_str": qq_str,
        "email_str": email_str
    }

    # 3、将名片字典添加到列表中
    card_list.append(card_dict)
    print(card_list)

    # 4、提示用户添加成功
    print("添加 %s 的名片成功！" % name_str)


def show_all():
    """显示全部"""
    print("-" * 50)
    print("显示全部")

    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")
    print("")

    # 打印分割线
    print("=" * 50)

    # 遍历名片列表依次输出字典信息
    for card_dirt in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (
            card_dirt["name_str"],
            card_dirt["phone_str"],
            card_dirt["qq_str"],
            card_dirt["email_str"],
        ))




def search_card():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")
