x = 100


def myfunc():
    x = 200
    print("in myfunc, we have the value {}".format(x))


print("before myfunc, we have the value {}".format(x))
myfunc()

print("after myfunc, we have the value {}".format(x))
