def testMe(**kwargs):
    print(type(kwargs))

    for item in kwargs:
        print(item, "=", kwargs[item])


kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
testMe(**kwargs)
