import requests, time, json
import datetime
from datetime import date, timedelta, datetime
import pandas as pd

from const_loja_digital import URL_LOJA_DIGITAL,\
HEADERS_LOJA_DIGITAL_REDIRECT,\
URL_LOGIN_LOJA_DIGITAL,\
PAYLOAD_LOGIN,\
PAYLOAD_GRPH,\
URL_REFEREER,\
HEADERS_LOGIN,\
HEADER_GHRP,\
QUERY_PARMS,\
URL_CONFIRM,\
HEADER_GRAPH_LOGIN,\
PAYLOAD_FIRESTORE_REQUEST,\
HEADER_FIRESTORE_REQUEST,\
PAYLOAD_FIRESORE_SID,\
HEADER_FIRESTORE_SID,\
HEADER_FIRESTORE_GET
class BomDiaCliente:
    """
        Essa classe tem por finalidade:
        1. Realizar o login no site consultora digital
        2. Naegar até a página com todas as lojas
        3. Clicar no clinete que está esperando resposta
        4. Clicar em responder
        5. enviar uma resposta automatática
    """
    def execute(self):
        """ Realiza o fluxo de atividades da classe """

        session, acces_token = self.realizando_login_loja_digital()

        self.pagina_envio_mensagem(session, acces_token)

    def realizando_login_loja_digital(self):
        """
        Método responsável por realizar o login no site loja digital
        """
        # Criando uma sessão requests
        session = requests.Session()
        # Obtendo o token de autenticação para logar no site
        response = session.get('https://lojadigital.boticario.com.br/login')

        # Extraindo autorization
        authorization_code = response.text.split('"authorizePath":"')[1].split('"')[0]

        # Extraindo ClientID
        client_id = response.text.split('"clientId":"')[1].split('"')[0]

        # Construindo a URL_LOJA_DIGITAL_ATUALIZADA
        URL_LOJA_DIGITAL_ATUALIZADA = URL_LOJA_DIGITAL.format(authorization_code=authorization_code,client_id=client_id)

        # Navegando ate a url de login
        response = session.get(URL_LOJA_DIGITAL_ATUALIZADA,headers=HEADERS_LOJA_DIGITAL_REDIRECT)

        # Verificando se houve erro
        if response.status_code != 200:
            raise Exception(f'Erro ao realizar o redirecionamento para o site. Status code: {response.status_code}')

        # Extraindo o tenantId
        tenantId = response.text.split('"tenant":"')[1].split('"')[0]

        # Extraindo transId
        transId = response.text.split('"transId":"')[1].split('"')[0]

        # Extraindo Csrf-Token
        csrf = response.text.split('"csrf":"')[1].split('"')[0]

        # Construindo a URL_LOGIN_LOJA_DIGITAL_ATUALIZADA
        URL_LOGIN_LOJA_DIGITAL_ATUALIZADA = URL_LOGIN_LOJA_DIGITAL.format(tenantId=tenantId,transId=transId)

        # Armazenando valor da url como texto
        URL_REFEREER_ATUALIZADO = URL_REFEREER.format(authorization_code=authorization_code,client_id=client_id)

        # Adicioanndo os headers
        HEADERS_LOGIN['Referer'] = URL_REFEREER_ATUALIZADO
        HEADERS_LOGIN['X-Csrf-Token'] = csrf

        # Fazendo a arequisição POST para logar
        response = session.post(URL_LOGIN_LOJA_DIGITAL_ATUALIZADA,headers=HEADERS_LOGIN, data=PAYLOAD_LOGIN)

        # Verificando se houve erro
        if response.status_code != 200:
            raise Exception(f'Erro ao fazer requisição post para logar. Status code: {response.status_code}')

        # #Obtendo access_token
        QUERY_PARMS_ATALIZADA = QUERY_PARMS.format(csrf=csrf,transId=transId)
        confirm_url = URL_CONFIRM + QUERY_PARMS_ATALIZADA

        # Realizando a requisição  GET pra obter o acc-token
        response = session.get(confirm_url,headers=HEADERS_LOGIN)

        if response.status_code != 200:
            raise Exception(f'Erro ao fazer requisição get para obter o id_token. Status code: {response.status_code}')

        # Obter o access_token por meio da location
        id_token = response.url.split('id_token=')[1].split('&')[0]

        # Requisição POST para graphiql para obter o id_token do login
        url_login_acces_token = 'https://api-loja-digital.prd.grupoboticario.digital/auth/api/v1/auth/login'

        # Atribuindo o id_token ao payload criado somente para obter o access_token
        payload_acces_token = {'accessToken': id_token}

        # Obtendo response
        response = session.post(url_login_acces_token,headers=HEADER_GRAPH_LOGIN, json=payload_acces_token)

        if response.status_code != 201:
            raise Exception(f'Erro ao fazer requisição POST para obter o access_token. Status code: {response.status_code}')

        acces_token = response.text.split('"token":"Bearer ')[1].split('"')[0]

        return session, acces_token
    def pagina_envio_mensagem(self,session,acces_token):
        """
        Método responsável por enviar uma mensagem para todas as lojas
        Paramtros:
            session: Sessão do requests
            acces_token: token de acesso para extração e atualização dos parâemtros das lojas
        Return:
            None
        """
        # url para encontrar o SID
        url = 'https://firestore.googleapis.com/google.firestore.v1.Firestore/Listen/channel?database=projects/loja-digital-344318/databases/(default)&VER=8&RID=3285&CVER=22&X-HTTP-Session-Id=gsessionid&$httpHeaders=X-Goog-Api-Client:gl-js/ fire/8.10.0 Content-Type:text/plain X-Firebase-GMPID:1:904136709224:web:3cb18a2fda09cafdc117dd Authorization:{acces_token}&zx=l7o98xwgg8ir&t=1'

        # Realizando a requisição GET
        response = session.post(url,headers=HEADER_FIRESTORE_REQUEST, data=PAYLOAD_FIRESTORE_REQUEST)
        
        sid = response.text.split('["c","')[1].split('"')[0]
        
        url_sid = 'https://firestore.googleapis.com/google.firestore.v1.Firestore/Listen/channel?database=projects/loja-digital-344318/databases/(default)&VER=8&gsessionid=GEts-YmKprNsVAMfnQ097Q9LK4_gmqKLWSjsqEzL6b0&SID={sid}&RID=3287&AID=15&zx=tueu6vg6868&t=1'
        
        response = session.post(url_sid,headers=HEADER_FIRESTORE_SID, data=PAYLOAD_FIRESORE_SID)
        url_get = 'https://firestore.googleapis.com/google.firestore.v1.Firestore/Listen/channel?database=projects/loja-digital-344318/databases/(default)&gsessionid=GEts-YmKprNsVAMfnQ097Q9LK4_gmqKLWSjsqEzL6b0&VER=8&RID=rpc&SID={sid}&AID=0&TYPE=xmlhttp&zx=6h19tg5nh993&t=1'
        response = session.get(url_get,headers=HEADER_FIRESTORE_GET)
atualizar_missao = BomDiaCliente().execute()