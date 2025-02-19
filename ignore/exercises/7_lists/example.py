# lists are pretty simple there just a few things u need to know

# the functions that are built into objects(such as the list) are called methods 

# a list is a built-in object in python and these are the methods that 
# you can call to make changes to lists 

List = ["monkey","ben",10]

List.append(5)     # adds an object to the end of a list

List.extend([5,6]) # adds a list to your list so this will add 5,6 to yur list

List.insert(0,1)   # adds an object at a specifc location in the list, this adds 1 to 
                   # the beginning of the list, because the first number is 0

List.remove(1)   # removes a object from the list at the given index, which in this case
                 # is at 0, so its going to remove the first item

removed_element = List.pop(2) # this removes an item from the list and returns it
                              # so if we were to read removed_element we would get 
                              # what it took out of the list

List.index("monkey") # returns the location of the first time 
                     # this object shows up in the list

#sorts a list by the form lowest to highest number, tbh idk...
#i commented it out because other wise it complains because we have strings...
#List.sort() 

List.reverse() # flips the entire list so the last item is now the first
               # and vise versa so first is now last

new_list = List.copy() #allows you to copy one list to another

len(List) # this technically isnt a method, but its very important
          # this returns the size of a list

list2 = "harlee hates me" 

ur_name = list2[0:6]       #[:6] or [:-2] is also valid 
me = list2[-2:]         #this grabs the last 2 characters

print (ur_name + " loves " + me )
