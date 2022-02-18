#猜数字游戏
import random

guessesTaken= 0;

print('Hello! What is your name');
myName=input();


number=random.randint(1,20);
print('well, '+myName+'I am thinking of a number between 1 and 20');

for i in range(6):
    print('Take a guess');
    guess=input()
    guess=int(guess);

    if guess<number:
     print('Your guess is too low');

    if guess>number:
     print('Your guess is too high');

    if guess==number:
     break;


if guess==number:
 guessesTaken=str(guessesTaken);
 print('good job'+myName+'you guessed my number in'+guessesTaken);

if guess!=number:
 number=str(number);
 print('Nope. The number Iwas thinking pf was'+number+'-');


