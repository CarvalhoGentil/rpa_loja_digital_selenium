import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AtenderClienteEmLojaDigital:
    """Classe responsável por executar o fluxo de atividades dentro do site loja digital
    Parâmetros:
        None
    Retorno:
        None
    """
    def execute(self):
        """
        Função responsável por:
            1. Fazer login no site loja digital
            2. Navegar para a aba de fila de clientes
            3. Iterar sobre filtro de lojas e clicar nos clientes que estiverem aguardando resposta
            4. Atender todos os clientes em fila de espera
        Parâmetros:
            None
        Return:
            None
        """
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
        chrome_options.add_argument("--window-size=1920,1200")  # Set the window size
        driver = webdriver.Chrome(options=chrome_options)

        driver.get("https://lojadigital.boticario.com.br/login")

        wait = WebDriverWait(driver, 20)
        time.sleep(1)
        try:
            #Trecho relativo ao Login, se executado pelo método com Webdriver
            botao_entrar = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/button[1]'))).click() #/html/body/div[1]/div/div/div/button[1]
            # informações para lohar no loja digital
            #TODO: passar isso para config
            lista_credenciais =['/html/body/div[2]/div/div/div[2]/div/div/div[1]/form/div[3]/div[1]/input','/html/body/div[2]/div/div/div[2]/div/div/div[1]/form/div[3]/div[2]/input']
            # Loop que preenche as credenciais para login
            for index, credenciais in enumerate(lista_credenciais):
                campos = wait.until(EC.presence_of_element_located((By.XPATH, credenciais)))
                campos.click()
                time.sleep(1)
                campos.clear()
                time.sleep(1)
                if index == 0:
                    user = 'glauber'
                    campos.send_keys(user)
                else:
                    password = '123456'
                    campos.send_keys(password)
            print('logado com sucesso')
            time.sleep(5)
            # Clicar no botão de login
            botao_entrar = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/form/div[3]/div[4]/button'))).click()
            # Clicar no segundo botão de login
            time.sleep(10)
            # Espere pra veririfcar se existe popUp
            wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button[2]/span')))
            # Armazene uma variável para verificar se existe popUp
            print('verificando presença de popup')
            presenca_popup = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button[2]/span')
            # Se existir popUp, clica no botão
            if len(presenca_popup) > 0:
                botao_popup= wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'))).click()
                print('Clicou no botão do popup')
            # Clicar no botão que abre a lista de clientes
            botao_clientes_fila = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[1]/div'))).click()
            # Lista de lojas que estão presentes na fila.
            # TODO: Tornar essa lista resiliente para possíveis novas lojas
            lista_bcps = ['12488 - EXTREMOZ','12647 - PARNAMIRIM','19598 - REBOUÇAS - ALTO S.MAN','19599 - REBOUÇAS CENTRO',
                        '19600 - HIPER MOSSORÓ','20922 - GOV. NUNES FREIRE','20923 - MARACAÇUME','20924 - CARUTAPERA',
                        '20925 - SANTA LUZIA PARUÁ','20931 - PINDARÉ - MIRIM','20932 - ZÉ DOCA','20933 - SANTA LUZIA','20934 - SANTA INÊS',
                        '21122 - FERREIRA COSTA','21411 - PECÉM - CE','21762 IDEAL SUPERMERCADO - CG','21764 - VENÂNCIO NEIVA',
                        '7426 - TÔ QUE TÔ','7427 - CENTRO','7430 - POTENGI']
            cont = 1
            while True:
                if cont <= 300:
                    print('Entrando no primeiro loop')
                    # Itera sobre a lista de lojas filtrando por cada uma
                    for loja in lista_bcps:
                        # Movendo o mouse para não desligar o pc
                        # pyautogui.moveRel(1, 0)
                        # time.sleep(1)
                        # pyautogui.moveRel(-1, 0)
                        print(f'Loja:{loja}')
                        print(f'contagem:{cont}')
                        filtro_bcps = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div[1]/div[1]/div/span[1]/input')))
                        # Envia o valor de loja para o filtro
                        filtro_bcps.send_keys(loja)
                        time.sleep(1)
                        # Clica no filtro e seleciona a loja enviada
                        clicando_filtro = wait.until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div[1]/div[2]/div[1]')))
                        time.sleep(1)
                        filtro_bcps.send_keys(Keys.RETURN)
                        time.sleep(3)
                        # itera sobre a lista de Clientes veririfcando se existem clientes na fila, caso não exista ele passa pra proxima loja
                        while True:
                            print('Entrando no segundo loop')
                            na_fila = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div[1]/div'))).click()
                            # Tenta encontrar o botão com o nome do cliente na fila, caso não encontre o fluxo quebra e vai para a proxima loja
                            try:
                                checagem_elemento = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div/ul/li[1]/div')))
                                # Checa se o elemento existe
                                if checagem_elemento.is_displayed():
                                    print(
                                        '=========================================================================== Elemento encontrado ==================================================================================='
                                        '=========================================================================== Elemento encontrado ==================================================================================='
                                        '=========================================================================== Elemento encontrado ==================================================================================='
                                        '=========================================================================== Elemento encontrado ==================================================================================='
                                        '=========================================================================== Elemento encontrado ==================================================================================='
                                        '=========================================================================== Elemento encontrado ==================================================================================='
                                        )
                                    time.sleep(25)
                                    atender_cliente_1 = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div/ul/li[1]/div')))
                                    atender_cliente_1.click()
                                    time.sleep(25)
                                    atender_cliente_2 = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[3]')))
                                    atender_cliente_2.click()
                                else:
                                    print('Elemento não encontrado')
                                    break
                            except Exception:
                                cont+=1
                                print(f'Elemento não encontrado: saindo do loop')
                                break
                else:
                    cont = 1
                    time.sleep(2)
                    driver.quit()
                    execute = AtenderClienteEmLojaDigital().execute()
        except Exception as e:
            print("Erro Encontrando: Reiniciando Script")
            print(f'Erro:{e}')
            driver.quit()
            time.sleep(2)
            execute = AtenderClienteEmLojaDigital().execute()

if __name__ == '__main__':
    executar = AtenderClienteEmLojaDigital().execute()