import string
import PySimpleGUI as sg
import random

lowercaseChars = list(string.ascii_lowercase)
uppercaseChars = list(string.ascii_uppercase)
digits = list(string.digits)
symbols = list(string.punctuation)

def generatePasswords(charsList, lenPassword, quantity):
    passwords = []
    for number in range(quantity):
        password = ''
        while len(password) < lenPassword:
            char = random.choice(charsList)
            password += char
        passwords.append(password)

    return passwords
    

def main():
    sg.theme('DarkBlue')

    layout = [  [sg.Checkbox(text="Lowercase Letters", key = 'lowercaseLetters')],
                [sg.Checkbox(text="Uppercase Letters", key = 'uppercaseLetters')],
                [sg.Checkbox(text="Symbols", key = 'symbols')],
                [sg.Checkbox(text="Digits", key = 'digits')],
                [sg.Text('What is the length of your password?'), sg.InputText(key = 'lenpass')],
                [sg.Text('How many passwords would you like to generate?'), sg.InputText(key = 'quantity')],
                [sg.Button('Generate', key = 'generate'), sg.Button('Exit', key = 'exit')],
                [sg.Multiline(size=(80,20), key='MultiLine')] ]


    window = sg.Window('Window Title', layout)
    window.Title = 'Password Generator'

    charsList = []

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'exit': 
            break
        if values['lowercaseLetters'] == True:
            charsList += lowercaseChars
        if values['uppercaseLetters'] == True:
            charsList += uppercaseChars
        if values['digits'] == True:
            charsList += digits
        if values['symbols'] == True:
            charsList += symbols
        if values['lowercaseLetters'] == False and values['uppercaseLetters'] == False and values['digits'] == False and values['symbols'] == False:
            sg.Popup('Hey user you have to choose what characters you want on your password so that we are able to generate one!', title='ERROR')
        elif values['lenpass'] == '' or values['quantity'] == '':
            sg.Popup('Hey user we are unable to generate a password without you telling us the length of the passwords and how many you want to generate!', title='ERROR')
        else:
            lenPassword = int(values['lenpass'])
            quantityPasswords = int(values['quantity'])

            passwords = generatePasswords(charsList, lenPassword, quantityPasswords)
            for index in range(len(passwords)):
                window['MultiLine'].update(passwords[index]+"\n", text_color_for_value='DarkBlue', append=True)
    

    window.close()


if __name__ == '__main__':
    main()