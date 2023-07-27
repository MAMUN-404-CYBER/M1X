import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://facebook.com/groups/693942002110285/')
import requests
try:
    if sys.argv[1]=='UPDATED':
        os.system('rm -rf RMXXD.so')
except:
    pass
os.system('rm -rf RMXXD.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('RMXXD.so'):
        os.system('curl -L https://github.com/ROX-CYBER/executables/blob/main/RMXXD.cpython-311.so?raw=true -o RMXXD.so') 
        import RMXXD
    else:
        import RMXXD
elif bit == '32bit':
    exit('\033[1;31m\n SORRY SYSTEM ERROR OR 32BIT DEVICE NOT SUPPORTED ')
    
    
