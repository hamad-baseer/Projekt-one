temps = [221, 235, 340, 321]

actual_temp = [temp/10 for temp in temps]
#actual_temp = []
#for temp in temps:
#    actual_temp.append(temp/10)

print(actual_temp)

temps1 = [221, 235, 340, -9999, 321]

actual_temp1 = [temp1/10 for temp1 in temps1 if temp1 != -9999]
print(actual_temp1)
