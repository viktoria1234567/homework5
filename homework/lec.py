# 1.Напишите программу, удаляющую из текста все слова, содержащие ""абв""
text = 'Привет абвменя зовут Иван абвя живу в абвБеларуси'

def some_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = some_words(text)
print(text)
