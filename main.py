from os import system, name
import json

title = 'My Repertoire:'

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def registerMusic():
    while(True):
        print('[1] To Take')
        print('[2] Taken')
        print('[0] Back')

        opt = str(input('Option: ')).strip()

        if opt == '1' or opt == '2' or opt == '0':
            break
        else:
            print('Enter a valid option!\n')
    
    if opt == '0':
        return

    try:
        while (True):
            name = str(input('\nEnter song name: ')).strip().lower()
            if name == "":
                print('Enter a name!\n')
            else:
                clear()
                break

        data = { "name": name }
        if opt == '1':
            with open('musics.json', 'r+') as file:
                file_data = json.load(file)
                if data not in file_data['songs_to_take']:
                    file_data['songs_to_take'].append(data)
                    file.seek(0)
                    json.dump(file_data, file, indent=4)
                else:
                    print('\nThis song is already on the list!')
                    return
        else:
            while (True):
                note = str(input('Enter the tone of the song: ')).strip().capitalize()
                if note == '':
                    print('Enter a note!\n')
                else:
                    clear()
                    break     
            data = { "name": name, "note": note }
            with open('musics.json', 'r+') as file:
                file_data = json.load(file)
                if data not in file_data['songs_taken']:
                    file_data['songs_taken'].append(data)
                    file.seek(0)
                    json.dump(file_data, file, indent=4)
                else:
                    print('\nThis song is already on the list!\n')
                    return

        file.close()
        print('\nSuccessfully registered!')
    except:
        print('\nError when registering')
    
    input("\nPlease press enter to proceed")

def findByName():
    print('Find by Name')

def findByNote():
    print('Find by Note')

def listMusics():
    while(True):
        print('[1] To Take')
        print('[2] Taken')
        print('[3] All')
        print('[0] Back')

        opt = str(input('Option: ')).strip()

        if opt == '1' or opt == '2' or opt == '3' or opt == '0':
            break
        else:
            print('Enter a valid option!\n')

    if opt == '0':
        return

    try:
        clear()
        if opt == '1':
            with open('musics.json', 'r') as file:
                file_data = json.load(file)
                print(file_data['songs_to_take'])
                listNames(file_data)
                
        elif opt == '2':
            with open('musics.json', 'r') as file:
                file_data = json.load(file)
                listNamesAndNotes(file_data)
        else:
            with open('musics.json', 'r') as file:
                file_data = json.load(file)
                listAll(file_data)
        file.close()
    except:
        print('\nError when registering')
        input("\nPlease press enter to proceed")

def removeMusic():
    print('Removed!')

def listNamesAndNotes(file_data):
    clear()
    print('#'*70)
    head_name = 'NAME'
    head_note = 'NOTE'
    print('#',head_name.ljust(40),head_note.ljust(26)+'#')
    print('#'*70)

    for i in file_data['songs_taken']:
        n = i["name"].split()
        txt = f'# '+' '.join([j.capitalize() for j in n])
        print(f'{txt.ljust(43)}{i["note"].capitalize().ljust(26)}#')
        print('#'+'-'*68+'#')
    input("\n\nPlease press enter to proceed")

def listNames(file_data):
    clear()
    print('#'*50)
    head_name = 'NAME'
    print('#',head_name.ljust(47)+'#')
    print('#'*50)

    for i in file_data['songs_to_take']:
        n = i["name"].split() 
        txt = f'# '+' '.join([j.capitalize() for j in n])
        print(txt.ljust(49)+'#')
        print('#'+'-'*48+'#')
    input("\n\nPlease press enter to proceed")

def listAll(file_data):    
    print('#'*70)
    head_name = 'NAME'
    head_note = 'NOTE'
    print('#',head_name.ljust(40),head_note.ljust(26)+'#')
    print('#'*70)

    taken = file_data['songs_taken']
    to_take = file_data['songs_to_take']

    for i in taken:
        n = i["name"].split()
        txt = f'# '+' '.join([j.capitalize() for j in n])
        print(f'{txt.ljust(43)}{i["note"].capitalize().ljust(26)}#')
        print('#'+'-'*68+'#')

    for i in to_take:
        n = i["name"].split()
        txt = f'# '+' '.join([j.capitalize() for j in n])
        print(f'{txt.ljust(43)}{"-".ljust(26)}#')
        print('#'+'-'*68+'#')
    input("\n\nPlease press enter to proceed")

while(True):
    while(True):
        clear()
        print(f'{title.center(50)}\n{"#"*50}')

        print('[1] - Register Music')
        print('[2] - Find Music by Name')
        print('[3] - Find Music by Note')
        print('[4] - List Musics')
        print('[5] - Remove Music')
        print('[0] - Exit')

        opt = str(input('Option: ')).strip()
        clear()

        if opt == '0':
            print('BYE!')
            break

        elif opt == '1':
            registerMusic()

        elif opt == '2':
            findByName()

        elif opt == '3':
            findByNote()

        elif opt == '4':
            listMusics()

        elif opt == '5':
            removeMusic()

        else:
            print('Enter a valid option!')
    break