#TASK: make a for loop that loops 10 times and appends the numbers to the list
# so then we will have a list with 0-9, then i want u to remove the number 8
# good luck ...

ur_list = []

for x in range(10):
    ur_list.append(x)

ur_list.remove(ur_list.index(8))

tester.checker_7(ur_list)
