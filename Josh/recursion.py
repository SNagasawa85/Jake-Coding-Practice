

def recursion(num):
  if int(num) != 15:
    num = input('guess again')
    recursion(num)
  else:
    print('you win!!')

recursion(input('guess a number!'))