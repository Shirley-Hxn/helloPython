name_list = ['a', 'b', 'c']
# print(name_list[0])
# 查找
print(name_list.index('b'))  # 数据的索引值
print(name_list[0])

# 插入数据
name_list.append('d')  # 后方追加数据

name_list2 = ['1', '2', '3']
name_list.extend(name_list2)

# 删除数据
name_list.remove('a')
name_list.pop(1)
# name_list.clear()  #清空


# 升序
# name_list.sort()

# 降序
# name_list.sort(reverse=True)

# 逆序（反转）
name_list.reverse()

# 使用迭代（iteration）遍历列表
# for …… in (列表) :

print(name_list)

