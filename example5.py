####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E5'
strategy_name = 'Collude first 100 rounds unless betrayed. Betray 101st round forward.'
strategy_description = '''\
Betray if ever betrayed.
If I haven't been betrayed yet, I'll betray starting with the 100th round.
'''

import random
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    # If the other player has betrayed or this is the last half of the game, 
    if 'b' in their_history or len(their_history)>100: 
        return 'b'               # Betray.
    else:
        return 'c'         # but 90% of the time collude
    
def move(my_history, their_history, my_score, their_score):
  ''' '''
  if len(my_history) > 98: #It's the last round, backstab
    return 'b'
  elif their_history[-1]=='b':
    return 'b' # Betray if severely punished last time,
  elif len(my_history)==0: #It's the first round, collude
    return 'c'
  else:
    return 'c' # otherwise collude if opponent also colludes.

def move(my_history, their_history, my_score, their_score):
  if len(their_history)%2 == 0:
      return 'c'
  else:
      return 'b' 


#My knowledge as I will be absent thursday
#Name = Tit for Tat Backstabbing
#Description = Collude until opponent backstabs, if they do, copy their previous move for the rest of the game until the last round, then backstab on round 100