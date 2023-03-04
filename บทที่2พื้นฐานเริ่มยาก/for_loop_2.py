def temperature_table():
    for celcius in range(101): # 0 - 100
        f = (celcius * 9 / 5) + 32
        # print(celcius, " = ", f)
        print("{}C = {:.2f}F".format(celcius, f))
# temperature_table()

def multi_table(from_n, to_n):
    #nested loop
    for i in range(from_n, to_n + 1):
        for j in range(1, 13): # nested loop
            print("{} x {} = {}".format(i, j , i * j))
        print("-" * 40)

multi_table(2,3)