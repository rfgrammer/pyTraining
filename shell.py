#! /usr/bin/python3

import os

myhome = os.environ.get('HOME')
os.chdir(os.path.join(myhome, 'Downloads'))
print(os.getcwd())

# install nano
app = 'nano'
os.system('sudo apt-get -y install '), app

# install wget
os.system('sudo apt-get install wget')

# install latest PyCharm
filename = 'pycharm-community-2016.2.3.tar.gz'
os.system('wget https://download.jetbrains.com/python/' + filename)
os.system('tar -xf ' + filename + ' -C .')
os.chdir('/home/charles/Downloads/' + filename.replace('.tar.gz', ''))

# create PyCharm2 folder
if os.path.exists('/opt/PyCharm2'):
    pass
else:
    os.system('sudo mkdir /opt/PyCharm2')

os.system('sudo cp -R * /opt/PyCharm2')
os.chdir('/opt/PyCharm2/bin')
os.system('sh pycharm.sh')
