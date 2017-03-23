#!/usr/bin/python

import os

os.system("apt-get install apt-mirror -y")

print ('\x1b[1;34m' + 'MONTOWANIE lokalnego repozytorium' + '\x1b[0m')
os.system("mkdir /mnt/repo")
os.system("mount /dev/sdb1 /mnt/repo")
print('\x1b[1;32m' + 'ZROBIONE' + '\n' + '\x1b[0m')

print ('\x1b[1;34m' + 'AKTUALIZACJA mirrora Debiana' + '\x1b[0m')
os.system("echo 'set base_path    /mnt/repo/repo/debian' > /etc/apt/mirror.list")
os.system("echo 'set defaultarch  amd64' >> /etc/apt/mirror.list")
os.system("echo 'set nthreads     20' >> /etc/apt/mirror.list")
os.system("echo 'set _tilde 0' >> /etc/apt/mirror.list")
os.system("echo 'deb-amd64 http://ftp.pl.debian.org/debian jessie main contrib non-free' >> /etc/apt/mirror.list")
os.system("echo 'clean http://ftp.pl.debian.org/debian' >> /etc/apt/mirror.list")
os.system("apt-mirror")
print('\x1b[1;32m' + 'ZROBIONE' + '\n' + '\x1b[0m')

print ('\x1b[1;34m' + 'AKTUALIZACJA mirrora Kali' + '\x1b[0m')
os.system("echo 'set base_path    /mnt/repo/repo/kali' > /etc/apt/mirror.list")
os.system("echo 'set defaultarch  amd64' >> /etc/apt/mirror.list")
os.system("echo 'set nthreads     20' >> /etc/apt/mirror.list")
os.system("echo 'set _tilde 0' >> /etc/apt/mirror.list")
os.system("echo 'deb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/mirror.list")
os.system("echo 'clean http://http.kali.org/kali' >> /etc/apt/mirror.list")
os.system("apt-mirror")
print('\x1b[1;32m' + 'ZROBIONE' + '\n' + '\x1b[0m')

print ('\x1b[1;34m' + 'KASOWANIE lokalnego repozytorium' + '\x1b[0m')
os.system("umount /mnt/repo")
os.system("rm -rf /mnt/repo")
os.system("service apache2 restart")
print('\x1b[1;32m' + 'ZROBIONE' + '\n' + '\x1b[0m')
