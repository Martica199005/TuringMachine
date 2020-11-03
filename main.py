import sys
import re
read_line=[]
input_lines=[]
rules=[]
trim_rules=[]
new_list=[]
listOflist=[]
k_values=[]
output=[]
list_rules=[]
test_list=[]





#it eliminates the () from the first and last element in list input_lines
def eliminate_parenthesis(list_words):
    for word in list_words:
        list_new=word.split(",")
        list_new[0]=list_new[0].replace("(","")
        list_new[2]=list_new[2].replace(")","")
        listOflist.append(list_new)
    return listOflist



def rule_found(left_word,state,right_word,new_rules):
    found=False
    rule=""
    for value in new_rules:
        if state==value[0] and right_word[0]==value[1]:
            rule=value
            found=True
    return [found,rule]



    
def go_right_1(word,char):
    word=list(word)
    word[0]=char
    new_word="".join(word)
    if len(word)>1:
        new_left=new_word[0]
        new_right=new_word[1:]
    else:
        new_left=new_word[0]
        new_right="#"
    return [new_left,new_right]

def hold(word,char):
    word=list(word)
    word[0]=char
    new_word="".join(word)
    return new_word

def go_left_1(word,char):
    word=list(word)
    word[0]=char
    new_word="".join(word)
    return new_word
  
    

    
    
def step(conf,dict_rules):
    new_list=[]
    left_word=conf[0]
    state=conf[1]
    right_word=conf[2]
    found_value=rule_found(left_word,state,right_word,dict_rules)
    if found_value[0]==False:
        return False
    else:
        value=found_value[1]
        state=value[2]
        #new state value[2]
        #new char value[-1][:-1]
        last_val=value[-1]
        direction=last_val[-1]
        new_char=last_val[:-1]
        if direction=="L":
            result=go_left_1(right_word,new_char)
            if left_word[:-1]=="":
                new_conf=("#",state,left_word[-1]+result)
            else:
                new_conf=(left_word[:-1],state,left_word[-1]+result)
        elif direction=="R":
            result=go_right_1(right_word,new_char)
            new_conf=(left_word+result[0],state,result[1])
        elif direction=="H":
            result=hold(right_word,new_char)
            new_conf=(left_word,state,result)
        else:
            new_conf=False
        return new_conf


    
def accept(word,final_states,num_states,dict_rules):
    tuple_in=('#','0',word)
    result=True
    while result:
        new_tuple=step(tuple_in,dict_rules)
        if type(new_tuple)==type(True):
            result=False
        else:
            result=True
            tuple_in=new_tuple
    if tuple_in[1] in final_states and result==False:
        return True
    else:
        return False
    
    
def k_accept(k,word,final_states,num_states,dict_rules):
    count=0
    tuple_in=('#','0',word)
    result=True
    while result:
        new_tuple=step(tuple_in,dict_rules)
        if type(new_tuple)==type(True):
            result=False
        else:
            result=True
            count=count+1
            tuple_in=new_tuple
            
    if tuple_in[1] in final_states and result==False and count<=int(k):
        return True
    else:
        return False
    
    
def match_word(string):
      pattern = re.compile("[A-Z#]+")
      # if found match (entire string matches pattern)
      if pattern.fullmatch(string) is not None:
        return True
      else:
        return False

def match_int(string):
    pattern = re.compile("[0-9]+")
    if pattern.fullmatch(string) is not None: # if found match (entire string matches pattern)
        return True
    else:
        return False



def split_word(word):
    return re.split('(\d+)',word)


def check_rule(word):
    count_char=0
    count=0
    if len(word)>4:
        for char in word:
            if char.isalpha() or char=="#":
                count_char=count_char+1
            elif char.isdigit():
                count=count+1
            else:
                return False
        if count_char>=3 and count>=2:
            return True
        else:
            return False
    else:
        return False


  
       
def readTM():
  #take off the \n sys.stdin
  for line in sys.stdin:
      x = line.replace("\n", "")
      read_line.append(x)

  num_states=read_line[2]
  final_states=read_line[3].split()
    

  #read_line reads strings from input
  #input_lines is a list of the inputs
  input_lines=read_line[1].split()
  


  #rules contains the rules from input
  for i in range(4,len(read_line)):
        rules.append(read_line[i])

  #trim the elements in the rules list        
  for i in rules:
      y=i.replace(" ","")
      trim_rules.append(y)

  for val in trim_rules:
      if check_rule(val): #check on the rules
          list_rules.append(split_word(val)) 
  
  for y in list_rules:
      test_list.append(list(filter(None, y)))
      

      
      
  if read_line[0]=='step':
      #the list of input configurations
      #trim_rules contains the rules
      listOflist=eliminate_parenthesis(input_lines)
      for word in listOflist:
          x=step(word,test_list)
          if type(x)!=bool:
              val_out="("+x[0]+","+x[1]+","+x[2]+")"
          else:
              val_out=x
          output.append(val_out)

  elif read_line[0]=='accept':
      #input_lines and test_list
      for word in input_lines:
      #word=input_lines[0]
        output.append(accept(word,final_states,num_states,test_list))
  elif read_line[0]=='k_accept':
      for i in input_lines:
          k_values=i.split(",")
          #k_values[0] is the word, k_values[1] is the number k
          output.append(k_accept(k_values[1],k_values[0],final_states,num_states,test_list))

          
  print(*output)  


readTM()


