#!/usr/bin/python

import os

#instalacja repozytoriow
print ('\x1b[1;34m' + 'DODAWANIE REPOZYTORIOW' + '\x1b[0m')
os.system("echo '# Kali linux repo Dodane\ndeb http://127.0.0.1/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
os.system("apt-get update -m")
print('\x1b[1;32m' + 'ZAINSTALOWANE!' + '\x1b[0m')

#instalacja paczek
# Information Gathering
print ('\x1b[1;34m' + 'INSTALACJA Information Gathering' + '\x1b[0m')
os.system("apt-get install -y acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/" )
print('\x1b[1;32m' + 'ZAINSTALOWANE!' + '\x1b[0m')
# Vulnerability Analysis
print ('\x1b[1;34m' + 'INSTALACJA Vulnerability Analysis' + '\x1b[0m')
os.system("apt-get install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")
print('\x1b[1;32m' + 'ZAINSTALOWANE!' + '\x1b[0m')
# Wireless Attacks
print ('\x1b[1;34m' + 'INSTALACJA Wireless Attacks' + '\x1b[0m')
os.system("apt-get install -y aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite")
print('\x1b[1;32m' + 'ZAINSTALOWANE!' + '\x1b[0m')
# Web Applications
print ('\x1b[1;34m' + 'INSTALACJA Web Applications' + '\x1b[0m')
os.system("apt-get install -y apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy")
print('\x1b[1;32m' + 'ZAINSTALOWANE!' + '\x1b[0m')
# Sniffing & Spoofing
print ('\x1b[1;34m' + 'INSTALACJA Sniffing & Spoofing' + '\x1b[0m')
os.system("apt-get install -y burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy")
print('\x1b[1;32m' + 'ZAINSTALOWANE!' + '\x1b[0m')
# Maintaining Access
print ('\x1b[1;34m' + 'INSTALACJA Maintaining Access' + '\x1b[0m')
os.system("apt-get install -y cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely")
print('\x1b[1;32m' + 'ZAINSTALOWANE!' + '\x1b[0m')
# Reporting Tools
print ('\x1b[1;34m' + 'INSTALACJA Reporting Tools' + '\x1b[0m')
os.system("apt-get install -y casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal")
print('\x1b[1;32m' + 'ZAINSTALOWANE!' + '\x1b[0m')
# Exploitation Tools
print ('\x1b[1;34m' + 'INSTALACJA Exploitation Tools' + '\x1b[0m')
os.system("apt-get install -y armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss")
print('\x1b[1;32m' + 'ZAINSTALOWANE!' + '\x1b[0m')
# Forensics Tools
print ('\x1b[1;34m' + 'INSTALACJA Forensics Tools' + '\x1b[0m')
os.system("apt-get install -y binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico")
print('\x1b[1;32m' + 'ZAINSTALOWANE!' + '\x1b[0m')
# Stress Testing
print ('\x1b[1;34m' + 'INSTALACJA Stress Testing' + '\x1b[0m')
os.system("apt-get install -y dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos")
print('\x1b[1;32m' + 'ZAINSTALOWANE!' + '\x1b[0m')
# Password Attacks
print ('\x1b[1;34m' + 'INSTALACJA Password Attacks' + '\x1b[0m')
os.system("apt-get install -y acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy")
print('\x1b[1;32m' + 'ZAINSTALOWANE!' + '\x1b[0m')
# Reverse Engineering
print ('\x1b[1;34m' + 'INSTALACJA Reverse Engineering' + '\x1b[0m')
os.system("apt-get install -y apktool dex2jar python-diStorm3 edb-debugger jad javasnoop JD OllyDbg smali Valgrind YARA")
print('\x1b[1;32m' + 'ZAINSTALOWANE!' + '\x1b[0m')
# Hardware Hacking
print ('\x1b[1;34m' + 'INSTALACJA Hardware Hacking' + '\x1b[0m')
os.system("apt-get install -y android-sdk apktool arduino dex2jar sakis3g smali")
print('\x1b[1;32m' + 'ZAINSTALOWANE!' + '\x1b[0m')
# Dodatki
print ('\x1b[1;34m' + 'INSTALACJA Dodatkow' + '\x1b[0m')
os.system("apt-get install -y usbguard usbguard-applet-qt")
print('\x1b[1;32m' + 'ZAINSTALOWANE!' + '\x1b[0m')

# Kasowanie repozytoriow
os.system("apt-get autoremove")
os.system("head -n-2 /etc/apt/sources.list > /etc/apt/sources.list.tmp")
os.system("mv /etc/apt/sources.list.tmp /etc/apt/sources.list")
print('\x1b[1;31m' + 'WPIS DO REPO SKASOWANY!' + '\x1b[0m')
