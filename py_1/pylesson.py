
a = 10
b = 20
print("AAAAAAAAAAA=", a + b)
a = 'Hello'

b = ' World'
print(id(a))
print(type(a))

BigData = a + b
print(BigData)

print(a, b, BigData , sep=' | ', end=' END\n\n')
print(abs(-15))

print(a, b, BigData , sep=' | ', end=' END\n\n')

x = 5
y = 2.5
print("x =", x, "y =", y)

print(f"Integer: {x}!!!!!!!!! Float: {y}")

input_data = input("Enter your data: ")
print( input_data, type(input_data) )

test_int = int( input("Enter an integer: ") )
print( test_int, type(test_int) )
if test_int % 2 == 0:
    print("Even number")
else:
    print("Odd number")