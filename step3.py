group_28 = ['Митя', 'Данила', 'Георгий', 'Герасим', 'Анастасия']
print('группа 28', group_28)
print(group_28[0], group_28[2])
print(type(group_28), dir(group_28))

print(group_28[len(group_28) - 1])
print(group_28[- 1])

group_28.append('Пётр')
print(group_28)

group_28.insert(2, 'Роман')
print(group_28)

last_student = group_28.pop()
print(last_student)
print(group_28)