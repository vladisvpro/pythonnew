a = [45, 55, 60, 37, 100, 105, 220]
i = [0, 0]

n = int(input('Введіть число(45, 55, 60, 37, 100, 105, 220)--(0 = 45; 1 = 55; і т.д.)Всього чисел до 6 : '))


print(a[n])


print('Неможна брати число ( 0 --- нуль )' )


guess = int(input('Введыть число на яке хочете поділити : '))


while type(guess) != int:
    try:
        a = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите целое число: ")
 
if n % 2 == 0:
    print("Четное")
else:
    print("Нечетное")

print(a[n] / guess)






