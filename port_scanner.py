import socket
import argparse


def scan_port(ip, port, timedout):
    try:
        s = socket.socket()
        s.settimeout(timedout)
        s.connect((ip, port))
        print(f"[+] Port {port} is OPEN")
        s.close()
        return True
    except socket.timeout:
        print(f"[-] Port {port} TIMED OUT")
    except ConnectionRefusedError:
        print(f"[-] Port {port} CLOSED")
    except Exception as e:
        print(f"[!] Error on port {port}: {e}")
    return False
