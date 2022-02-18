import random
import time

def displayIntro():
    print("'你进入到了龙之岛，山洞里有丰富的宝藏，但是其中一个山洞很危险，你要去哪个山洞？'");
    print();

def chooseCave():
    cave=''
    while cave!='1' and cave!='2':
        print('你想进入哪个山洞？?(1 or 2)')
        cave =input()

        return cave




def checkCave(chosenCave):
    print('你进入了山洞')
    time.sleep(2);
    print('一条巨大的龙看到了你，然后。。。')
    print()
    time.sleep(2)

    friendlyCave=random.randint(1,2)

    if chosenCave == str(friendlyCave):
        print('给你了一份礼物！')
    else:
        print('把你吃进了嘴里！')




playAgain='yes'
while playAgain=='yes' or playAgain=='y':
    displayIntro();
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('你想再玩一次吗？(y or n)')
    playAgain=input();
