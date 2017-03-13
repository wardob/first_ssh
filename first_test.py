import argparse
import paramiko



def main(host, port, user, secret):
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


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("host")
    parser.add_argument("port")
    parser.add_argument("user")
    parser.add_argument("password")

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = get_args()
    main(args.host, args.port, args.user, args.password)


