# Configura o gmail para habilitar o IMAP, diminuir o nivel de segurança para facilitar o acesso
# Utiliza o Selenium para fazer a configuração pelo navegador
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep

# Recebe do usuario o endereço de email e senha
enderecoEmail = input('Insira o endereço de Email: ')
senhaEmail = input('Insira a senha do email: ')

# Acessa o site Gmail
driver = webdriver.Chrome()
driver.get('https://www.gmail.com')
sleep(2)

# Identifica onde esta o campo de Username e preenche com os dados informados pelo usuario
acessoUsuario = driver.find_element_by_name('identifier')
acessoUsuario.send_keys(enderecoEmail)
clicaAvancar = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]')
clicaAvancar.click()
sleep(3)

# Identifica onde esta o campo Password e preenche  com os dados informados pelo usuario
campoSenha = driver.find_element_by_name('password')
campoSenha.send_keys(senhaEmail)
clickProsseguir = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
clickProsseguir.click()
sleep(3)

# Abre o menu de configuraçoes - Não tem necessidade
configMenu = driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[3]/div[1]/div[2]/div/a')
configMenu.click()
sleep(2)

# Vai na pagina de configuração da conta do Gmail
manageYourGoogleAccount = driver.get('https://myaccount.google.com/?utm_source=OGB&tab=mk&utm_medium=act&pli=1&gar=1')
sleep(2)
segurancaOpcao = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/c-wiz/div/div[1]/div[3]/c-wiz/nav/ul/li[4]/a')
segurancaOpcao.click()
sleep(3)
acessoAppMenosSeguros = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/c-wiz/div/div[3]/div/div/c-wiz/section/div[7]/article/div/div/div[3]/div[2]/a')
acessoAppMenosSeguros.click()
sleep(2)
permitirApp = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz[3]/div/div[3]/c-wiz/div/div[3]/div[1]/div/div/div/div[2]/div/div[3]/div')
permitirApp.click()
driver.close()