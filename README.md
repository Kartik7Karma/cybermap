# 🛡️ CyberMap: Python-Based Network Reconnaissance Toolkit

CyberMap is a lightweight, modular Python toolkit designed to perform basic **network reconnaissance tasks** such as port scanning and banner grabbing. It showcases how low-level socket programming and concurrency can be used to identify open ports and extract service banners from target systems.

This project demonstrates foundational cybersecurity skills like footprinting, enumeration, and multithreaded scanning—vital in penetration testing and network auditing.

--------

## 📁 Project Structure

| File             | Description |
|------------------|-------------|
| `banner_grab.py` | Grabs banners from open ports to identify running services. |
| `port_scanner.py`| Scans a range of ports on a given target using TCP sockets. |
| `mainfile.py`    | Combines port scanning and banner grabbing into a unified script using command-line arguments. |

--------

## 🚀 Features

- Custom **target host** and **port range** input via CLI.
- **Multithreaded scanning** for faster results.
- **Banner grabbing** using raw socket communication.
- Command-line options for **timeout** configuration.
- Modular design with reusable components.

--------

## 🔧 Technologies Used

- **Python 3**
- `socket` for low-level networking
- `argparse` for command-line interfaces
- `concurrent.futures.ThreadPoolExecutor` for multithreading

--------

🖥️ How to Use

1. Port Scanner
bash--> python3 port_scanner.py --target scanme.nmap.org --ports 20-100 --timeout 1

2. Banner Grabber
bash--> python3 banner_grab.py --ip scanme.nmap.org --port 22 --timeout 1

3. Combined Main Script
bash-->python3 mainfile.py --target scanme.nmap.org --ports 20-100 --timeout 1

scanme.nmap.org is a public test server provided by Nmap. Replace with your own host if required.

--------

📸 Sample Output:

[✔] Port 22 is open
[🔍] Banner from port 22: SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13
[✔] Port 80 is open
[🔍] Banner from port 80: HTTP/1.1 400 Bad Request

--------

✅ Future Enhancements:

Add UDP port scanning
Export results in CSV/JSON
GUI wrapper using Tkinter or PyQt

--------

👤 Author___

Kartik Budhlakoti
Cybersecurity & Python Development
