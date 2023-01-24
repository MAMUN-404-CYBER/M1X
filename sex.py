import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://facebook.com/groups/770617227293870/')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf MX-M1.py')
except:
    pass
os.system('rm -rf MX-M1.py')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('MX-M1.py'):
        os.system('curl -L https://github.com/MAMUN-404-CYBER/MX-M1/blob/main/MX-M1.py') 
        import RMXXD
        RMXXD.RM()
    else:
        import RMXXD
        RMXXD.RM()
        
elif bit == '32bit':
    exit('\033[1;31m\n Sorry System or 32bit device not supported ')
