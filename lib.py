  
def lb(n):


nums = [45, 55, 60, 37, 100, 105, 220]


guess = int(input('Введите число на которое хотите поделить : '))


if n % guess == 0 :
    print('все ок')
    print(nums[n] / guess)

elif n % guess <= 0 :
    print('Нельзя поделить')
    print(nums[n] / guess)

else:
    print('Nельзя поделить')


