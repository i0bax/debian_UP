#!/usr/bin/python

import os
import argparse
from sys import argv

parser=argparse.ArgumentParser(description='''Jak uzywac skryptu.''', epilog='''Uzywaj tylko jednego przelacznika''')
parser.add_argument('-t', action='store_true' , help='Tworzenie lokalnego repozytorium')
parser.add_argument('-k', action='store_true' , help='Kasowanie lokalnego repozytorium')
args= parser.parse_args()

if args.t == True:
	# Tworzenie lokalnego repozytorium
	print ('\x1b[1;34m' + 'TWORZENIE lokalnego repozytorium' + '\x1b[0m')
	os.system("mkdir /mnt/repo")
	os.system("mount /dev/sdb1 /mnt/repo")
	os.system("ln -s mnt/repo/repo/debian /var/www/debian")
	os.system("ln -s mnt/repo/repo/kali /var/www/kali")
	os.system("echo 'deb http://127.0.0.1/debian stable main contrib non-free' > /etc/apt/sources.list")
	os.system("echo 'deb http://127.0.0.1/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
	os.system("service apache2 restart")
	print('\x1b[1;32m' + 'ZROBIONE' + '\x1b[0m')
	'''
	sprawdzic czy nie trzeba dodac linka !!
	cd /var/spool/apt-mirror/mirror/ftp.de.debian.org/debian/dists
	ln -s sarge/ stable
	'''
elif args.k == True:
	# Kasowanie lokalnego repozytorium
	print ('\x1b[1;34m' + 'KASOWANIE lokalnego repozytorium' + '\x1b[0m')
	os.system("echo 'deb http://ftp.pl.debian.org/debian jessie main contrib non-free' > /etc/apt/sources.list")
	os.system("rm -f /var/www/debian")
	os.system("rm -f /var/www/kali")
	os.system("umount /mnt/repo")
	os.system("rm -rf /mnt/repo")
	os.system("service apache2 restart")
	print('\x1b[1;32m' + 'ZROBIONE' + '\x1b[0m')
else:
	parser.print_help()