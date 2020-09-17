  
def lb(n):
        a = [45, 55, 60, 37, 100, 105, 220]


        guess = int(input('Введите число на которое хотите поделить : '))
        for x in a:
            if x % guess == 0 :
                    print('все ок')
                    print(x / guess)

            


