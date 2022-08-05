import random
def rpc():
    
    player=input("Pick any one- 'r' for rock,'p' for papaer,'s' for scissors")
    pc=random.choice(['r','p','s'])

    if player==pc:
        return 'its a draw'
    
    if won(player,pc):
        return 'you won'

    return'you lost'

def won(player1,pc1):
    if(player1=='r'and pc1=='s') or (player1=='s' and pc1=='p') or (player1=='p' and pc1 == 'r'):
        return True
        
    print (rpc())
    print("computer choice was ",pc)
