🔍 Port Scanner Script — port_scanner.py
        This script scans a range of TCP ports on a specified target (domain or IP) and determines whether each port is open, closed, or timed out.

📌 Purpose:
        Port scanning is a foundational technique in cybersecurity to:
        Discover open ports and services on a system
        Assess network security posture
        Identify potential vulnerabilities
        This script is part of a larger project on reconnaissance techniques.

Arguments:
        --target → Target domain or IP address (e.g., scanme.nmap.org)
        --ports → Port range to scan (e.g., 20-100)

✅ Example Output:
        [*] Scanning scanme.nmap.org from port 20 to 100
        [+] Port 22 is OPEN
        [-] Port 23 CLOSED
        [-] Port 25 TIMED OUT
        ...
📌 Note: You can adjust the timeout value in the code to wait longer for slower responses.

🧠 Features:
        Scans a custom port range
        Uses TCP sockets to connect
        Basic error handling (timeouts, refused connections)
        Output clearly shows status for each port

🧪 Usage:
        python3 port_scanner.py --target scanme.nmap.org --ports 20-100