# collatz function

#ask user input a number


def collatz(number):
    if number % 2==0:
        num1=number//2
        print(str(num1))
    else:
        num2=3*number+1
        print(str(num2))

print('Enter number:')
guess = int(input())
print('the number is '+ str(guess))

while True :
        num=collatz(guess)
        if (num==1):
            break
        else:
            continue
        

