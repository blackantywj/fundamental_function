from functools import partial

# 　partial函数的作用就是：将所作用的函数作为 partial() 函数的第一个参数，
#   原函数的各个参数依次作为 partial() 函数的后续参数，原函数有关键字参数的一定要带上关键字，没有的话，按原有参数顺序进行补充。

def my_sum(a, b):
    print("a = ", a)
    print("b = ", b)
    return a + b

# 偏函数的第一个参数是 作用函数(my_sum)
# 偏函数的第二个参数是 传给作用函数的第一个参数(a)
# 偏函数的第三个参数是 传给作用函数的第三个参数(b)

new_my_sum = partial(my_sum, 10)
res = new_my_sum(20)

print("res=", res)


from functools import partial


def my_sum(a, b):
    print("a=", a)
    print("b=", b)
    return a + b


# 偏函数的第一个参数是 作用函数(my_sum)
# 偏函数的第二个参数是 传给作用函数的第一个参数(a)
# 偏函数的第三个参数是 传给作用函数的第三个参数(b)
new_my_sum = partial(my_sum, 10, 20)        # 相当于: new_my_sum = my_sum(10, b)   位置传参轮到a了, a=10; 轮到b了, b=20
res = new_my_sum()                    # 相当于: res = my_sum(10, 20)

print("res=", res)

# 结果:
# a= 10
# b= 20
# res= 30


from functools import partial


def my_sum(a, b):
    print("a=", a)
    print("b=", b)
    return a + b


# 偏函数的第一个参数是 作用函数(my_sum)
# 偏函数的第二个参数是 传给作用函数的第一个参数(a)
# 偏函数的第三个参数是 传给作用函数的第三个参数(b)

# 注意: 这里的关键字传参,传给的是后边的b,前边的a未指定关键字,没有报错,正常,因为按照形参a和b的位置来看,关键字参数要在位置参数之后
new_my_sum = partial(my_sum, b=10)        # 相当于: new_my_sum = my_sum(a, 10)   关键字传参,传给了b, b=10
res = new_my_sum(20)                      # 相当于: res = my_sum(20, 10)         b有了实参,剩下a,所以传给了a, a=20

print("res=", res)

# 结果:
# a= 20
# b= 10
# res= 30

from functools import partial


def my_sum(a, b):
    print("a=", a)
    print("b=", b)
    return a + b


# 偏函数的第一个参数是 作用函数(my_sum)
# 偏函数的第二个参数是 传给作用函数的第一个参数(a)
# 偏函数的第三个参数是 传给作用函数的第三个参数(b)

# 注意: 这里的关键字传参,传给的是前边的a,后边的b未指定关键字,就会报错,因为按照形参a和b的位置来看,关键字参数要在位置参数之后,也就是说,a指定了,b也必须指定就可以了
new_my_sum = partial(my_sum, a=10)        # 相当于: new_my_sum = my_sum(10, b)   关键字传参,传给了a, a=10
res = new_my_sum(20)                      # 相当于: res = my_sum(10, 20)         a有了实参,剩下b,所以想要传给b, b=20,但是违反了关键字参数在位置参数之后原则,所以报错

print("res=", res)

# 结果:
# TypeError: my_sum() got multiple values for argument 'a'