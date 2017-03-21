#!/usr/bin/python

import os
import argparse
from sys import argv

parser=argparse.ArgumentParser(description='''Jak uzywac skryptu.''', epilog='''Uzywaj tylko jednego przelacznika''')
parser.add_argument('-t', action='store_true' , help='Tworzenie lokalnego repozytorium')
parser.add_argument('-k', action='store_true' , help='Kasowanie lokalnego repozytorium')
args= parser.parse_args()

	# Tworzenie lokalnego repozytorium
if args.t == True:
	print ('\x1b[1;34m' + 'TWORZENIE lokalnego repozytorium' + '\x1b[0m')
	os.system("mkdir /mnt/repo")
	os.system("mount /dev/sdb1 /mnt/repo")
	os.system("ln -s /mnt/repo/repo/debian/mirror/ftp.us.debian.org/debian /var/www/html/debian")
	os.system("ln -s /mnt/repo/repo/kali/mirror/http.kali.org/kali /var/www/html/kali")
	os.system("cp /etc/apt/sources.list /etc/apt/sources.list.bak")
	os.system("echo 'deb http://127.0.0.1/debian unstable main contrib non-free' > /etc/apt/sources.list")
	os.system("echo 'deb http://127.0.0.1/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
	os.system("service apache2 restart")
	print('\x1b[1;32m' + 'ZROBIONE' + '\x1b[0m')
	'''
	sprawdzic czy nie trzeba dodac linka !!
	cd /var/spool/apt-mirror/mirror/ftp.de.debian.org/debian/dists
	ln -s sarge/ stable
	'''
	# Kasowanie lokalnego repozytorium
elif args.k == True:
	print ('\x1b[1;34m' + 'KASOWANIE lokalnego repozytorium' + '\x1b[0m')
	os.system("cp /etc/apt/sources.list.bak /etc/apt/sources.list")
	os.system("rm -f /var/www/html/debian")
	os.system("rm -f /var/www/html/kali")
	os.system("umount /mnt/repo")
	os.system("rm -rf /mnt/repo")
	os.system("service apache2 restart")
	print('\x1b[1;32m' + 'ZROBIONE' + '\x1b[0m')
else:
	parser.print_help()
