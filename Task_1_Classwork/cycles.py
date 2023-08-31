'''Цикл While'''

number = 0

while number<10:
    print(f'number={number}')
    number +=1
print('app close')

string ='54'

while len(string)>0:
    print('String exist - '+ string)
    string=string[0:len(string)-1]
else:
    print('blank string')

'''Цикл For'''

def cycle_for(items):

    for item in items:
        print(item)


cycle_for('string')
cycle_for([0,1,2])
cycle_for(('a','b','c'))

def sum_list(my_list):
    result=0
    for elem in my_list:
        result=result+elem
    return result

print(sum_list([1,2,3]))

def sum_list2(my_list):
    return sum(my_list)


print(sum_list([1,2,3]))