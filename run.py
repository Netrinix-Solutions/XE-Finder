import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import os
import sys
import time
import concurrent.futures
import socket

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def hacker_intro():
    clear_screen()
    print("\033[1;32m")  # Bright green text
    print(r"""
  ██╗███████╗    ███████╗██╗███╗░░██╗██████╗░███████╗██████╗░
  ╚██╗██╔════╝    ██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗
   ╚███╔╝░█████╗  █████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
   ██╔██╗░╚════╝  ██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
  ██╔╝╚██╗███████╗██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║
  ╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝
  """)
    print("\033[1;36m" + "=" * 65)
    print(" Web Reconnaissance Suite - Professional Security Scanner")
    print("=" * 65)
    print("\033[0;32mDeveloped by Netrinix Solutions - https://netrinix.com\033[0m")
    print("\033[1;36m" + "=" * 65 + "\033[0m")

    print("\n\033[1;33mInitializing system...\033[0m")
    for i in range(4):
        print(f"\033[1;32mLoading{'...'[:i+1]}\033[0m", end='\r')
        time.sleep(0.5)
    print("\n\033[1;32mSecurity protocols engaged\033[0m")
    time.sleep(0.5)
    print("\033[1;32mReconnaissance modules activated\033[0m")
    time.sleep(0.5)
    print("\033[1;32mReady for target acquisition\033[0m\n")

def get_js_files(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        scripts = soup.find_all("script")
        js_files = []

        for script in scripts:
            src = script.get("src")
            if src:
                full_url = urljoin(url, src)
                js_files.append(full_url)

        return js_files, response.status_code
    except requests.exceptions.RequestException as e:
        print(f"\033[1;31mConnection Error: {e}\033[0m")
        return [], None

def find_subdomains(domain, wordlist):
    subdomains = []
    print(f"\n\033[1;33m[+] Scanning for subdomains on {domain}\033[0m")

    try:
        with open(wordlist, 'r') as f:
            sub_list = [line.strip() for line in f]
    except FileNotFoundError:
        print(f"\033[1;31m[!] Wordlist file not found: {wordlist}\033[0m")
        return []

    print(f"\033[1;36m[+] Loaded {len(sub_list)} subdomains for scanning\033[0m")

    def check_subdomain(subdomain):
        full_domain = f"{subdomain}.{domain}"
        try:
            ip = socket.gethostbyname(full_domain)
            return full_domain, ip
        except:
            return None

    found_count = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        future_to_sub = {executor.submit(check_subdomain, sub): sub for sub in sub_list}
        for future in concurrent.futures.as_completed(future_to_sub):
            sub = future_to_sub[future]
            try:
                result = future.result()
                if result:
                    subdomain, ip = result
                    print(f"\033[1;32m[+] Found: {subdomain} \033[0m(\033[0;34m{ip}\033[0m)")
                    subdomains.append((subdomain, ip))
                    found_count += 1
            except Exception as e:
                pass

    print(f"\n\033[1;32m[+] Subdomain scan complete: Found {found_count} live subdomains\033[0m")
    return subdomains

def find_hidden_directories(url, wordlist):
    directories = []
    print(f"\n\033[1;33m[+] Scanning for hidden directories on {url}\033[0m")

    try:
        with open(wordlist, 'r') as f:
            dir_list = [line.strip() for line in f]
    except FileNotFoundError:
        print(f"\033[1;31m[!] Wordlist file not found: {wordlist}\033[0m")
        return []

    print(f"\033[1;36m[+] Loaded {len(dir_list)} directories for scanning\033[0m")

    session = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    found_count = 0
    for directory in dir_list:
        target_url = urljoin(url, directory)
        try:
            response = session.get(target_url, headers=headers, timeout=5, allow_redirects=False)
            status = response.status_code

            if status < 400 or status == 403:
                print(f"\033[1;32m[+] Found: {target_url} \033[0m(\033[0;34m{status}\033[0m)")
                directories.append((target_url, status))
                found_count += 1
        except:
            pass

    print(f"\n\033[1;32m[+] Directory scan complete: Found {found_count} accessible directories\033[0m")
    return directories

def find_sensitive_files(url):
    sensitive_files = []
    print(f"\n\033[1;33m[+] Scanning for sensitive files on {url}\033[0m")

    file_list = [
        'robots.txt', '.env', '.git/config', '.htaccess', 'web.config',
        'backup.zip', 'dump.sql', 'config.php', 'security.txt', 'crossdomain.xml'
    ]

    session = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    found_count = 0
    for file in file_list:
        target_url = urljoin(url, file)
        try:
            response = session.get(target_url, headers=headers, timeout=5, allow_redirects=False)
            status = response.status_code

            if status == 200:
                print(f"\033[1;32m[+] Found: {target_url} \033[0m(\033[0;34m{status}\033[0m)")
                sensitive_files.append((target_url, status))
                found_count += 1
        except:
            pass

    print(f"\n\033[1;32m[+] Sensitive file scan complete: Found {found_count} exposed files\033[0m")
    return sensitive_files

def save_results(data, path, scan_type):
    try:
        with open(path, 'w') as f:
            if scan_type == "js":
                f.write("JavaScript Files Found:\n")
                f.write("=" * 50 + "\n")
                for i, link in enumerate(data, 1):
                    f.write(f"{i}. {link}\n")
            elif scan_type == "subdomains":
                f.write("Subdomains Found:\n")
                f.write("=" * 50 + "\n")
                for i, (subdomain, ip) in enumerate(data, 1):
                    f.write(f"{i}. {subdomain} ({ip})\n")
            elif scan_type == "directories":
                f.write("Hidden Directories Found:\n")
                f.write("=" * 50 + "\n")
                for i, (url, status) in enumerate(data, 1):
                    f.write(f"{i}. {url} (Status: {status})\n")
            elif scan_type == "sensitive":
                f.write("Sensitive Files Found:\n")
                f.write("=" * 50 + "\n")
                for i, (url, status) in enumerate(data, 1):
                    f.write(f"{i}. {url} (Status: {status})\n")
        return True
    except Exception as e:
        print(f"\033[1;31mSave Error: {e}\033[0m")
        return False

def display_menu():
    print("\n\033[1;36m[+] Select scan type:")
    print("\033[1;37m1. JavaScript File Finder")
    print("2. Subdomain Discovery")
    print("3. Hidden Directory Scanner")
    print("4. Sensitive File Finder")
    print("5. Full Reconnaissance Scan")
    print("6. Exit\033[0m")
    return input("\033[1;37m>>> \033[0m").strip()

def main():
    hacker_intro()

    # Get user input
    print("\033[1;36m[+] Enter target URL (e.g., https://example.com):")
    url = input("\033[1;37m>>> \033[0m").strip()

    print("\033[1;36m[+] Enter storage path for results (e.g., /path/to/results.txt):")
    storage_path = input("\033[1;37m>>> \033[0m").strip()

    # Initialize wordlists
    subdomain_wordlist = "subdomains.txt"
    directory_wordlist = "directories.txt"

    # Create default wordlists if not available
    if not os.path.exists(subdomain_wordlist):
        with open(subdomain_wordlist, 'w') as f:
            f.write("www\nmail\nftp\nadmin\nwebmail\nsecure\nblog\ndev\ntest\nstaging\napi\ncdn\nportal\nshop\napp\n")

    if not os.path.exists(directory_wordlist):
        with open(directory_wordlist, 'w') as f:
            f.write("admin\nlogin\nwp-admin\nbackup\nold\ntemp\ntest\nhidden\ncgi-bin\nsecret\nconfig\n.git\n.ssh\nbackups\narchive\n")

    # Ask for custom wordlist paths
    print("\033[1;36m[+] Enter custom subdomain wordlist path (or press Enter for default):")
    custom_sub = input("\033[1;37m>>> \033[0m").strip()
    if custom_sub and os.path.exists(custom_sub):
        subdomain_wordlist = custom_sub
        print(f"\033[1;32m[+] Using custom subdomain wordlist: {subdomain_wordlist}\033[0m")
    else:
        if custom_sub:
            print(f"\033[1;31m[!] Custom wordlist not found, using default: {subdomain_wordlist}\033[0m")
        else:
            print(f"\033[1;32m[+] Using default subdomain wordlist\033[0m")

    print("\033[1;36m[+] Enter custom directory wordlist path (or press Enter for default):")
    custom_dir = input("\033[1;37m>>> \033[0m").strip()
    if custom_dir and os.path.exists(custom_dir):
        directory_wordlist = custom_dir
        print(f"\033[1;32m[+] Using custom directory wordlist: {directory_wordlist}\033[0m")
    else:
        if custom_dir:
            print(f"\033[1;31m[!] Custom wordlist not found, using default: {directory_wordlist}\033[0m")
        else:
            print(f"\033[1;32m[+] Using default directory wordlist\033[0m")

    while True:
        choice = display_menu()

        if choice == "1":  # JavaScript Finder
            print(f"\n\033[1;33mScanning target: \033[1;35m{url}\033[0m")
            js_links, status = get_js_files(url)

            print("\n" + "=" * 65)
            print(f"\033[1;36mJS SCAN COMPLETE | Status Code: {status if status else 'N/A'}\033[0m")
            print("=" * 65)

            if js_links:
                print(f"\n\033[1;32m[+] Found {len(js_links)} JavaScript files:\033[0m")
                for i, link in enumerate(js_links, 1):
                    print(f"\033[0;32m{i:02d}. \033[0;34m{link}\033[0m")

                # Save results
                if save_results(js_links, storage_path, "js"):
                    print(f"\n\033[1;32mResults saved to: \033[1;35m{storage_path}\033[0m")
            else:
                print("\n\033[1;31m[!] No JavaScript files found or error occurred\033[0m")

        elif choice == "2":  # Subdomain Discovery
            domain = urlparse(url).netloc
            subdomains = find_subdomains(domain, subdomain_wordlist)

            if subdomains:
                save_path = storage_path.replace(".txt", "_subdomains.txt")
                if save_results(subdomains, save_path, "subdomains"):
                    print(f"\n\033[1;32mSubdomain results saved to: \033[1;35m{save_path}\033[0m")
            else:
                print("\n\033[1;31m[!] No subdomains found\033[0m")

        elif choice == "3":  # Hidden Directory Scanner
            directories = find_hidden_directories(url, directory_wordlist)

            if directories:
                save_path = storage_path.replace(".txt", "_directories.txt")
                if save_results(directories, save_path, "directories"):
                    print(f"\n\033[1;32mDirectory results saved to: \033[1;35m{save_path}\033[0m")
            else:
                print("\n\033[1;31m[!] No accessible directories found\033[0m")

        elif choice == "4":  # Sensitive File Finder
            files = find_sensitive_files(url)

            if files:
                save_path = storage_path.replace(".txt", "_sensitive.txt")
                if save_results(files, save_path, "sensitive"):
                    print(f"\n\033[1;32mSensitive file results saved to: \033[1;35m{save_path}\033[0m")
            else:
                print("\n\033[1;31m[!] No sensitive files found\033[0m")

        elif choice == "5":  # Full Reconnaissance Scan
            print("\n\033[1;33m[+] Initiating Full Reconnaissance Scan\033[0m")

            # JavaScript scan
            print("\033[1;36m[+] Starting JavaScript File Scan\033[0m")
            js_links, _ = get_js_files(url)
            if js_links:
                save_results(js_links, storage_path, "js")

            # Subdomain scan
            print("\033[1;36m[+] Starting Subdomain Discovery\033[0m")
            domain = urlparse(url).netloc
            subdomains = find_subdomains(domain, subdomain_wordlist)
            if subdomains:
                save_path = storage_path.replace(".txt", "_subdomains.txt")
                save_results(subdomains, save_path, "subdomains")

            # Directory scan
            print("\033[1;36m[+] Starting Hidden Directory Scan\033[0m")
            directories = find_hidden_directories(url, directory_wordlist)
            if directories:
                save_path = storage_path.replace(".txt", "_directories.txt")
                save_results(directories, save_path, "directories")

            # Sensitive file scan
            print("\033[1;36m[+] Starting Sensitive File Scan\033[0m")
            files = find_sensitive_files(url)
            if files:
                save_path = storage_path.replace(".txt", "_sensitive.txt")
                save_results(files, save_path, "sensitive")

            print("\n\033[1;32m[+] Full reconnaissance scan completed!\033[0m")

        elif choice == "6" or choice.lower() == "exit":
            print("\n\033[1;36mTerminating session...\033[0m")
            break

        else:
            print("\n\033[1;31m[!] Invalid selection. Please choose 1-6.\033[0m")

        print("\n" + "=" * 65)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[1;31mOperation aborted by user!\033[0m")
        sys.exit(1)
