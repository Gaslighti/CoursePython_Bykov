lang = 'Python'
if lang == "Python":
    print('Hello')
print('End')

def get_types_of_sentense(sentense):
    last = sentense[-1]

    if last == "?":
        sentense_type = 'question'
    else:
        sentense_type = "normal"

    return 'sentense is '+ sentense_type

print(get_types_of_sentense('sentense'))
print(get_types_of_sentense('Sentense???'))

def user_number(user_data):
    permit_print = True

    if permit_print and user_data == -6:
        print('value = -6')

    elif permit_print and user_data > 0:
        print("value positive")

    elif not permit_print:
        print('print denied')

user_number(-6)
user_number(6)
user_number(0)

def student_rank(year_of_study):
    if year_of_study in range(1,5):
        print('You Bachelor')
    elif year_of_study in range(5,7):
        print('You Master')
    elif year_of_study in range(7,10):
        print('You Graduate student')
    else:
        print('input correct value year of study')

student_rank(5)
student_rank(8)
student_rank(15)