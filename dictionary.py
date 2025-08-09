# phonebook = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
# print(phonebook)

# if 'Chris' in phonebook:
#     print(phonebook['Chris'])

# phonebook['Joe'] = '555-0123'
# phonebook['Chris'] = '555-4444'
# print(phonebook)

# person = {
#     "name": "mike",
#     "birthday": "1980-09-09",
#     "height": "5.9",
#     "hair_color": "white"

# }
# print(person['name'])
# del person['name']
# print(person)

test_scores = { 'Kayla' : [88, 92, 100], 
               'Luis' : [95, 74, 81],
                'Sophie' : [72, 88, 91], 
                'Ethan' : [70, 75, 78] 
            }

print(test_scores)
kayla_scores = test_scores['Kayla']
print(kayla_scores)

for score in test_scores['Kayla']:
    print(score)


mixed_up = {'abc':1, 
            999:'yada yada', 
            (3, 6, 9): [3, 6, 9]}
print(mixed_up)

phonebook = {}
print(phonebook)
phonebook['Chris'] = '555-1111'
phonebook['Katie'] = '555-2222'
phonebook['Joanne'] = '555-3333'
print(phonebook)

phonebook = {'Chris':'555-1111', 
             'Katie':'555-2222', 
             'Joanne':'555-3333'}

for key in phonebook:
    print(key)
for key in phonebook:
    print(key, phonebook[key])



phonebook.clear()
print(phonebook)

phonebook = {'Chris':'555-1111', 'Katie':'555-2222'}
value = phonebook.get('Katie2', 'Entry not found')
print(value)


print(phonebook.items())

for key, value in phonebook.items():
    print(key, value)

for key in phonebook.keys():
    print(key)

# phone_num = phonebook.pop('Katie', 'Element not found')
# print(phone_num)
# print(phonebook)

for val in phonebook.values():
    print(val)