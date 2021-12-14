from ClienteView import ClienteView
from Cliente import Cliente
import PySimpleGUI as sg


class ClienteController:
    def __init__(self):
        self.__telaCliente = ClienteView(self)
        self.__clientes = {}  # lista de objetos Cliente

    def inicia(self):
        self.__telaCliente.tela_consulta()

        # Loop de eventos
        rodando = True
        resultado = ''
        while rodando:
            event, values = self.__telaCliente.le_eventos()

            if event == sg.WIN_CLOSED:
                rodando = False

            elif event == 'Cadastrar':
                nome = values['nome'].strip()
                codigo = values['codigo']
                if nome != '' and codigo != '':
                    resultado = self.adiciona_cliente(codigo, nome)
                else:
                    resultado = 'Preencha todos os campos'

            elif event == 'Consultar':
                nome = values['nome'].strip()
                codigo = values['codigo']
                if codigo != '' and nome == '':
                    resultado = self.busca_codigo(codigo)
                elif codigo == '' and nome != '':
                    resultado = self.busca_nome(nome)
                elif codigo != '' and nome != '':
                    resultado = 'Por favor, digite em apenas um campo'
                else:
                    resultado = 'Por favor, digite em um dos campos'

            if resultado != '':
                dados = str(resultado)
                self.__telaCliente.mostra_resultado(dados)

        self.__telaCliente.fim()

    def busca_codigo(self, codigo):
        if codigo.isnumeric():
            codigo = int(codigo)
            try:
                return self.__clientes[codigo]
            except:
                return 'Código não encontrado'
        else:
            return 'Por favor, digite apenas números'

    # cria novo OBJ cliente e adiciona ao dict
    def adiciona_cliente(self, codigo, nome):
        try:
            codigo = int(codigo)
        except:
            return 'Por favor, digite apenas números inteiros'
        if codigo not in self.__clientes.keys():
            self.__clientes[codigo] = Cliente(codigo, nome)
            return f'{nome}: {codigo} cadastrado com sucesso'
        else:
            return 'Esse código já está em uso'

    def busca_nome(self, nome):
        for key, val in self.__clientes.items():
            if val.nome == nome:
                return self.__clientes[key]

        return 'Nome não encontrado'
