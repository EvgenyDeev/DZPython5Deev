# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
text = 'Всем привет, абв какое прекрасное утро абв ! хорошего дня теебе :) абв'

def del_text(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

text = del_text(text)
print(text)