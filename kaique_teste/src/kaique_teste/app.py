"""
Olá! Este é uma aplicação feita por Kaique Afonso e ele está aprendendo a desenvolver com o BeeWare
"""
import sqlite3
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import screen

#tela = screen.Tela_2()

class HelloWorld(toga.App):

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label('Nome: ', style=Pack(padding=(0, 0)))
        self.name_input = toga.TextInput(style=Pack(flex=1))
        cpf_label = toga.Label('CPF: ', style=Pack(padding=(0, 0)))
        self.cpf_input = toga.TextInput(style=Pack(flex=1))
        cidade_label = toga.Label('Cidade: ', style=Pack(padding=(0, 0)))
        self.cidade_input = toga.TextInput(style=Pack(flex=1))
        self.data_table = toga.Table(['Nome', 'CPF', 'Cidade'])

        name_box = toga.Box(style=Pack(direction=COLUMN, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)
        name_box.add(cpf_label)
        name_box.add(self.cpf_input)
        name_box.add(cidade_label)
        name_box.add(self.cidade_input)

        button = toga.Button('Salva', on_press=self.salvar_dados, style=Pack(padding=5))
        button2 = toga.Button('CHAMAR NOVA TELA', on_press=self.chamar_tela2, style=Pack(padding=5)) #<- CONNECTION WITH THE CALL NEW SCREEN FUNCTION
        main_box.add(name_box)
        main_box.add(button)
        main_box.add(button2)
        main_box.add(self.data_table)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.criar_banco()
        self.mostrar_dados()
        self.main_window.show()

    def salvar_dados(self, widget):
        nome = self.name_input.value
        cpf = self.cpf_input.value
        cidade = self.cidade_input.value
        try:
            conn = sqlite3.connect(self.paths.app/'teste.db')
            c = conn.cursor()
            c.execute("INSERT INTO clientes (nome, cpf, cidade) VALUES (?, ?, ?)", (nome, cpf, cidade))
            conn.commit()
            conn.close()
            self.main_window.info_dialog('Sucesso!', 'Cliente Cadastrado Com Sucesso!')
            self.name_input.value = ""
            self.cpf_input.value = ""
            self.cidade_input.value = ""
            self.mostrar_dados()
        except Exception as ERROR:
            self.main_window.info_dialog('ERROR', 'Cliente Já Cadastrado no sistema')

    def mostrar_dados(self):
        try:
            conn = sqlite3.connect(self.paths.app/'teste.db')
            c = conn.cursor()
            c.execute("SELECT nome, cpf, cidade FROM clientes")
            dados_lidos = c.fetchall()
            cont = 0
            for b in dados_lidos:
                nome = b[0]
                CPF = b[1]
                cidade = b[2]

                self.data_table.data.insert(cont, nome, CPF, cidade)

        except Exception as ERROR:
            print(ERROR)

    def criar_banco(self):
        try:
            conn = sqlite3.connect(self.paths.app/'teste.db')
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS clientes ( id INTEGER PRIMARY KEY AUTOINCREMENT,"
                      "nome VARCHAR(50) UNIQUE,"
                      "cpf  VARCHAR(11) UNIQUE,"
                      "cidade VARCHAR(50))")
            conn.commit()
            conn.close()
        except Exception as ERROR:
            print(ERROR)
            self.main_window.info_dialog('ERROR', f'{ERROR}')

    ################### FUNCTION THAT CALLS THE SCREEN #######################
    def chamar_tela2(self, widget):
        self.tela = screen.Tela_2()
    #    '''outer_box = toga.Box()
    #    self.second_window = toga.Window(title='Kaique Teste')
    #    self.windows.add(self.second_window)
    #    self.second_window.content = outer_box
    #    self.second_window.show()'''
    ##########################################################################


def main():
    return HelloWorld()
