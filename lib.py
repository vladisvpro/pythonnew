  
def lb(n):
        a = [45, 55, 60, 37, 100, 105, 220]


        guess = int(input('Введите число на которое хотите поделить : '))
        for q in a:
            if q % guess == 0 :
                    print('все ок')
                    print(q / guess)
            else:
                print('Оно с остатком(не записуеся)')
                

            


