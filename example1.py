####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E1'
strategy_name = 'Betray if they betrayed the last two times'
strategy_description = 'If both of the previous two moves of the opponent are betray, then betray the next turn. '
    
def move(my_history, their_history, my_score, their_score):
  ''''''
  if len(my_history) > 1:
    if their_history[-1] == 'b' and their_history[-2] == 'b':
      return 'b'
  else:
    return 'c'
  
