import PySimpleGUI as sg 

# View do padrão MVC
class ClienteView():
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__container = []
        self.__window = sg.Window("Consulta de clientes", self.__container ,font=("Helvetica", 14))

    def tela_consulta(self):
        sg.theme('Dark Brown 1')

        self.__container = [
            [sg.Text('Digite o código ou o nome do cliente e clieque na ação esperada:')],
            [sg.Text('Nome:', size=(10, 1)), sg.InputText('', key='nome')],
            [sg.Text('Código:', size=(10, 1)), sg.InputText('', key='codigo')],
            [sg.Button('Cadastrar'), sg.Button('Consultar')],
            [sg.Text('', key='status', size=(50, 1))]
        ]

        self.__window = sg.Window("Consulta de clientes", self.__container, font=("Helvetica", 14))

    def mostra_resultado(self, resultado): 
        self.__window.Element('status').Update(resultado)

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()
