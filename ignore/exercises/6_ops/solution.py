#TASK: your task is to fix the operations in this, so when the numb var fits in 3 
#then add the word "fizz" to the list, if the number fits in 5 then add "buzz"
#if the number fits in both add "fizzbuzz"

List = []

for x in range(20):

    #modify the following if statements

    if x%3!=True and x%5!=True:
        List.append("fizzbuzz")

    elif x%3!=True:
        List.append("fizz")

    elif x%5!=True:
        List.append("buzz")

tester.checker_6(List)

