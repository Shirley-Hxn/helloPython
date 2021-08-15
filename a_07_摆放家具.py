"""需求：
1、房子（House）有 户型、总面积和家具名称列表；
    新房子没有任何的家具
2、家具（HouseItem）有 名字和占地面积， 其中
    席梦思（bed）占地 4 平米；
    衣柜（chest）占地 2 平米；
    餐桌（table）占地 1.5 平米；
3、将以上三件 家具 添加到 房子 中；
4、打印房子是，要求输出：户型、总面积、剩余面积、家具名称列表
"""


class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        pass


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area

    def __str__(self):
        pass

    def add_item(self, item):
        pass
