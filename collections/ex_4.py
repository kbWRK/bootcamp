p_3=0
p_5=0
l3=[]
l5=[]
for a in range(101):
 if a % 3 == 0:
     p_3 += 1
     l3.append(a)
 elif a % 5 == 0:
     p_5 += 1
     l5.append(a)
print(f"przez 3 :{l3} przez 4 :{l5} ")



