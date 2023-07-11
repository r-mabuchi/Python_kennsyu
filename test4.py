for i in range(0,40):
    i +=1
    if i %4 ==0 and i %5 ==0:
        print('FizzBuzz')
    elif i %4 ==0:
        print('Fizz')
    elif i %5 ==0:
        print('Buzz')
    else:
        print(i)