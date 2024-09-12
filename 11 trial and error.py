import sys

greet = ('''what would you like to do?
Choose an option:
1. Add a new task
2. Remove a task
3. View tasks
4. Prioritize a task
5. Mark task as completed
6. Clear all tasks
7. Exit''')

print(greet)
userTask = [] #INI HARUS DILUAR WEH, KARENA MIKIR ANJING, KALO LU MASUKIN DI DALEM WHILE LOOP
              #NANTI BAKAL RESTART, KARENA TIAP ITERATION BAKAL NGEBACA userTask = []
while True:
    try:
        askMainMenu = int(input('choose an option(1/2/3/4/5/6/7): '))
        if 1 <= askMainMenu <= 7: #
            if askMainMenu == 1: #
                askOption1 = input('type in new task: ')
                userTask.append(askOption1)
            elif askMainMenu == 2: #
                for i in userTask:
                    print(i, end='\n')
                try:
                    askOption2 = int(input('which task you want to remove?(enter the task number) : '))
                    del userTask[askOption2 - 1]
                except IndexError:
                    print('input invalid, you do not have that many tasks.')
                except ValueError:
                    print('input invalid, you did not enter a number.')
            elif askMainMenu == 3: #
                for i in userTask:
                    print(i, end='\n')
            elif askMainMenu == 4: #In Python, you cannot directly change the index of an item in a list.
                                     #However, you can effectively "move" an item to a different index by removing it from its current position
                                     #and inserting it into the desired position. Here's how you can do that:
                                     #1. Remove the item from its current index.
                                     #2. Insert the item at the new index
                                     #pake method yang belum gua pelajarin anjir,
                                     #AYO KITA COBA PAKE METHOD POP()
                                     #gak kayak method list yang lain pop() punnya return value heheheheh
                                     #jadi fungsi pop itu nge-remove item dari specified index
                                     #nah returnnya item/value yang diremove tersebut. jadi bisa kita manfaatin buat
                                     #bikin opsi prioritize task cuk
                try:
                    askOption4 = int(input('what task do you want to prioritize?(enter the task number) : '))
                    print('task before:')
                    for i in userTask:
                        print(i, end='\n')
                    print('task after:')
                    originalTask = userTask.pop(askOption4 - 1)
                    userTask.insert(0, originalTask)
                    for i in userTask:
                        print(i, end='\n')
                except IndexError:
                    print('input Invalid, you do not have that many tasks.')
                except ValueError:
                    print('Input invalid, you did not enter a number.')
            elif askMainMenu == 5: #
                try:
                    askOption5 = int(input('which task would you want to uptade the status?(enter the task number) : '))
                    task5 = userTask[askOption5 - 1] #harus bikin dedicated var biar kedetect sama try block yang diluar.
                    try:
                        status = ['completed', 'pending', 'cancelled']
                        for i in status:
                            print(i, end='\n')
                        askOption5_2 = int(input('what status would you want to give the task? (enter the status number) : '))
                        userTask[askOption5 - 1] = task5 + ' status: ' + status[askOption5_2 - 1] #baru dimasukin ke sini, walaupun nanti salah, kedetectnya kan duluan di atas.
                    except IndexError:
                        print('invalid input, that is not in the status list')
                    except ValueError:
                        print('invalid input, you did not enter a number.')
                except IndexError:
                    print('input invalid, you do not have that many tasks.')
                except ValueError:
                    print('Input invalid, you did not enter a number.')
            elif askMainMenu == 6: #
                del userTask[:]
                print(userTask)
            elif askMainMenu == 7: #
                break
        else:
            print('please choose a number between 1-7') #lu bikin kondisi if 1 <= askMainMenu <= 7: tapi gak ngedetect error ketika
                                                        #masukin something like 123? thats because you dont have/didnt write the fucking condition
                                                        #to handle something like that, ya lu harus nulis else-nya lah. lu mau ngapain kalo EMANG
                                                        #ADA situasi kek gitu? 
    except ValueError:
        print('input invalid')
