# SEQUENTIAL: Eksekusi berurutan
print('Hello World!')
print('this command')
print(f'Hello World!\n'
      f'this command multiline')
print('execute sequencial')
print('-' * 10)

# CONDITION
is_danger = True
if is_danger:
    print('turn arround')
else:
    print('straight ahead')

# LOOPING
num = 4

print('\n for ')
print('-' * 10)

for idx in range(1, num+1):
    print(f'Hello number #{idx}')

print('\n while ')
print('-' * 10)
times = 0
while times < 20:
    times += 1
    print(f"print {times} times")
    if times == 11:
        break
