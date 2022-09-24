#Напишите программу, удаляющую из текста все слова, содержащие 'абв'

tex = 'Напишитеабв программу, удаляющую из текстаабв все слова, содержащие "абв"'
print(' '.join((filter(lambda x: 'абв' not in x, tex.split()))))


# lst = list(tex.split()) 
# print(lst) 
# lst = list(filter(lambda x: 'абв' not in x, lst)) 
# print(' '.join(lst))
