temperatures = (30, 32, 29, 35, 31, 33, 28)

maximum = temperatures[0]
minimum = temperatures[0]

for temp in temperatures:
    if temp > maximum:
        maximum = temp

    if temp < minimum:
        minimum = temp

average = sum(temperatures) / len(temperatures)

print("Maximum Temperature =", maximum)
print("Minimum Temperature =", minimum)
print("Average Temperature =", average)
