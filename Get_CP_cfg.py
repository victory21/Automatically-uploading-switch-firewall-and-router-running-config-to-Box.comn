from boxsdk import JWTAuth
from boxsdk import Client
import netmiko
from netmiko import ConnectHandler
import datetime

import threading
from threading import Thread

# Configure JWT auth object
sdk = JWTAuth(
  client_id="Qn6p8cio5i1nr93kzlyac70aj6xjprbw",
  client_secret="TMrbjJLq8Ek3kht8hGH9FAgZbOJkKaJl",
  enterprise_id="62977688",
  jwt_key_id="qun049ut",
  rsa_private_key_file_sys_path="C:\\cygwin64\\home\\User-12\\private_Jing.json",
  rsa_private_key_passphrase='#####Round'.encode()
)
client = Client(sdk)

def runner(ipp, u_name, p_word, s_word):
    ssh_connection = ConnectHandler(
        device_type='checkpoint_gaia',
        ip=ipp,
        username=u_name,
        password=p_word,
        #secret=s_word
    )
    result = ssh_connection.find_prompt() + "\n"
    result += ssh_connection.send_command('clish -c "show configuration"', delay_factor=4)

    result += ssh_connection.send_command('clish -c "fw getifs"', delay_factor=4)                 
    ssh_connection.disconnect()
    return result

today=str(datetime.date.today())

#loop of ip addresses
ip_list=["172.23.109.10"]
# ip_list=["172.23.109.7","172.23.109.8","172.23.109.9","172.23.109.10"]


#for x in range(0,len(ip_list)):
def sub_cmd(ip_add):
    try:
        the_stuff=runner(ip_add,'jshi695','!0725Round','password')
        tp_n=the_stuff.split('\n')[0]
        name=tp_n[tp_n.find('@')+1:tp_n.find(':')]+'_'+today+'.txt'
        file =open(name+'.txt','w')
        file.write(the_stuff)
        file.close()

        box_file = client.folder('0').upload('C:\\Python36\\MI\\'+name+'.txt', name)
    except:
        print('sarry')

if __name__ == '__main__':
    for x in range(0,len(ip_list)):
        Thread(target = sub_cmd(ip_list[x])).start()
