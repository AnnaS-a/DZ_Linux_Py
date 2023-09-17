from checkers import ssh_checkout
from load import upload_file


def deploy():
    res = []
    upload_file('0.0.0.0', 'user2', '11', '/home/user/p7zip-full.deb', '/home/user2/p7zip-full.deb')
    res.append(ssh_checkout('0.0.0.0', 'user2', '11', 'echo' "11" | 'sudo -S dpkg -i /home/user2/p7zip-full.deb',
                            'Настраивается пакет'))
    res.append(ssh_checkout('0.0.0.0', 'user2', '11', 'echo' "11"
                            | 'sudo -S dpkg -s p7zip-full.deb', 'Status: install ok installed'))
    return all(res)


if deploy():
    print('success')
else:
    print('false')
    
