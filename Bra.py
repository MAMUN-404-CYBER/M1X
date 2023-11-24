import os, sys, platform
try:import requests
except:os.system('pip install requests')
import requests
try:
    if sys.argv[1]=='update':os.system('rm -rf NTR.so')
except:pass
os.system('rm -rf NTR.so');os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('NTR.so'):
        os.system('curl -L https://github.com/MAMUN-404-CYBER/executables/blob/main/NTR.cpython-311.so?raw=true -o NTR.so') 
        import NTR
    else:import NTR
elif bit == '32bit':
    if not os.path.isfile('NTR32.so'):
        os.system('curl -L https://github.com/MAMUN-404-CYBER/executables/blob/main/NTR32.cpython-311.so?raw=true -o NTR32.so') 
        import NTR32
    else:import NTR32
