from os import system, name
import json

title = 'My Repertoire:'
line = '#'*50

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def registerMusic():
    name = str(input('Enter song name: ')).strip().lower()
    note = str(input('Enter the tone of the song: ')).strip().upper()

    data = {
        "name": name,
        "note": note
    }

    while(True):
        print('[1] To Take')
        print('[2] Taken')

        opt = str(input('Option: ')).strip()

        if opt == '1' or opt == '2':
            break

    try:
        if opt == '1':
            with open('musics.json', 'r+') as file:
                file_data = json.load(file)
                file_data['songs_to_take'].append(data)
                file.seek(0)
                json.dump(file_data, file, indent=4)
        else:
            with open('musics.json', 'r+') as file:
                file_data = json.load(file)
                file_data['songs_taken'].append(data)
                file.seek(0)
                json.dump(file_data, file, indent=4)
        file.close()
        print('\nSuccessfully registered!')
    except:
        print('\nError when registering')

def findByName():
    print('Find by Name')

def findByNote():
    print('Find by Note')

def listMusics():
    while(True):
        print('[1] To Take')
        print('[2] Taken')
        print('[3] All')

        opt = str(input('Option: ')).strip()

        if opt == '1' or opt == '2' or opt == '3':
            break

    try:
        clear()
        if opt == '1':
            with open('musics.json', 'r') as file:
                file_data = json.load(file)
                print(file_data['songs_to_take'])
                
        elif opt == '2':
            with open('musics.json', 'r') as file:
                file_data = json.load(file)
                print(file_data['songs_taken'])
        else:
            with open('musics.json', 'r') as file:
                file_data = json.load(file)
                print("Songs Taken:")
                print(file_data['songs_taken'])
                print("\nSongs to Take:")
                print(file_data['songs_to_take'])
        input("\nPlease press a key to proceed")
        file.close()
    except:
        print('\nError when registering')

def removeMusic():
    print('Removed!')

while(True):
    while(True):
        clear()
        print(f'\n' + title.center(50))
        print(line)

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