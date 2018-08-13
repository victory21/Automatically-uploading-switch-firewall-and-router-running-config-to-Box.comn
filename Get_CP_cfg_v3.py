from boxsdk import JWTAuth
from boxsdk import Client
import netmiko
from netmiko import ConnectHandler
import datetime

# Configure JWT auth object
sdk = JWTAuth(
  client_id="pi4s33hjb67dp1fiqeb8redy5j7ovosu",
  client_secret="GKtOuTOMuQCHY2SH0bx0sDs6l7VGC47u",
  enterprise_id="62450315",
  jwt_key_id="0jntyc9m",
  rsa_private_key_file_sys_path="C:\\cygwin64\\home\\Victor\\private.json",
  rsa_private_key_passphrase='password'.encode()
)
client = Client(sdk)

def runner(ipp, u_name, p_word, s_word):
    ssh_connection = ConnectHandler(
        device_type='linux',
        ip=ipp,
        username=u_name,
        password=p_word,
        secret=s_word
    )

    ssh_connection.enable()
    ssh_connection.send_command("clish")
    print ("clish worked")
    result = ssh_connection.find_prompt() + "\n"

    result += ssh_connection.send_command("sh run", delay_factor=2)

    ssh_connection.disconnect()

    #print(result)
    return result

today=str(datetime.date.today())

#runner('10.0.2.5','admin','password','sh run')

try:
    the_stuff=runner('10.0.2.5','admin','password','password')
    name=the_stuff.split('\n')[0]+today+'.txt'
    file =open('transitory.txt','w')
    file.write(the_stuff)
    file.close()
    #print('yeet')

    

    box_file = client.folder('0').upload('C:\\Python36-32\\transitory.txt', name)
except:
    print('sarry')

