# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
import time

elements=['r','p','s']

def Play():
  user_choice=input('Enter your choice'
                    ' \nr for Rock\np for Paper\ns for Scissors\n')
  computer_choice=random.choice(elements)
  if Verify_Choice(user_choice.lower()):
    Result(user_choice.lower(),computer_choice)
  else:
    print('Invalid Choice')


def Verify_Choice(user):
    return user in elements

def Result(user,computer):
  print('computers Choice '+computer)
  if user==computer:
    print('tie')
  elif ((user=='r'and (computer=='s'))or (user=='p'and (computer=='r'))or (user == 's' and (computer == 'p'))):
    print('win')
  else:print('lose')

  time.sleep(1)

if __name__ == '__main__':
  while(1):
    input('Press Enter to Play')
    Play()
