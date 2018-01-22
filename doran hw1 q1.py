x = 17
print('Setting x =', x)

# integer
y1 = x
print('y1 =', y1)
print('y1 is a', type(y1))

# float
y2 = float(x)
print('y2 =', y2)
print('y2 is a', type(y2))

# string
y3 = str(x)
print('y3 =', y3)
print('y3 is a', type(y3))

# boolean, true/false
y4 = bool(x > 3)
print('y4 is a', type(y4))
print('y4 is equal to', y4)

# text
text = 'The value of x is', y1
print(text)
