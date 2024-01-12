# Get user's name input
name = input('Enter your name: ')

# Greeting message using user's name
greeting = f"Hello! Good Morning {name} how are you..\n"
print(greeting.title())

# Check if the user is ready to write daily tasks
ready = input('Are you ready for writing your daily tasks? (y or n)...')

# Handle user responses for readiness
if ready == 'n':
    print('You can write your tasks in the next section..')
    quit()

if ready != 'y':
    print("Wrong choice\nTry again...")
    quit()

# Lists to store tasks for today, tomorrow, and day after tomorrow
todays_tasks = []
tomorrow_tasks = []
day_after_tomorrow_tasks = []

# Input today's tasks and handle quitting
print("\nEnter your Today's Tasks.")
print("If you wanna Quit, Enter 'q'.\n")

while True:
    task = input("Enter your Today's Task here: ")
    if task == 'q':
        # Display today's tasks
        print("\nYour Today's Task are: ")
        for i, task in enumerate(todays_tasks, start=1):
            print("You want to ", task)
        break
    todays_tasks.append(task)

# Check if user wants to input tomorrow's tasks
choice = input('\nDo you want to write your Tomorrow\'s Tasks? (y or n) ').lower()

if choice == 'n':
    # Display today's tasks and quit
    print("\nToday's Task's are.")
    for i, task in enumerate(todays_tasks, start=1):
        print("You want to ", task)
    quit()

elif choice == 'y':
    # Input tomorrow's tasks and handle quitting
    print('Enter your Tomorrow\'s Tasks: \n')
    while True:
        task2 = input("Enter your Tomorrow's Task here: ")
        if task2 == 'q':
            # Display today's and tomorrow's tasks
            print("\nToday's Tasks:")
            for i, task in enumerate(todays_tasks, start=1):
                print("You want to ", task)

            print("\nTomorrow's Task are: ")
            # Check if user wants to input day after tomorrow's tasks
            choice2 = input("\nDo you want to enter day after Tomorrow's Task's (y or n) ").lower()

            if choice2 == 'n':
                # Display today's and tomorrow's tasks and quit
                print("\nYour today's tasks are: ")
                for i, task in enumerate(todays_tasks, start=1):
                    print("You want to ", task)

                print("\nYour tomorrow's tasks are: ")
                for i, task2 in enumerate(tomorrow_tasks, start=1):
                    print("You want to ", task2)

            elif choice2 == 'y':
                # Input day after tomorrow's tasks and handle quitting
                print("Enter your Day After Tomorrow's Tasks\n")
                while True:
                    task3 = input("Enter your Day After Tomorrow's Tasks here: ")
                    if task3 == 'q':
                        # Display today's, tomorrow's, and day after tomorrow's tasks
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

            # Final message indicating task update
            print('\r')
            print("Your tasks have been updated!")

            for i, task2 in enumerate(tomorrow_tasks, start=1):
                print("You want to ", task2)

            break
        tomorrow_tasks.append(task2)

# Check if user wants to input day after tomorrow's tasks
choice2 = input("\nDo you want to enter day after Tomorrow's Task's (y or n) ").lower()

if choice2 == 'n':
    # Display today's and tomorrow's tasks and quit
    print("\nYour today's tasks are: ")
    for i, task in enumerate(todays_tasks, start=1):
        print("You want to ", task)

    print("\nYour tomorrow's tasks are: ")
    for i, task2 in enumerate(tomorrow_tasks, start=1):
        print("You want to ", task2)

elif choice2 == 'y':
    # Input day after tomorrow's tasks and handle quitting
    print("Enter your Day After Tomorrow's Tasks\n")
    while True:
        task3 = input("Enter your Day After Tomorrow's Tasks here: ")
        if task3 == 'q':
            # Display today's, tomorrow's, and day after tomorrow's tasks
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

# Final message indicating task update
print('\r')
print("Your tasks have been updated!")
