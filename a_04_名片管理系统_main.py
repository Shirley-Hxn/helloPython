import a_04_名片管理系统_tools


while True:

    # TODO 显示功能菜单
    a_04_名片管理系统_tools.show_menu()

    action_str = input("请选择要执行的操作： ")
    print("您选择的操作是【%s】" % action_str)

    if action_str in ['1', '2', '3']:
        """ 功能：
        1、新建名片
        2、显示全部
        3、查询名片
        0、退出系统
        """
        if action_str == '1':
            a_04_名片管理系统_tools.new_card()

        elif action_str == '2':
            a_04_名片管理系统_tools.show_all()

        elif action_str == '3':
            a_04_名片管理系统_tools.new_card()

        pass  # 占位符；不执行任何操作

    elif action_str == '0':
        print("退出成功，欢迎再次使用【名片管理系统】")
        break
        # pass
    else:
        print("您输入的操作不存在，请重新选择！")
