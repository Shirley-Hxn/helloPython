"""需求：
1、小明体重 75.0 公斤；
2、每跑一次步体重减少 0.5 公斤；
3、每吃一次美食体重增加 1 公斤。
"""


class Person:
    def __init__(self, name, weight):
        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫 %s ，目前的体重是 %.2f 公斤" % (self.name, self.weight)

    def run(self):
        print("%s他去运动啦！" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s他去吃美食啦~ 晚点在减肥！" % self.name)
        self.weight += 1


# 创建对象
XiaoMing = Person('小明', 75.0)
XiaoMing.run()
XiaoMing.eat()

print(XiaoMing)
