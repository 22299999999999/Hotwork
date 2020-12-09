class Person:
    name = "default"
    age = 0
    gender = "male"
    weight = 0

    def eat(self):
        print("eating")

    def jump(self):
        print("jumpping")


# 实例化类
zs = Person()
print(Person.name)
print(zs.name)

# print(f"zs的名字为：",{zs.name})
# print("zs的名字为：",zs.name)
