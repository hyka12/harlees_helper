import os, time, threading, tester, shutil, sys

logo = """\033[96m

 /$$   /$$                     /$$                                     /$$   /$$           /$$                              
| $$  | $$                    | $$                                    | $$  | $$          | $$                              
| $$  | $$  /$$$$$$   /$$$$$$ | $$  /$$$$$$   /$$$$$$   /$$$$$$$      | $$  | $$  /$$$$$$ | $$  /$$$$$$   /$$$$$$   /$$$$$$ 
| $$$$$$$$ |____  $$ /$$__  $$| $$ /$$__  $$ /$$__  $$ /$$_____/      | $$$$$$$$ /$$__  $$| $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$__  $$  /$$$$$$$| $$  \\__/| $$| $$$$$$$$| $$$$$$$$|  $$$$$$       | $$__  $$| $$$$$$$$| $$| $$  \\ $$| $$$$$$$$| $$  \\__/
| $$  | $$ /$$__  $$| $$      | $$| $$_____/| $$_____/ \\____  $$      | $$  | $$| $$_____/| $$| $$  | $$| $$_____/| $$      
| $$  | $$|  $$$$$$$| $$      | $$|  $$$$$$$|  $$$$$$$ /$$$$$$$/      | $$  | $$|  $$$$$$$| $$| $$$$$$$/|  $$$$$$$| $$      
|__/  |__/ \\_______/|__/      |__/ \\_______/ \\_______/|_______/       |__/  |__/ \\_______/|__/| $$____/  \\_______/|__/      
                                                                                              | $$                          
                                                                                              | $$                          
                                                                                              |__/                          
"""

for x in range(len(sys.argv)):
    if sys.argv[x] == "--harlee-mode":
        logo = logo = """\033[96m

             /$$   /$$                     /$$                                     
            | $$  | $$                    | $$                                     
            | $$  | $$  /$$$$$$   /$$$$$$ | $$  /$$$$$$   /$$$$$$         
            | $$$$$$$$ |____  $$ /$$__  $$| $$ /$$__  $$ /$$__  $$      
            | $$__  $$  /$$$$$$$| $$  \\__/| $$| $$$$$$$$| $$$$$$$$     
            | $$  | $$ /$$__  $$| $$      | $$| $$_____/| $$_____/        
            | $$  | $$|  $$$$$$$| $$      | $$|  $$$$$$$|  $$$$$$$       
            |__/  |__/ \\_______/|__/      |__/ \\_______/ \\_______/                                                                                                                                    
            """ 


running=True
current_exercise=0
completed_amount=0

exercise_paths = []
solution_paths = []
reset_paths = []
exercises = ["1_types", "2_if..else", "3_loops", "4_casts", "5_str","6_ops","7_lists","8_funcs","9_objs"] 

for x in exercises:
    exercise_paths.append(os.getcwd()+"/exercises/"+x+"/test.py")
    solution_paths.append(os.getcwd()+"/ignore/exercises/"+x+"/solution.py")
    reset_paths.append(os.getcwd()+"/ignore/exercises/"+x+"/test.py")

print(logo+f"\n r:reset        n:next        q:quit        current: {exercise_paths[current_exercise]}\n")

def file_whatcher(file_paths):
    last_modified = []

    for path in file_paths:
        last_modified.append(os.path.getmtime(path))

    while(running):
        for i in range(len(file_paths)):
            current_modified = os.path.getmtime(file_paths[i])

            if current_modified != last_modified[i]:
                try:
                    exec(open(file_paths[i]).read())
                    last_modified[i] = current_modified

                except Exception as e:
                    print(e)
                    last_modified[i] = current_modified
                    break
                
        time.sleep(0.1)

def input_handler(): 
    global running, current_exercise;

    while(running):
        usri=input()

        if usri == "q":
            running=False
            print("\033[0m")
            break

        elif usri == "s" and tester.current_done:
            solution_path = exercise_paths[current_exercise][:-7]+"solution.py"
            os.system("cls")
            print(logo+f"\nr:reset        n:next        q:quit        solution: {solution_path}\n")
            shutil.copy(solution_paths[current_exercise], exercise_paths[current_exercise][:-7]+"solution.py")

        elif usri == "n" and tester.current_done:

            if current_exercise+1<len(exercises):
                current_exercise+=1
                os.system("cls")
                print(logo+f"\nr:reset        n:next        q:quit        current: {exercise_paths[current_exercise]}\n")
                tester.current_done=False

            else:
                os.system("cls")
                print(logo+"\n Congradualations, You've completed my course, are you proud of ur self, cuz im proud of You ...")

        elif usri == "n" and tester.current_done!=True:
            print("the current_exercise hasnt been fully completed")

        elif usri == "r":
            os.system("cls")
            print(logo+f"\nr:reset        n:next        q:quit        current: {exercise_paths[current_exercise]}\n\ncurrent file has been reset\n")
            shutil.copy(reset_paths[current_exercise], exercise_paths[current_exercise])


if __name__ =="__main__":
    file_whatching = threading.Thread(target=file_whatcher, args=(exercise_paths,))
    input_handling = threading.Thread(target=input_handler, args=())

    file_whatching.start()
    input_handling.start()

    file_whatching.join()
    input_handling.join()
