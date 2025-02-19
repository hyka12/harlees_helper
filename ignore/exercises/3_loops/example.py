#these are loop is how tasks are repeteated or lists are cycled through
#this is the while loop and it would run forever if there was never a break

count = 0
while True:
    print(count)

    count+=1

    if count>25:
        break


#the for loop can be using in 2 ways, 
#this first one is numerical, 
#so basically it counts from 0 up to whatever number has been set 

for x in range(25):
    print(x)

#this is how you go through each item in a list

list = ["monkey1", "monkey2", "monkey3", "monkey4", "monkey5"]

for element in list:
    print(element)
