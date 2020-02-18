####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E1'
strategy_name = '65-35'
strategy_description = '65% collude, 35% betray'
    
def move(my_history, their_history, my_score, their_score):
  '''This function makes it a 65% collude, 35% betray situation/strategy'''
  opponent_b = 0 
  for decision in their_history:
    if decision == 'b':
      opponent_b+=1
  if len(their_history)==0:
    return "c"
  else:
    if opponent_b/len(their_history)>0.35 or their_score > my_score:
      return 'b'
    else:
      return 'c'
  print(opponent_b)
