print('Scalar data type')
num1 = 'Eko'
num2 = 'Dwi'
num3 = 'Tri'
num4 = 'Catur'

print(num1)
print(num2)
print(num3)
print(num4)

print('\nList data type')
jvnumber = ['Eko', 'Dwi', 'Tri', 'Catur']
print(jvnumber)
jvnumber.append('Limo')
print(jvnumber)

print('\ncall number 2')
print(f'Hello {jvnumber[1]}!')

print('\ncall all jvnumber')
for a in jvnumber:
    print(f'Hello {a}!')

print('\ndiferent way to print list of jvnumber')
for a in range(0, len(jvnumber)):
    print(f'{a+1}.  {jvnumber[a]}')