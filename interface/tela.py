from PySimpleGUI import PySimpleGUI as sg
sg.theme('Reddit')
layout = [
    [sg.Text('usuario'),sg.input(key='usuario')],
    [sg.Text('senha'),sg.input(key='senha', password_char='*')],
    [sg.Checkbox('salvar? ')],
    [sg.Button('entrar')]
    
]
janela = sg.Window('loggin',layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'entrar':
        if valores['usuarios'] == 'jhonatan' and valores['senha']== '123456':
            print('bem vindo')
        