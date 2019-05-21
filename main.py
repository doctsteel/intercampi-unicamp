import requests
import datetime
import time



def cadastra_todos_dias():
  date = datetime.datetime.today()
  count = 2
  while count < 11:
    databus = (date + datetime.timedelta(days=count)).strftime('%d/%m/%Y')
    if ((date + datetime.timedelta(days=count))).weekday() < 5:
      
      payload_manha = {'reason_id': '12', 'date': databus, 'schedule_id': '1', 'action':'cadastrar'}
      
      payload_tarde ={'reason_id': '12', 'date':databus, 'schedule_id': '7', 'action':'cadastrar'}
      
      m = s.post('https://sistemas2.ft.unicamp.br/intercamp/reservations.php', data=payload_manha)
      
      t = s.post('https://sistemas2.ft.unicamp.br/intercamp/reservations.php', data=payload_tarde)
      
      if m.status_code == 200  and  t.status_code == 200: 
        print("agendado dia {} 7:30 e 16:30 com sucesso".format(databus))
        time.sleep(5)
      else:
        print("erro no dia{}".format(databus))
        print("erro numero {} de manhã".format(m.status_code))
        print("erro numero {} a tarde".format(t.status_code))
    else:
      print("{} é fim de semana, cabaço".format(databus))

    count+=1
    
      

user = input("Usuário do intercampi, por favor. \n")
pwd = input("Senha do intercampi, por favor. \n")

s = requests.Session()
print("Se logando...")

login = {'usuario':str(user), 'pass': str(pwd), 'action':'login'}
r = s.post('https://sistemas2.ft.unicamp.br/intercamp/login.php', data=login)

print(r.status_code)
print('Logado.')

print('Fazer o que agora?')

print('1 - preencher dez dias seguidos 7:30 e 16:30')
print('2 - preencher 7:30/16:30 do ultimo dia que foi disponibilizado (10 dias a partir de hoje)')
print('3 - deslogar')

a = input()
if a == '1':
  cadastra_todos_dias()
elif a == '2':
  pass
else:
  print("sem tempo irmão")


s.get('https://sistemas2.ft.unicamp.br/intercamp/logout.php')
print("deslogado.")
print("時間がない、兄貴")
quit()






