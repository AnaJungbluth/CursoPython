# Hashzap
# botao de iniciar chat
# popup para entrar no chat
# quando entrar no chat: (aparece para todo mundo)
    # a mensagem que você entrou no chat
    # o campo e o botão de enviar mensagem
# a cada mensagem que você envia (aparece para todo mundo)
    # Nome: Texto da Mensagem

import flet as ft
from datetime import datetime
from tkinter import Tk, Label, font

def main(pagina):
    texto = ft.Text("HashZap")

    def enviar_mensagem_tunel(mensagem):
        text_mensagem = ft.Text(mensagem)
        chat.controls.append(text_mensagem)

        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    hora_atual = datetime.now()
    format_hora_atual = hora_atual.strftime("%H:%M")

    def enviar_mensagem(evente):
        pagina.pubsub.send_all(f"{nome_usuario.value}\n {camp_mensagem.value} ""         "f"{format_hora_atual}")

        camp_mensagem.value = ""

        pagina.update()

    chat = ft.Column()
    camp_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar_men = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_camp_botao = ft.Row(
        [camp_mensagem,
         botao_enviar_men]
    )

    def entrar_chat(evento):
        popup.open = False
        pagina.remove(texto)
        pagina.remove(botao_iniciar)

        pagina.add(chat)
        pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")
        pagina.add(linha_camp_botao)
        
        pagina.update()

    titulo_popup = ft.Text("Bem vindo ao HashZap")
    nome_usuario = ft.TextField(label="Escreva se nome no chat", on_submit=entrar_chat)
    botao_chat = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=titulo_popup,
        content=nome_usuario,
        actions=[botao_chat]
    )

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True

        pagina.update()
    
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=abrir_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER)