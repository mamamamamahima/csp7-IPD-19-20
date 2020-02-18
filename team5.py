####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team Coronavirus'
strategy_name = 'Tit for Tat Backstabbing'
strategy_description = 'Collude until opponent backstabs, if they do, copy their previous move for the rest of the game until the last round, then backstab on round 100'
    
def move(my_history, their_history, my_score, their_score):
  ''' '''
  if len(my_history) > 0: #If not round 1
    if len(my_history) > 98: #It's the last round, backstab
      return 'b'
    elif their_history[-1]=='b':
      return 'b' # Betray if severely punished last time,
    elif len(my_history)==0: #It's the first round, collude
      return 'c'
  else:
    return 'c' # otherwise collude if opponent also colludes.

