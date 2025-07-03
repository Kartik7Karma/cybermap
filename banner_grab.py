import socket
import argparse


def grab_banner(ip, port, timedout):
    try:
        s = socket.socket()
        s.settimeout(timedout)
        s.connect((ip, port))
        banner = s.recv(1024).decode().strip()
        print(f"[🔍] Banner from port {port}: {banner}")
        s.close()
    except Exception as e:
        print(f"[!] Failed to grab banner from port {port}: {e}")
