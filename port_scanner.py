import socket
import concurrent.futures
import sys
import argparse

# Colors
RED = "\033[91m"     # Open ports
GREEN = "\033[92m"   # Banner text
YELLOW = "\033[93m"  # Closed/filtered ports
RESET = "\033[0m"

def format_port_results(results, show_all=False):
    formatted_results = "\nPort Scan Results:\n"
    formatted_results += "{:<8} {:<15} {:<15}\n".format("Port", "Service", "Status")
    formatted_results += "-" * 45 + "\n"
    for port, service, banner, status in sorted(results):
        if status:  # Open port
            formatted_results += f"{RED}{port:<8} {service:<15} {'Open':<15}{RESET}\n"
            if banner:
                for line in banner.splitlines():
                    formatted_results += f"{GREEN}{'':<8}{line}{RESET}\n"
        elif show_all:  # Only display closed/filtered if --all
            formatted_results += f"{YELLOW}{port:<8} {'':<15} {'Closed/Filtered':<15}{RESET}\n"
    return formatted_results

def get_banner(sock):
    try:
        sock.settimeout(1)
        banner = sock.recv(1024).decode("utf-8", errors="ignore").strip()
        return banner
    except:
        return ""

def scan_port(target_ip, port):
    sock = None
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            try:
                service = socket.getservbyport(port, 'tcp')
            except:
                service = "Unknown"
            banner = get_banner(sock)
            return port, service, banner, True
        else:
            return port, "", "", False
    except:
        return port, "", "", False
    finally:
        if sock:
            sock.close()

def port_scan(target_host, start_port, end_port, show_all=False):
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print(f"{RED}Error: Could not resolve host {target_host}{RESET}")
        return

    print(f"Starting scan on host: {target_ip}\n")

    results = []
    total_ports = end_port - start_port + 1
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(scan_port, target_ip, port): port for port in range(start_port, end_port + 1)}
        for i, future in enumerate(concurrent.futures.as_completed(futures), start=1):
            port, service, banner, status = future.result()
            results.append((port, service, banner, status))
            sys.stdout.write(f"\rProgress: {i}/{total_ports} ports scanned")
            sys.stdout.flush()

    sys.stdout.write("\n")
    print(format_port_results(results, show_all))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python Port Scanner")
    parser.add_argument("target", help="Target IP/Hostname")
    parser.add_argument("start", type=int, help="Start Port")
    parser.add_argument("end", type=int, help="End Port")
    parser.add_argument("--all", action="store_true", help="Show all ports (including closed/filtered)")
    args = parser.parse_args()

    port_scan(args.target, args.start, args.end, args.all)
