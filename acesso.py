# Modulo que acessa o Gmail.
# O endereço de email e a senha são informados pelo pelo usuario inputando as infromações
# Não há armazenamento de informações pessoais
import imaplib
import email
import getpass
import pandas as pd

# Acesso ao Gmail
enderecoEmail = input('Insira o endereço de Email: ')
senhaEmail = input('Insira a senha do email: ')
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(enderecoEmail, senhaEmail)

# Lista de emails
print(mail.list())
mail.select("inbox")

# Produzindo lista de emails
result, numbers = mail.uid('search', None, "ALL")
uids = numbers[0].split()
uids = [id.decode("utf-8") for id in uids ]
uids = uids[-1:-100:-1]
result, messages = mail.uid('fetch', ','.join(uids), '(BODY[HEADER.FIELDS (SUBJECT FROM DATE)])')

# Criando lista de cada tipo de dados
date_list = []
from_list = []
subject_text = []

# Rotina para extrair os dados de cada email no inbox
for i, message in messages[::2]:
    msg = email.message_from_bytes(message)
    decode = email.header.decode_header(msg['Subject'])[0]
    if isinstance(decode[0],bytes):
        decoded = decode[0].decode()
        subject_text.append(decoded)
    else:
        subject_text.append(decode[0])
    date_list.append(msg.get('date'))
    fromlist = msg.get('From')
    fromlist = fromlist.split("<")[0].replace('"', '')
    from_list1 = []
    from_list1.append(fromlist)
# Cria um DataFrame basedo na Data
date_list = pd.to_datetime(date_list)
date_list1 = []
for item in date_list:
    date_list1.append(item.isoformat(' ')[:-6])
print(len(subject_text))
print(len(from_list))
print(len(date_list1))
dados = {'Date':date_list1, 'Sender':from_list, 'Subject':subject_text}
dados_texto = str(dados)
f = open('lista de emails.txt','a')
f.write(dados_texto)

