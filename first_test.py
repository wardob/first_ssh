import paramiko

host = '1.1.3.1'
user = 'user'
secret = 'secret'
port = 22

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret, port=port)
stdin, stdout, stderr = client.exec_command('terminal length 0\n')
stdin.write('show ip int br')
stdin.write('\n')
stdin.flush()
output = stdout.readlines()
print (output)
#stdin, stdout, stderr = client.exec_command('show int status\n')
#stdin, stdout, stderr = client.exec_command('show running-config\n')
output = stdout.readlines()
client.close()
