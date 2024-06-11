# double = lambda x: x * 2
# cube = lambda x: x*x*x
# avg = lambda x,y: (x+y)/2
# print(double(5))
# print(cube(3))
# print(avg(3, 5))

def apply(fx, value):
    return 5 + fx(value)

print(apply(lambda x: x * x * x, 2))