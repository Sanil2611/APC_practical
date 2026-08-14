tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 50, 60, 70)

common = ()

for num in tuple1:
    if num in tuple2:
        common = common + (num,)

print("Common elements =", common)
