#Creating a list and Altering the list 
my_list=[1, 2, 3, 108, 'vikhram', 92, 89, 54, 2] #Creates a list with the given values
print(my_list) #prints my list
my_list.pop() #pops the last element
print(my_list) 
my_list.remove("vikhram") #removes the entered value
print(my_list) 
my_list.pop(2) #pops the element in index 2 
print(my_list)
my_list.append([32, 43]) #adds the given element to the list
print(my_list)
a=my_list.pop(6)  #pops the element in index 3 
print('popped element : ' , a,) 

#Other functions of the list
print(len(my_list)) #prints the length of the list
print(my_list.index(2)) #Prints the first found  index of 2
print(my_list.count(2)) #returns the number of times 2 in=s in the list
my_list.sort() #sorts the list in ascending order 
print(my_list)
my_list.sort(reverse=True) #Reverses the list
print(my_list)
my_list.clear() #clears the entire list 
print(my_list)