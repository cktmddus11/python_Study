path = 'C:\\Programs\\Python\\Python36-32\\python.exe'
#a = path.find('python.exe')
#filename = path[a:]
# print(filename)

#x = path.split('\\')
#filename = x[-1]
#print(filename)

x = path.split('\\')
x.reverse() # 리스트 순서 반대로 
print(x)
print(x[0])

#a = input()
#d = a.strip(',.').split()
#print(d)
#print(d.count('the'))

a = map(int, input().split(';'))
c= list(a)
c.sort(reverse=True)
d = 0
for i in c:
    # '{0:>9,}'.format(c[d])
    print('%9s' % format(c[d], ','),sep='\n')
    d = d+1

