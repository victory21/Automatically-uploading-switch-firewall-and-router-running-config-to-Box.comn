from boxsdk import JWTAuth
from boxsdk import Client
import paramiko
import time

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

#file_path = 'C:\\Users\\Victor\\Documents\\transition.txt'
#file_name = 'transition.txt'
#folder_id = '0'

#box_file = client.folder(folder_id).upload(file_path, file_name)

#box_file = client.folder(folder_id).upload(file_path)

#box_file = client.folder('0').upload('C:\\Users\\Victor\\Documents\\language.txt')


def runner(ip, u_name, p_word, komand):
    ssh= paramiko.SSHClient()
    #print("hi")
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=22, username=u_name, password=p_word, timeout=10)

    remote_conn = ssh.invoke_shell()
    remote_conn.send("en")
    remote_conn.send("\n")
    
    remote_conn.send("password\n")
    remote_conn.send("\n")

    remote_conn.send(komand)
    remote_conn.send("\n")
    time.sleep(10)
    output = remote_conn.recv(65535)
    
    print(output)
    #stdin, stdout, stderr =ssh.exec_command(komand)
    #output=stdout.readlines()
    return output

runner('10.0.2.5','admin','password','sh run')

'''try:
    the_stuff=runner('10.0.2.5','admin','password','sh run')
    file =open('transitory.txt','w')
    file.write('\n'.join(the_stuff))
    file.close()
    print('yeet')

   # box_file = client.folder('0').upload('C:\\Python36-32\\transitory.txt', "litt")
except:
    print('sarry')
'''
