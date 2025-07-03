import argparse
from sock_arg import scan_port
from banner_grab import grab_banner

def main():
    parser = argparse.ArgumentParser(description="Cybersecurity Port Scanner with Banner Grabbing")
    parser.add_argument('--target', type=str, required=True, help='Target IP or hostname')
    parser.add_argument('--ports', type=str, required=True, help='Port range, like 20-100')
    parser.add_argument('--timedout', type=int, default=5 ,help='time-out duration in seconds')

    args = parser.parse_args()

    target = args.target
    start_port, end_port = map(int, args.ports.split('-'))
    timedout = args.timedout

    print(f"[*] Scanning {target} from port {start_port} to {end_port}")

    for port in range(start_port, end_port + 1):
        if scan_port(target, port, timedout):
           grab_banner(target, port, timedout)

if __name__ == "__main__":
    main()
