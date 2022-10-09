# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

TextDel = 'Напишите абв напиабв програбвмму программу, удаляющую из \
    этого абв текста все вабвс слова, содерабващие содержащие "абв"'

def DelWords(TextDel):
    TextDel = list(filter(lambda x: 'абв' not in x, TextDel.split()))
    return " ".join(TextDel)

TextDel = DelWords(TextDel)
print(TextDel)