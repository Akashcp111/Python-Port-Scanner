# 🔍 Python Port Scanner

A lightweight, multi-threaded **TCP Port Scanner** written in Python.  
It mimics the style of Nmap by showing open ports, services, and even banner information when available.  
Ideal for **students, ethical hackers, and cybersecurity enthusiasts** who want to learn the internals of port scanning.

---

## 🚀 Features

- 🔎 **Custom Port Range Scanning** – Scan any port range (1–65535).  
- ⚡ **Multi-threaded Scanning** – Fast execution with Python’s `ThreadPoolExecutor`.  
- 🛠️ **Service Detection** – Identifies common services by port number.  
- 📡 **Banner Grabbing** – Fetches extra info when services expose version details.  
- 🎨 **Color-Coded Output**  
  - 🔴 Open ports  
  - 🟡 Closed/Filtered ports  
  - 🟢 Banner text (if available)  
- 📊 **Progress Indicator** – Real-time scan progress like professional tools.  
- 🎛️ **Modes** –  
  - Default → Only shows open ports.  
  - `--all` flag → Displays open + closed/filtered ports (Nmap-style).  

---

## ⚙️ Installation

Requires **Python 3.7+**. No external libraries needed.

```bash
# Clone the repository
git clone https://github.com/your-username/python-port-scanner.git
cd python-port-scanner

# Run the script
python scanner.py <target> <start_port> <end_port> [--all]
```
## 🖥️ Usage Examples
1. Scan common ports
```
python scanner.py 192.168.0.102 1 1024
```
2. Full port scan
```
python scanner.py 192.168.0.102 1 65535
```
3. Show all ports (open + closed/filtered)
```
python scanner.py 192.168.0.102 1 1000 --all
```
## 📊 Example Output
```
Starting scan on host: 192.168.0.102

Progress: 991/991 ports scanned

Port     Service         Status
----------------------------------------
135      epmap           Open
139      netbios-ssn     Open
445      microsoft-ds    Open
80       http            Closed/Filtered
443      https           Closed/Filtered
```
## 📖 How It Works

1. User provides a target IP/hostname and a port range.
2. Each port is probed using a TCP socket connection attempt.

* ✅ Success → Port marked Open.

* ❌ Failure → Port marked Closed/Filtered.

3. For open ports:

* Detects service name via socket.getservbyport().

* Attempts to grab banners from the service for extra details.

4. Results are displayed in a clean, color-coded table.

## 🔬 Educational Value

This project helps you understand:

* ✅ TCP connection handling in Python

* ✅ Basics of service fingerprinting

* ✅ Multi-threading with ThreadPoolExecutor

* ✅ How tools like Nmap work under the hood

## 🛡️ Disclaimer

### ⚠️ Legal Notice
This tool is for educational purposes and authorized testing only.
Do not scan targets you don’t own or have explicit permission to test.
Unauthorized usage may violate laws and regulations.

## 🤝 Contributing

Want to improve this project? Contributions are welcome!

1. Fork this repository

2. Create a feature branch (feature/new-feature)

3. Commit your changes

4. Submit a Pull Request

Ideas for future improvements:

* 🔹 UDP scanning support

* 🔹 --top 1000 most common ports (like Nmap)

* 🔹 Save scan results to JSON/CSV

* 🔹 Add OS fingerprinting heuristics

## 📜 License

* This project is licensed under the MIT License.
* You are free to use, modify, and share with proper attribution.
