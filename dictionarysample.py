#Creating a Dictionary
my_dict={} #Declaring an Empty Dictionary
print(my_dict) 
my_dict={'lang':'python', 'name':'Kamal',} #Assigning Values to the Dictionary
print(my_dict)
my_dict['des']='developer' #Adding one more Value the Dictionary
print(my_dict)
my_dict['name']='vikhram' #Changing the name kamal Into vikhram
print(my_dict)
a=my_dict.pop('des') #Removing the value of des
print('popped item:', a) #Prints the removed Item from the Dictionary
print('dictionary:', my_dict)  
b=my_dict.popitem() #Pops/Removes the last item of the Dictionary
print('popitem popped :', b) 
print(my_dict)
my_dict.clear() #Clears the Entire Dictionary
print(my_dict)