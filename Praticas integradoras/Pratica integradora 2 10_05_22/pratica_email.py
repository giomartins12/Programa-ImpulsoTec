import mysql.connector
from mysql.connector import Error
import win32com.client as win32
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import datetime
import email.message
import ssl
import time


def enviar_email():
    anexo = 'C:\\Users\\giovanni.martins\\teste.txt'
    corpo_email = """
    <p>Olá!</p>
    <p>Segue as respostas das perguntas do passo 4 do</p>
    <p>projeto integrador 10/05/2022</p>
    <p><b>a) - Sobre seu aplicativo, em qual outra aplicação você integraria este sistema de envio de e-mails?<b></p>
    <p>R - Aplicaria meu sistema em um aplicativo de controle e comunicação de funcionarios onde é possivel<p>
    <p>cadastrar e enviar informações, documentos ou até mesmo uma confirmação de cadastro.</p>
    <p><b>b) - Quais recursos você gostaria de incorporar ao seu programa de envio de e-mails?</p>
    <p>R - Implementaria o recurso de consulta, alteração e exclusão de cadastro</p> 
    <p>além de poder concatenar dados do Banco de dados e enviar por email.</p>
    <p><b>c) - Sobre a pergunta anterior, apresente a forma que utilizaria para incorporar um novo</p>
    <p><b>recurso neste programa.<p>
    <p>R - Realizaria as alterações e exclusões através de comandos SQL (SELECT, UPDATE E DELETE) via Python</P>
    <p><b>d) - Qual temática da primeira semana de estudos você mais utilizou nesta atividade?</p>
    <p>R - Utilizei mais os conceitos de algoritimos e estruturas de dados com a linguagem de programação Python</p>
    <p><b>e) - Faça um breve relato de sua experiência, e ao final compartilhe conosco o seguinte: você,</p>
    <p><b>ensinaria alguém a fazer esta atividade?</p>
    <p>R - Consegui aplicar varios ensinamentos e tecnicas vistas e realizadas durante o estudo das disciplinas.</p>
    <p>Adicionei elementos de acesso ao banco de dados e tive como obstáculo o codigo para envio de email</p>
    <p> que não foi mostrado e ensinado nas aulas. Porem, com a pratica tive a oportunidade de aprender novas</p>
    <p> técnicas e aprimorar as que já tinha aprendido</p> 
    """

    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition', f'attchment; filename=teste.txt')
    msg = email.message.Message()
    msg['Subject'] = "Projeto Integrador 2 "
    msg['From'] = 'email@gmail.com'
    msg['To'] = 'email@gmail.com'
    password = '<senha>'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Aguarde, enviando email...')
    time.sleep(3)
    print('Email enviado com sucesso!')

print("\nIniciando a conexão com banco de dados...\n")
time.sleep(3)
try:
        db_connection = mysql.connector.connect(host='localhost', user='user', password='senha',
                                                database='data_base_name')
        print("Banco de dados conectado!\n")
        time.sleep(3)
        #os.system('cls') or None
except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Banco de dados não existe!")
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Login ou senha incorretos!")
        else:

            print(error)
else:


    cursor = db_connection.cursor()
    inf_nome = input("Digite o nome: ")
    inf_empresa = input("Digite a empresa: ")
    inf_cargo = input("Digite o cargo: ")
    inf_email = input("Digite o email: ")
    menu = (f'{inf_nome}', f'{inf_empresa}', f'{inf_cargo}', f'{inf_email}', )
    sql = "INSERT INTO tbl_email (nome, empresa, cargo, email) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, menu)
    db_connection.commit()
    cadastro = cursor.lastrowid


print("Foi cadastrado o novo usuario de id: ", cadastro)
time.sleep(2)
selecao = "SELECT * FROM tbl_email"
cursor.execute(selecao)
resultado = cursor.fetchall()
selecao_email = "SELECT email FROM tbl_email"
cursor.execute(selecao_email)
resultado_email = cursor.fetchall()
cursor.close()
db_connection.close()

for result in resultado:
    print("Usuario cadastrado: ", result)
time.sleep(2)
enviar_email()
for email in resultado_email:
    print("email enviado: ", email)
