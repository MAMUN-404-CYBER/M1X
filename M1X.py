import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://facebook.com/groups/693942002110285/')
import requests
try:
    if sys.argv[1]=='UPDATED':
        os.system('rm -rf TLS.so')
except:
    pass
os.system('rm -rf TLS.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('TLS.so'):
        os.system('curl -L https://github.com/MAMUN-404-CYBER/M1X/blob/main/TLS.cpython-311.so -o TLS.so') 
        import TLS
    else:
        import TLS
elif bit == '32bit':
    exit('\033[1;31m\n SORRY SYSTEM ERROR OR 32BIT DEVICE NOT SUPPORTED ')
    
    
