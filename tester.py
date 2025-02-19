current_done = False

def checker_1(luke, harlee):
    global current_done

    luke_correct=False
    harlee_correct=False

    if isinstance(luke, str) and luke == "luke has a python in his pants":
        print("\nYou Got The luke Variable Perfect!, want head...")
        luke_correct=True

    elif isinstance(luke, str) and luke != "luke has a python in his pants":  
        print("\nyour luke variable is the correct type, but the message isnt correct")

    elif isinstance(luke, str)!=True: 
        print("\nyour luke variable is the wrong type")


    if isinstance(harlee, str) and harlee == "harlee is a python master":
        print("\nYou Got The harlee Variable Perfect!")
        harlee_correct=True

    elif isinstance(harlee, str) and harlee != "harlee is a python master":  
        print("\nyour harlee variable is the correct type, but the message isnt correct")

    elif isinstance(harlee, str)!=True: 
        print("\nyour harlee variable is the wrong type")

    if luke_correct and harlee_correct:
        current_done=True
        print("\nif you would like to see how i would solve it press s...")


def checker_2(a, b, c):
    global current_done;

    if a == 0 and b == 5 and c == 5:
        print("\n Nice u got it :()")
        current_done=True

def checker_3():
    global current_done;

    print("\nI knew u were a smart cookie")
    current_done=True
    

def checker_4(summ):
    global current_done;

    if isinstance(summ, int) and summ == 76:
        print("\nYour really smart, and cool...")
        current_done=True

    elif isinstance(summ, int)!=True: 
        print("\nthe type of your variable is wrong, it should be an int...")

def checker_5(harlee):
    global current_done;

    if harlee == "loves luke":
        print("\nYour getting good...")
        current_done=True
        
def checker_6(input_list):
    global current_done;

    List = []

    for x in range(20):

        if x%3!=True and x%5!=True:
            List.append("fizzbuzz")

        elif x%3!=True:
            List.append("fizz")

        elif x%5!=True:
            List.append("buzz")

    if List == input_list:
        print("\nIm Proud of U...")
        current_done=True

    elif List != input_list:
        print("\nIt doesnt seem to be right...")
        

def checker_7(input_list):
    global current_done;

    correct_list = [0,1,2,3,4,5,6,7,9]
    close_list = [0,1,2,3,4,5,6,7,8,9]

    if input_list == correct_list:
        print("\nTHATS RIGHT, HOLY FISH...")
        current_done=True

    elif input_list == close_list:
        print("\nThat was really close...")


def checker_8(i):
    global current_done;

    if i==(35-15):
        print("\nYour Too good, this should be ilegal")
        current_done=True
        
def checker_9(name):
    global current_done;

    if name != "harlee" and name != "luke":
        print("\nGood jub, You Did it")
        current_done=True

    elif name == "luke":
        print("\nGood job, called it...")
        current_done=True












 

