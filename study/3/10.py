x = input().split()

#del(x[len(x):len(x)-6:-1]) # 12 : 12-6:-1 -> 6(5)
#del(x[len(x)]-5:)
del(x[-5:len(x)])
print(tuple(x))


