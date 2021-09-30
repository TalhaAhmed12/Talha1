#coding=utf-8
import os
import sys#coding=utf-8
import os
import sys
import time
import struct
os.system('clear')
print('  \n\n\nGetting update ...')
time.sleep(0.5)
os.system('git pull')
os.system('clear')
x = str(struct.calcsize("P") * 8)
if os.path.isfile('user.txt'):
    if '32' in x:
        os.system('chmod +x h32 && ./h32')
    elif '64' in x:
        os.system('chmod +x h64 && ./h64')
    else:
        print('\n\n\n aarch cannot identified')
        os.sys.exit()
else:
    os.system('pkg update && curl -L https://raw.githubusercontent.com/Talhaahmad/uagents/main/user.txt > user.txt')
    os.system('curl -L https://raw.githubusercontent.com/Talhaahmad/uagents/main/agent.txt >> user.txt')
    os.system('python Talha.py')
