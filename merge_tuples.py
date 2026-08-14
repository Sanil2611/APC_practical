tuple1 = (10, 20, 30, 40)
tuple2 = (30, 40, 50, 60)
merged = tuple1 + tuple2
result = ()
for num in merged:
    if num not in result:
        result = result + (num,)
print("Merged tuple =", result)
