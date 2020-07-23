#mau recode ya?
#Silahkan, saya iklas:)
import os,sys,time,itertools,threading
from time import sleep

def bersih():
  os.system('clear')

def ldb():
  for x in range(101):
      time.sleep(0.1)
      print(f'\r\33[32;1m[!] Penginstalan bahan {x}%', end='', flush=True)

def trojantnp():
  print('')
  no = input('\33[31;1m[\33[32;1m•\33[31;1m] \33[36;1mMasukkan nomer target:\33[1;33m ')
  lan1 = input('\33[31;1m[\33[32;1m•\33[31;1m] \33[36;1mApakah anda yakin untuk melanjutkan? [y/t]:\33[1;33m ')
  if lan1 == 'y':
     sleep(1)
     print('')
     print('\33[31;1m[!] Mencari Target!')
     sleep(2)
     print('\33[32;1m[!] Target Ditemukan')
     print('')
     sleep(3)
     print('\33[31;1m[!] Menyiapkan bahan')
     sleep(2)
     ldb()
     print('\33[37;1m')
     print('')
     sleep(1)
     print('\33[31;1mTrojan akan di kirim dalam 5 detik lagi!')
     sleep(2)
     print('Trojan siap dikirim')
     sleep(3)
     while True:
        print('\33[31;1mTrojan sukses terkirim ke :\33[1;33m ' +no)
  else:
     bersih()
     os.system('exit')

def trojanbts():
  print('')
  tatget = input('\33[31;1m[\33[32;1m•\33[31;1m] \33[36;1mMasukkan nomer target:\33[1;33m ')
  jum = int(input('\33[31;1m[\33[32;1m•\33[31;1m] \33[36;1mMasukkan Jumlah:\33[1;33m '))
  lan2 = input('\33[31;1m[\33[32;1m•\33[31;1m] \33[36;1mApakah anda yakin untuk melanjutkan? [y/t]:\33[1;33m ')
  if lan2 == 'y':
     sleep(1)
     print('')
     print('\33[31;1m[!] Mencari Target!')
     sleep(2)
     print('\33[32;1m[!] Target Ditemukan')
     print('')
     sleep(3)
     print('\33[31;1m[!] Menyiapkan bahan')
     sleep(2)
     ldb()
     print('')
     print('')
     sleep(1)
     print('\33[31;1mTrojan akan di kirim dalam 5 detik lagi!')
     sleep(2)
     print('Trojan siap dikirim')
     print('')
     sleep(3)
     for i in range(jum):
       sleep(0.5)
       print(f'\33[31;1m[\33[32;1m{i}\33[31;1m] \33[31;1mTrojan Sukses Terkirim ke :\33[1;33m ' +tatget)
  else:
     bersih()
     os.system('exit')

bersih()
print('\33[37;1m')
banner = '''
\33[31;1m _____          _
|_   _| __ ___ (_) __ _ _ __
  | || '__/ _ \| |/ _` | '_ \  \33[1;33mfake
\33[31;1m  | || | | (_) | | (_| | | | |
  |_||_|  \___// |\__,_|_| |_|
             |__/
\33[32;1m╔════════════════════════════════════════╗
\33[32;1m║\33[36;1m➣ Author : \33[1;33mRenal                        \33[32;1m║
\33[32;1m║\33[36;1m➣ YouTube: \33[1;33m-                           \33[32;1m ║
\33[32;1m║\33[36;1m➣ Github : \33[1;33m/github.com/R3N4L/          \33[32;1m ║
\33[32;1m╚════════════════════════════════════════╝
'''

note = '''
\33[31;1m                     Note!
        Script ini hanya untuk bercanda!
Saya yg buat script ini tidak bertanggung jawab!
    Saya hanya iseng saja membuat script ini!
'''

print(banner)
sleep(1)
print(note)
sleep(1)
print('\33[31;1m[\33[1;33m01\33[31;1m] \33[32;1mTanpa Batas')
print('\33[31;1m[\33[1;33m02\33[31;1m] \33[32;1mDengan Batas')
print('')

sleep(1)
men1 = input('\33[36;1m➣ Masukkan pilihan Anda:\33[1;33m ')
if men1 == '01':
   trojantnp()
elif men1 == '1':
   trojantnp()
elif men1 == '02':
   trojanbts()
elif men1 == '2':
   trojanbts()
else:
   print('Wrong input!')
