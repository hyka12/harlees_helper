#this is fairly straight forward

#the def keyword specifies that we are making a function
#followed by the name of the function with paretheses
#inside the paretheses is where the variables that the function needs to work
#in this example this function needs an object thats called word in the scope of 
#of the function

def ex_function(word):
    for x in range(10):
        print(word)

#this is how the function is called
ex_function("words here")

#functions can also return variables in this example
#we have a function that takes 2 variables and adds them together
def addition(a, b):
    return a+b 

print(addition(10, 10)) #print is a built in function that 
                        #displays items to the terminal

