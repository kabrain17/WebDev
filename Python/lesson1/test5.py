a = 'XS'
b = 'XL'

size_weights = {
    'S':5,
    'M':10,
    'L':15,
}


a_size, b_size = a[-1], b[-1]
a_count, b_count = a.count('X'), b.count('X')
a_weight = size_weights [a_size]
b_weight = size_weights [b_size]

if a_count != 0:
    a_count +=1
    if a_size == 'S':
        a_weight /= a_count
    elif a_size == 'L':
            a_weight *= a_count

if b_count != 0:
    b_count += 1
    if b_size == 'S':
        b_weight /= b_count 
    elif a_size == 'L':
        b_weight *= b_count

operand = '='
if a_weight > b_weight:
    operand = '>'
elif a_weight < b_weight:
    operand ='<'

print(f'{a} {operand} {b}')
