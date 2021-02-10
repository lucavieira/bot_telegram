import requests
import json

class telegramBot:
    def __init__(self):
        token = '1681407181:AAGx6P7BthClqNHZcW27j2rGkvQxD13Eyvs'
        self.url_base = f'https://api.telegram.org/bot{token}/'

    #Iniciar Bot
    def iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obterMensagens(update_id)
            mensagens = atualizacao['result']
            if mensagens:
                for mensagem in mensagens:
                    update_id = mensagem['update_id']
                    chat_id = mensagem['message']['from']['id']
                    resposta = self.criarResposta()
                    self.responder(resposta, chat_id)
    #Obter Msgs
    def obterMensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)
    #Criar Resposta
    def criarResposta(self):
        return 'Olá bem - vindo ao grupo'
    #Responder
    def responder(self, resposta, chat_id):
        link_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_envio)


bot = telegramBot()
bot.iniciar()
