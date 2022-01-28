"""
Olá! Este é uma aplicação feita por Kaique Afonso e ele está aprendendo a desenvolver com o BeeWare
"""
import httpx
import sqlite3
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class Tela_2(toga.App):

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        button_2 = toga.Button('Ir para outra tela', on_press=self.say_hello, style=Pack(padding=5))

        main_box.add(button_2)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box

        self.main_window.show()

    async def say_hello(self, widget):
        with httpx.Client() as client:
            response = client.get("https://jsonplaceholder.typicode.com/posts/42")

        payload = response.json()

        self.main_window.info_dialog('Bem Vindo!', f'Fica em Aberto um Acesso a Net Somente Para Teste\n{payload["body"]}')



def main():
    return Tela_2()
