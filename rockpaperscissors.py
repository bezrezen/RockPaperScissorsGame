import random

print('Камень,ножницы или бумага?')
answers = ("камень","ножницы","бумага")
ai_answer = random.choice(answers)
#print(ai_answer)
#проверка алгоритма
player_answer = input()
if player_answer == ai_answer:
    print('Ничья')
elif (player_answer == 'камень') and (ai_answer == 'ножницы'):
    print('Ты победил')
elif (player_answer == 'бумага') and (ai_answer == 'камень'):
    print('Ты победил')
elif (player_answer == 'ножницы') and (ai_answer == 'бумага'):
    print('Ты победил')
else:
    print('Ты проиграл')
print('Я выбрал: '+ ai_answer)
