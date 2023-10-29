# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

n = int(input("Integer: "))

value_1 = int('%s' %n)
value_2 = int('%s%s' % (n, n))
value_3 = int('%s%s%s' % (n, n, n))

# value = (n+nn+nnn)

print(f'Result: {value_1+value_2+value_3}')