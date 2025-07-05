# 🔐 Main File: Integrated Port Scanner & Banner Grabber

📌 Description:

    This script acts as the **central coordinator** for two critical cybersecurity utilities:
        1. A **port scanner** (`port_scanner.py`)
        2. A **banner grabber** (`banner_grab.py`)

It integrates the functionalities of both scripts, allowing you to:
- **Scan a range of ports** on a target host.
- **Identify open ports** and perform **banner grabbing** to discover running services.
- Do so with **custom timeouts** and **multi-threading** for performance.

This file showcases how modular cybersecurity scripts can be **connected and orchestrated** in a secure, flexible, and scalable way — reflecting real-world penetration testing scenarios.

--------

⚙️ How It Works:

1. Accepts arguments via `argparse`:
   - `--target`: IP/domain to scan
   - `--ports`: Range (e.g., `20-100`)
   - `--timedout`: Socket timeout (default is usually `3`)
2. For each port:
   - Scans for availability.
   - If open, attempts to grab service banner.
3. Prints live feedback to the terminal.

--------

📥 Usage:
bash--> python3 mainfile.py --target scanme.nmap.org --ports 20-100 --timeout 2

Example Output:
[*] Scanning scanme.nmap.org from port 20 to 100
[+] Port 22 is OPEN
🔍 Banner from port 22: SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13
[-] Port 23 CLOSED
...
🧩 Dependencies
Python 3

----------

Built-in modules:
    socket
    argparse
    concurrent.futures (for threading)

🧠 Learning Outcome:
    This file demonstrates:
        Your understanding of network sockets, scanning logic, and exception handling.
        How to use argument parsing to build flexible CLI tools.
        How to structure cybersecurity tools modularly, which is essential for real-world security audits and DevSecOps pipelines.


📁 Files Connected:
File	         |      Description
                 |
port_scanner.py  |	Scans ports, handles TCP sockets
banner_grab.py	 |  Connects to open ports, grabs service banners
mainfile.py   	 |   Combines both functionalities into one command-line interface

----------

🧪 Tested On
    Ubuntu 22.04
    Python 3.10+
    Public target: scanme.nmap.org (for educational and safe testing)

📚 License
    Educational use only.