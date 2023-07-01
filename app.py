class NotPositiveError(UserWarning):
    pass


notes = []


def addNote():
    val = input("What do you wish to add:\n")
    notes.append(val)


def printNotes():
    print(notes)


def deleteNote():
    pass


while True:
    print("TODOLIST APP")
    print("Select What you want to do\n 1. Add a Todo\n 2. Delete a Todo\n 3. Print all Todo's")
    try:
        response = int(input('Input a number from 1-3: '))
        if response <= 0:
            raise NotPositiveError
        elif response == 1:
            addNote()
        elif response == 2:
            deleteNote()
        elif response == 3:
            printNotes()
        else:
            raise IndexError
    except ValueError:
        print("please input a numeric value")
    except NotPositiveError:
        print("Please input a positive number")
    except IndexError:
        print("Index out of range")
