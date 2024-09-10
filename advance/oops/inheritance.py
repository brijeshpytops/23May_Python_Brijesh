# single
# class A:
#     def a(self):
#         print("I am from class A")

# class B(A):
#     def b(self):
#         print("I am from class B")

# obj = B()
# # print(dir(obj))
# obj.a()
# obj.b()

# multi-level
# class A:
#     def a(self):
#         print("I am from class A")

# class B(A):
#     def b(self):
#         print("I am from class B")

# class C(B):
#     def c(self):
#         print("I am from class C")

# obj = C()
# # print(dir(obj))
# obj.a()
# obj.b()
# obj.c()

# multiple inheritance
# class A:
#     def a(self):
#         print("I am from class A")

# class B:
#     def b(self):
#         print("I am from class B")

# class C(A,B):
#     def c(self):
#         print("I am from class C")

# obj = C()
# # print(dir(obj))
# obj.a()
# obj.b()
# obj.c()


# method resolution order (MRO)
# hierarchical inheritance
class Shape:
    def shape(self):
        print("I am a shape")

class Shape2d(Shape):
    def shape2d(self):
        print("I am a 2D shape")

class Circle(Shape2d):
    def circle(self):
        print("I am a circle")

class Square(Shape2d):
    def square(self):
        print("I am a square")


class Shape3d(Shape):
    def shape3d(self):
        print("I am a 3D shape")

class Cube(Shape3d):
    def cube(self):
        print("I am a cube")

class Cylinder(Shape3d):
    def cylinder(self):
        print("I am a cylinder")

# obj = Cylinder()
# print(Cylinder.mro())
# print(Cylinder.__mro__)

obj = Circle()

obj.shape()
obj.shape2d()
# obj.shape3d()
obj.circle()
# obj.square()