color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

x = str(color.index(input()))
y = str(color.index(input()))
z = str(10**color.index(input()))

print(int(x + y + z[1:]))