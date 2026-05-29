string_1 = '123123'
print(len(string_1))
print(len([1,2,3]))
print([1,2,3][2])

list_validation = [1,2,3]
print(f'size of list list_validation: {len(list_validation)}')
for k in range(len(list_validation)):
    print(f'index: {k}, value: {list_validation[k]}')

tesx_str = ('sdasdassdasdada-dsadadadsadasdasdasda,'
            'dsakdjajsdaidjasdjiawjdiwajidwaiodwaijdiawd'
            'dsaidkjakjdk asdkjdaksjskdjkajsdka dskjdskajds ksa')

string1 = 'TEXT'
print(string1[:1:])

print(tesx_str[:100:-1])


#кортедж (тапл)
tuple_2 = (1, 2, 3, 4, 5)
tuple_3 = tuple_2[1:3]
print(type(tuple_3))
print(id(tuple_2) == id(tuple_3))

print('123123'[-1])

print(max((1, 2, 3, 4, 5)))
print(min((1, 2, 3, 4, 5)))


int_value = 0
for k in (1,2,3,4,5):
    if int_value < k:
        int_value = k

