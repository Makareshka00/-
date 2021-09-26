student = ('Иван Питонов', 2001, [8, 7, 7, 9, 6], True)
element1 = student [0]
name = element1 [:4]
surname = element1 [5:]
print ('Студент: ', surname, name)
age = student [1]
print ('Возраст: ', 2020 - age)
notes = student [2]
print ('Оценки: ', str(notes))
av_note = sum(notes)/len(notes)
print ('Средний балл: ', av_note)
if av_note >= 8:
    print ('Повышенная стипендия: ', True)
else:
    print ('Повышенная стипендия: ', False)
