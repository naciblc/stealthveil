import subprocess
import random as rnd
import os

def sudocheck():
    if os.geteuid() != 0:
        print("Please run with root...")
        exit()
    else:
        pass
def macgenerator():
    fb = rnd.randint(0x00,0xff)
    fb = fb & 0b11111110
    mac = [fb] + [rnd.randint(0x00,0xff)for _ in range(5)]
    return ':'.join(f"{m:02x}"for m in mac)

def macbackup(interface):
    ifout = subprocess.getoutput(f"ifconfig {interface}")
    ifsplit = ifout.splitlines()
    for i in ifsplit:
        bc = i.strip()
        if bc.startswith("ether"):
            macb =bc.split()[1]
            backup = f"{interface}: ether {macb}"
    try:
        with open(".macbackup","r") as f:
            backups = [i.strip() for i in f.readlines()]
    except:
        backups = []
    back = False
    for a in backups:
        if backup.split(":")[0] in a.split(":")[0]:
            back = True
            break
        
    if back == False:
        with open(".macbackup","a") as i:
            i.write(backup)
            i.write("\n")
        print(f"Old Mac adress Backup Successful")
        



def success(interface):
    outp = subprocess.getoutput(f"ifconfig {interface}")
    a = outp.splitlines()
    for i in a:
        out = i.strip()
        if out.startswith("ether"):
            macsuc=out.split()[1]
    return macsuc

def macchanger():
    subprocess.call(["clear"])
    interface=subprocess.getoutput("ifconfig")
    interface=interface.splitlines()
    interfaces = []
    ia = 0
    interface_lst = {}
    for inter in interface:
        if inter and not inter.startswith(" "):
            interface_split=inter.split(":")[0]
            interfaces.append(interface_split)
    print("""İnterface List:
---------------""")
    for i in interfaces:
        interface_lst[ia] = i
        print(f"{ia}){i}")
        ia += 1
    print(f"{ia})Menu")
    while True:
        try:
            select_int = int(input("Select Interface: "))
        except:
            print("Wrong Choice")
            continue
        else:
            if select_int > ia:
                print("Wrong Choice")
            if select_int in interface_lst:
                selected = interface_lst[select_int]
                macbackup(selected)
                mac=macgenerator()

                subprocess.call(["ifconfig",selected,"down"])
                subprocess.call(["ifconfig",selected,"hw","ether",mac])
                subprocess.call(["ifconfig",selected,"up"])
                suc = success(selected)
                if mac == suc:
                    print(f"Successful New Mac Adress: {mac}")
                    input("Press a key to return")
                    main()
                    break
                else:
                    print(f"En Error Occourred...")
                    break
            elif select_int == ia:
                main()
                break
                
    
def backupmac():
    with open(".macbackup","r") as i:
        mac = i.readlines()
        print("----------")
        print("Interfaces")
        print("----------")
        for i in mac:
            print(i.strip())
    input("Press a key to return")
    main()


def manuelchange():
    subprocess.call(["clear"])
    print("""Interface List:
---------------""")
    lists = subprocess.getoutput(["ifconfig"])
    macs = lists.splitlines()
    intf = []
    interfacelist = {}
    l = 0
    aii = 0
    for b in macs:
        if b and not b.startswith(" "):
            intf.append(b.split(":")[0])
    
    for _ in intf:
        interfacelist[l] = _
        l +=1
    for i in intf:
        print(f"{aii}){i}")
        aii += 1
    print(f"{aii})Menu")
    while True:
        try:            
            selectinterface = int(input("Selected Interface: "))
        except:
            print("Wrong Choice")
            continue
        else:
            if selectinterface > aii:
                print("Wrong Choice")
            if selectinterface in interfacelist:
                global selecti
                selecti = interfacelist[selectinterface]
                cm()
                break
            elif selectinterface == aii:
                main()
                break
def cm():
    mac = input("Write Mac Adress: ")
    subprocess.call(["ifconfig",selecti,"down"])

    result=subprocess.call(["ifconfig",selecti,"hw","ether",mac])
    if result == 1:
        print("You entered an incorrect MAC address. Please try again.")
        subprocess.call(["ifconfig",selecti,"up"])        
        cm()
    else:
        subprocess.call(["ifconfig",selecti,"up"])
        suc=success(selecti)
        if mac in suc:
            macbackup(selecti)
            print(f"Successful New Mac Adress: {suc}")
            input("Press a key to return")
            main()
        else:
            print(f"En Error Occourred...")

def ipbackup(interface):
    
    ifout = subprocess.getoutput(f"ifconfig {interface}")
    ifsplit = ifout.splitlines()
    ipb = None
    for i in ifsplit:
        line = i.strip()
        if line.startswith("inet "):
            ipb = line.split()[1]
            backup = f"{interface}: inet {ipb}"
            break
    
    if ipb is None:
        print("IP address not found.")
        return

    
    try:
        with open(".ipbackup", "r") as f:
            backups = [i.strip() for i in f.readlines()]
    except FileNotFoundError:
        backups = []

    
    back = False
    for a in backups:
        if backup.split(":")[0] in a.split(":")[0]:
            back = True
            break

    if not back:
        with open(".ipbackup", "a") as f:
            f.write(backup + "\n")
        print("Old IP address backup successful.")
    else:
        print("Backup already exists.")
    
def sucip(interface):
    d = subprocess.getoutput(f"ifconfig {interface}")
    a=d.splitlines()
    for i in a:
        s=i.strip()
        if s.startswith("inet "):
            ipsuc=s.split()[1]
            return ipsuc

def ipchange():
    subprocess.call(["clear"])
    interface=subprocess.getoutput("ifconfig")
    interface=interface.splitlines()
    interfaces = []
    ia = 0
    interface_lst = {}
    for inter in interface:
        if inter and not inter.startswith(" "):
            interface_split=inter.split(":")[0]
            interfaces.append(interface_split)
    print("""İnterface List:
---------------""")
    for i in interfaces:
        interface_lst[ia] = i
        print(f"{ia}){i}")
        ia += 1
    print(f"{ia})Menu")
    while True:
            try:
                select_int = int(input("Select Interface: "))
            except:
                print("Wrong Choice")
                continue
            else:
                if select_int > ia:
                    print("Wrong Choice")
                    continue
                if select_int in interface_lst:
                    selected = interface_lst[select_int]
                    
                    ip= input("Write Ip Adress: ")
                    subprocess.call(["ifconfig",selected,ip])
                    suc = sucip(selected)
                    if ip == suc:
                        ipbackup(selected)
                        print(f"Successful New Ip Adress: {ip}")
                        input("Press a key to return")
                        main()
                        break
                    else:
                        print(f"En Error Occourred...")
                        break
                elif select_int == ia:
                    main()
                    break


def backupip():
    try:
        with open(".ipbackup", "r") as f:
            ip_lines = f.readlines()
            print("----------")
            print("IP Backups")
            print("----------")
            for line in ip_lines:
                print(line.strip())
    except FileNotFoundError:
        print("No IP backup file found.")
    
    input("Press a key to return")
    main()

def main():
    subprocess.call(["clear"])
    sudocheck()
    print("""
Stealthveil & Network Interface IP & MAC Address Manager
---------------------
1) Change MAC Address
2) Change IP Address
3) View MAC Address Backups
4) View IP Address Backups
5) Clear All Backups
6) Exit
---------------------""")
    while True:
        try:
            global proc
            proc =int(input("Please select the action to be taken: "))
        except:
            print("Yanlış Tuşlama")
            continue
        else:
            break
    sec()
def clear():
    retcode = subprocess.call(["rm","-rf",".macbackup",".ipbackup"])
    if retcode == 0:
        print("Files deleted successfully.")
        return True
    else:
        print(f"Error deleting files. Return code: {retcode}")
        return False
def sec():
    subprocess.call(["clear"])
    if proc == 1:
        print("1)Manuel Change")
        print("2)Random Change")
        print("3)Menu")
        metod = int(input("Select Change Metod: "))
        if metod == 1:
            manuelchange()
        elif metod == 2:
            macchanger()
        elif metod == 3:
            main()
        else:
            print("Wrong Choice")
            input("Press a key to return")
        sec()
    elif proc == 2:
        ipchange()
    elif proc == 3:
        backupmac()
    elif proc == 4:
        backupip()
    elif proc == 5:
        clear()
    elif proc == 6:
        exit()
    else:
        print("Wrong Choice")
        main()


main()
