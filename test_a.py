# def func(x):
#     return x + 1
#
#
# def test_answer():
#     assert func(3) == 5
# 加法
def test_sum():
    result = 0
    for i in range(101):
        if i % 2 == 0:
            result = result + i
    print(result)


def test_sum_oushu():
    result = 0
    for i in range(2, 101, 2):
        result = result + i
    print(result)


# 数据类型
def test_type():
    a = 1  # 数值
    b = "abcd"  # 字符串
    c = [1, 2, 3, 4]  # 列表
    d = {"a", "b", 3, 4}  # 元组
    e = {"a": 1, "b": 2}  # 字典

    print(a)
    print(b)
    print(c[0])
    print(c[0:3])
    print(d)
    print(e)
    print("hello python")


# def test_c():
#     count = 0
#     while(count < 5): print("<5")
#     #     count = count + 1
#     # else
#     #     print(">=5")


def test_wenjian():
    f = open("data.txt")
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())
    f.close()


def test_c():
    with open("data.txt") as f:
        while True:
            line = f.readline()
            if line:
                print(line)
                print("hello python")
            else:
                break
