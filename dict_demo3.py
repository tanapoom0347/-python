def demo():
    m = { 
        ("th", 2016): {"g": 5, "s": 3, "b": 7}, 
        ("th", 2015): {"g": 15, "s": 13, "b": 17}, 
        ("sg", 2016): {"g": 3, "s": 1, "b": 2},
        ("sg", 2015): {"g": 23, "s": 21, "b": 22},
        ("jp", 2016): {"g": 13, "s": 10, "b": 25},
        ("jp", 2015): {"g": 93, "s": 90, "b": 95}
    }

    print(m)
    print(m["th", 2015])
    print(m["th", 2015]["g"])
    m["th", 2015]["g"] = "99"
    print(m["th", 2015])
    m["th", 2015] = {"g": 75, "s": 73, "b": 77}
    print(m["th", 2015])
    del m[("jp", 2016)]
    print(m)
    if ("th", 2017) in m:
        print("found")
    else:
        print("not found")
    m[("my", 2016)] = {"g": 3, "s": 7, "b": 2}
    print(m)

demo()