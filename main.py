from os import system, name
import json

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def registerMusic():
    print(f"{'Register Music:'.center(50)}\n{'#'*50}")
    print('[1] To Take')
    print('[2] Taken')
    print('[0] Back')
    while(True):
        opt = str(input('Option: ')).strip()

        if opt == '1' or opt == '2' or opt == '0':
            break
        else:
            print("Enter a valid option!\n")
    
    if opt == '0':
        return

    while (True):
        name = str(input("\nEnter song name: ")).strip().lower()
        if name == "":
            print("Enter a name!\n")
        elif name == '0':
            return
        else:
            break

    try:
        with open('musics.json', 'r+') as file:
            file_data = json.load(file)
            if opt == '1':
                music_list = file_data['songs_to_take']
                data = { "name": name }
            else:
                music_list = file_data['songs_taken']
                while (True):
                    note = str(input('Enter the tone of the song: ')).strip().capitalize()
                    if note == '0':
                        return
                    elif note == '' or note.isnumeric():
                        print("Enter a valid note!\n")
                    else:
                        clear()
                        data = { "name": name, "note": note }
                        break
                
            if data not in music_list:
                music_list.append(data)
                file.seek(0)
                json.dump(file_data, file, indent=4)
            else:
                file.close()
                print("\nThis song is already on the list!")
                input("\nPlease press enter to proceed")
                return

        file.close()
        print("\nSuccessfully registered!")
    except:
        print("\nError when registering")
    
    input("\nPlease press enter to proceed")
    clear()
    registerMusic()

def findByName():
    print(f"{'Find Music by Name:'.center(50)}\n{'#'*50}")
    print("[0] Back\n")
    while (True):
        name = str(input('Enter the music name: ')).strip().lower()
        if name == '0':
            return
        elif name == '' or name in "#{}[]":
            print("Enter a valid name!\n")
        else:
            clear()
            break

    try:
        with open('musics.json', 'r') as file:
            data_file = json.load(file)
            taken = data_file['songs_taken']
            to_take = data_file['songs_to_take']
            music_list = {"songs_taken": [], "songs_to_take": []}

            for i in taken:
                if name in str(i['name']):
                    music_list['songs_taken'].append(i)

            for i in to_take:
                if name in str(i['name']):
                    music_list['songs_to_take'].append(i)
        file.close()
        listAll(music_list)

    except:
        print('Error')

def findByNote():
    print(f"{'Find Music by Note:'.center(50)}\n{'#'*50}")
    print("[0] Back\n")
    while (True):
        note = str(input('Enter the note: ')).strip().capitalize()
        if note == '0':
            return
        elif note == '' or note.isnumeric():
            print("Enter a valid note!\n")
        else:
            clear()
            break
    try:
        with open('musics.json', 'r') as file:
            file_data = json.load(file)
            data = file_data['songs_taken']

            if note in str(data):
                music_list = {"songs_taken": []}

                for i in data:
                    if i['note'] == note:
                        music_list['songs_taken'].append(i)

                listNamesAndNotes(music_list)
                file.close()
            else:
                file.close()
                print('No results found!')
                input("\nPlease press enter to proceed")
    except:
        print('Error!')
        input("\nPlease press enter to proceed")

def listMusics():
    while(True):
        print(f"{'List Musics:'.center(50)}\n{'#'*50}")
        print('[1] To Take')
        print('[2] Taken')
        print('[3] All')
        print('[0] Back')

        opt = str(input('Option: ')).strip()

        if opt == '1' or opt == '2' or opt == '3' or opt == '0':
            break
        else:
            print("Enter a valid option!\n")

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
        print("\nError when registering")
        input("\nPlease press enter to proceed")
    clear()
    listMusics()

def removeMusic():
    clear()
    print(f"{'Remove Music:'.center(50)}\n{'#'*50}")
    print('[1] To Take')
    print('[2] Taken')
    print('[0] Back')

    while(True):
        opt = str(input('Enter the option: ')).strip()

        if opt == '0':
            return
        elif opt == '1' or opt == '2':
            break
        else:
            print("Enter a valid option!\n")

    while(True):
        name = str(input("\nEnter the song name: ")).strip().lower()
        if name == '0':
            return
        elif name != "":
            break
        else:
            print('Invalid name!')

    try:
        with open('musics.json', 'r') as file:
            data_file = json.load(file)
            if opt == '1':
                data = data_file['songs_to_take']
            else:
                data = data_file['songs_taken']

            if name in str(data):
                for i, element in enumerate(data):
                    if element['name'] == name:
                        data.pop(i)
                file.close()
                
                with open('musics.json', 'w') as file:
                    json.dump(data_file, file, indent=4)
                file.close()    

                print("\nSong removed!")
            else:
                print("\nMusic not found!")
    except:
        print("\nError!")

    input("\nPlease press enter to proceed")
    removeMusic()

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

def main():
    while(True):
        while(True):
            clear()
            print(f"{'My Repertoire'.center(50)}\n{'#'*50}")

            print('[1] - Register Music')
            print('[2] - Find Music by Name')
            print('[3] - Find Music by Note')
            print('[4] - List Musics')
            print('[5] - Remove Music')
            print('[0] - Exit')

            opt = str(input('Option: ')).strip()
            clear()

            if opt == '0':
                print("BYE!\n")
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

        break

main()