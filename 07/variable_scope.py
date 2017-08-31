
x = 1

def get():
    global x
    x = 10
    print("x = ", x)

def get2():
    print("x = ", x)

get()
get2()
