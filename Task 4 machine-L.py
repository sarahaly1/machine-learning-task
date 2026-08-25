import numpy as np
n = int(input("How many numbers?  "))
x = []
for i in range(n):
    num = int(input("Enter the no.: "))
    x.append(num)

x_arr = np.array(x)
print(x_arr)
order = int(input("Enter the order:  "))
rows=[]
for num in x_arr:
        powered= []
        for p in range(order + 1):
            val = num ** p      
            powered.append(val)  
        rows.append(powered)
final=np.array(rows)
print(final)