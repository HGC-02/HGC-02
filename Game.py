#player can not control the character
#pls dont gambling
import random
score=0
run=1
while run==1:#let the commend keep running
  a=random.randint(1,2)#randomly to genterate a numder to decide the game character get shot or not
  if a==1:# decide the game id the character not get shoot
    score=score+1#this is the result of the game character alive one round
    print("you alive one round")
  elif a==2:#same as line 6 but is get shot
    print("you die")
    print("round you alive is",score)
    run=0
    break#the game character die,the game end