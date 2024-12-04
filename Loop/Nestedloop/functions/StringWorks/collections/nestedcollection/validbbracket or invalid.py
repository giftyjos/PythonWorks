# ....nxt qn.....

   # sample_input="{}"
    # op=>valid

    # "{()}" valid

    # "{(})}" valid

    # "[](" =valid

user_input=input("enter bracket pairs")

symbol_dictionary={

  "{":"}",
  "[":"]",
  "(":")",
  "<":">"
}
symbol_stack=[]#list 
top=-1
is_valid=True
for symbol in user_input:#symbol={
  if symbol in symbol_dictionary:#symbol is an opening
    top=top+1
    symbol_stack.append(symbol)#push the symbol to satck
  elif top==-1:
    is_valid=False
  elif symbol== symbol_dictionary.get(symbol_stack[top]):#chck symbol is a valid closing
    top=top-1
    symbol_stack.pop()
  else:
    is_valid=False
  if len(symbol_stack)==0 and is_valid==True:  #=0 means symbol stackil onula empty
    print("valid")
  else:
    print("invalid")

  # list,dictionary


  lst1=["apple","mango","onion","potato"]
  lst2=[100,200]

# {"apple":100,"mango":200,"onion":1,"potato":2}