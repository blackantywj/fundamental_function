# hasattr()函数通过使用getattr()函数来检查对象是否具有指定的属性或方法。它尝试获取对象的属性或方法，如果成功获取到，则说明对象具有该属性或方法，返回True；否则，返回False。

class MyClass:
    def __init__(self):
        self.my_attribute = "Hello"

my_object = MyClass()

if hasattr(my_object, "my_attribute"):
    print("my_object具有my_attribute属性")
else:
    print("my_object没有my_attribute属性")



class MyClass:
    def my_method(self):
        print("Hello")

my_object = MyClass()

if hasattr(my_object, "my_method"):
    print("my_object具有my_method方法")
else:
    print("my_object没有my_method方法")
