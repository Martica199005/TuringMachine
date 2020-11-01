dict={'val1':' ','val2':'#','val3':'UPPERCASE'}

rules={'rule1':('0','A','1','B','R'),'rule2':('2','B','3','A','L'), 'rule3':('1','B','1','B','L'),'rule4':('2','D','1','F','L'), 'rule5':('0','B','4','D','R'),'rule6':('4','B','2','A','R'),'rule7':('3','A','5','A','H')}

tasks=['step','accept','k_accept']


def readTM():
  task=input("Give the name of the task\n")
  if task==tasks[0]:
    input_list=input("Give the list of inputs saparated by space\n")
    number_states=int(input("Give the number of states\n"))
    print("-\n")
    transitions=input("Give the transitions\n")
    return step(input_list,transitions)
  elif task==tasks[1]:
    words=input("Give the list words saparated by space\n")
    number_states=int(input("Give the number of states\n"))
    end_states=input("Give the list of the final states saparated by space\n")
    transitions=input("Give the transitions\n")
    return accept(words,end_states,number_states,transitions)
  elif task==tasks[2]:
    k_words=input("Give the steps+words saparated by space\n")
    number_states=int(input("Give the number of states\n"))
    end_states=input("Give the list of the final states saparated by space\n")
    transitions=input("Give the transitions\n")
    return k_accept(k_words,end_states,number_states,transitions)
    
  
  


def go_left(word,index,char):
  if index >0:
    index=0
    word=list(word)
    word[index]=char
    print(word[index])
    new_word="".join(word)
    print(new_word)
    new_index=index-1
    return [new_word,new_index,new_word[:new_index]]
  elif index==0:
    print('cannot go on the left')
  else:
    print('error')

def go_right(word,index,char):
  if index <len(word)-1:
    index=0
    word=list(word)
    word[index]=char
    print(word[index])
    print("".join(word))
    new_word= "".join(word)
    new_index=index+1
    return [new_word[new_index:],new_index,new_word[index]]
  elif index==len(word)-1:
    print('cannot go on the right')
  else:
    print('error')

def hold(word,index,char,):
  word=list(word)
  if index in range(0,len(word)):
    word[index]=char
    print(word[index])
    print("".join(word))
    new_word= "".join(word)
    new_index=0
    return [new_word,new_index]


def step(conf,dict_rules):
  left_word=conf[0]
  print(left_word)
  state=conf[1]
  right_word=conf[2]
  print(right_word)
  for key, value in dict_rules.items():
    if state==value[0] and right_word[0]==value[1]:
      print(value)
      state=value[2]
      print('new state '+value[2])
      if value[4]=="L":
        print('left')
        result=go_left(right_word,1,value[3])
        new_tuple=(left_word[:-1],state,left_word[-1]+result[0])
      elif value[4]=="R":
        print('right')
        result=go_right(right_word,0,value[3])
        new_tuple=(left_word+result[2],state,result[0])
      elif value[4]=="H":
        print('hold')
        result=hold(right_word,0,value[3])
        new_tuple=(left_word,state,result[0])
    if not new_tuple:
      return False
    else:
      return new_tuple
    

    

def accept(word,final_states,num_states,dict_rules):
  print(word)
  tuple2=('#','0',word)
  result=True
  while result:
    tuple3=step(tuple2,dict_rules)
    if tuple3 is None:
      result=False
    else:
      print(tuple3)
      result=True
      tuple2=tuple3
  if tuple2[1] in final_states and result==False:
    return True
  else:
    return False

# cambia k word
def k_accept(k_word,final_states,num_states,dict_rules):
  count=0
  print(word)
  tuple2=('#','0',word)
  result=True
  while result:
    tuple3=step(tuple2,dict_rules)
    if tuple3 is None:
      result=False
    else:
      print(tuple3)
      result=True
      tuple2=tuple3
      count=count+1
  if tuple2[1] in final_states and result==False and count<=k:
    return True
  else:
    return False



# tuple1=('D','2','BBB')
# print(step(tuple1,rules))

# word="BBB"
# end_states=[6,5]
# print(accept(word,end_states,7))

readTM()



