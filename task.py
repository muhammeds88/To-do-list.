name = input('Enter your name: ')
greeting = f"Hello! Good Morning {name} how are you..\n"
print(greeting.capitalize())

ready = input('Are you ready for writing your daily tasks?(y or n)...')
if ready == 'n':
    print('You can write your tasks on the next section..')
    quit()

if ready != 'y':
    print("Wrong choice\nTry agin...")
    quit()

todays_tasks = []
tomorrow_tasks = []
day_after_tomorrow_tasks = []

print("\nEnter your Today's Tasks.")
print("If you wanna Quit, Enter 'q'.\n")

while True:
    task = input("Enter your Today's Task here: ")
    if task == 'q':
        print("\nYour Today's Task are: ")
        for i, task in enumerate(todays_tasks, start=1):
            print("You want to ", task)
        break
    todays_tasks.append(task)

choice = input('\nDo you want to write your Tomorrows Tasks? (y or n) ').lower()

if choice == 'n'.lower():
    print("\nToday's Task's are.")
    for i, task in enumerate(todays_tasks, start=1):
        print("You want to ", task)
    quit

elif choice == 'y'.lower():
    print('Enter your Tomorrows Tasks: \n')

    while True:
        task2 = input("Enter your Tomorrow's Task here: ")
        if task2 == 'q':
            print("\nToday's Tasks:")
            for i, task in enumerate(todays_tasks, start=1):
                print("You want to ", task)

            print("\nTomorrow's Task are: ")
            for i, task2 in enumerate(tomorrow_tasks, start=1):
                print("You want to ", task2)

            break
        tomorrow_tasks.append(task2)

choice2 = input("\nDo you want to enter day after Tomorrow's Task's (y or n) ").lower()

if choice2 == 'n'.lower():
    print("\nYour today's tasks are: \n")

    for i, task in enumerate(todays_tasks, start=1):
        print("You want to ", task)

    print("Your tomorrows tasks are: \n")

    for i, task2 in enumerate(tomorrow_tasks, start=1):
        print("You want to ", task2)


elif choice2 == 'y'.lower():
    print("\nEnter your Day After Tomorrow's Tasks\n")

    while True:
        task3 = input("Enter your Day After Tomorrow's Tasks here: ")
        if task3 == 'q':
            print("\nToday's Tasks: ")

            for i, task in enumerate(todays_tasks, start=1):
                print("You want to ", task)

            print("\nTomorrow's Tasks: ")
            for i, task2 in enumerate(tomorrow_tasks, start=1):
                print("You want to ", task2)

            print("\nDay After Tomorrow's Tasks: ")
            for i, task3 in enumerate(day_after_tomorrow_tasks, start=1):
                print("You want to ", task3)

            break
        day_after_tomorrow_tasks.append(task3)

print('\r')
print("Your task have been updated!")
