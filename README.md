XE-Finder - Professional Infromation & Security Scanner

https://img.shields.io/badge/Developed%2520by-Netrindx%2520Solutions-blue?style=for-the-badge
https://img.shields.io/badge/Python-3.8%252B-blue?style=for-the-badge&logo=python
https://img.shields.io/badge/License-MIT-green?style=for-the-badge

https://screenshot.png
Overview

The Web Reconnaissance Suite is a professional security scanner developed by Netrindx Solutions for comprehensive web reconnaissance operations. This powerful tool enables security professionals to perform in-depth scanning and enumeration of web targets, identifying potential vulnerabilities and gathering critical intelligence.

With its modular design and comprehensive scanning capabilities, the Web Reconnaissance Suite is an essential tool for penetration testers, security researchers, and IT professionals conducting security assessments.
Key Features

    JavaScript File Discovery: Identify all JavaScript files on a target domain

    Subdomain Enumeration: Discover hidden subdomains using powerful wordlists

    Hidden Directory Scanning: Uncover concealed directories and paths

    Sensitive File Detection: Locate potentially sensitive files and endpoints

    Full Reconnaissance Mode: Comprehensive scan combining all reconnaissance modules

    Custom Wordlist Support: Use your own specialized wordlists

    Results Export: Save findings to text files for further analysis

Installation
Prerequisites

    Python 3.8+

    pip package manager

Setup Instructions

    Clone the repository:

bash

git clone https://github.com/netrindx/web-reconnaissance-suite.git
cd web-reconnaissance-suite

    Install required dependencies:

bash

pip install -r requirements.txt

    Run the scanner:

bash

python scanner.py

Usage
Basic Operation

    Launch the scanner

    Enter the target URL when prompted

    Specify the output file path for results

    Choose between default or custom wordlists

    Select the desired scan type

Command Options
Option	Description
-u, --url	Specify target URL directly
-o, --output	Set output file path
-m, --module	Select specific module to run
--subdomain-wordlist	Custom subdomain wordlist path
--directory-wordlist	Custom directory wordlist path
--full-scan	Perform full reconnaissance scan
Example Commands
bash

# Basic scan with interactive prompts
python scanner.py

# Directly scan a target with full reconnaissance
python scanner.py -u https://example.com -o results.txt --full-scan

# Run specific module (subdomain discovery)
python scanner.py -u https://example.com -m subdomain

Scan Modules
1. JavaScript File Finder

Identifies all JavaScript files accessible on the target domain, which can reveal application structure and potential vulnerabilities.
2. Subdomain Discovery

Enumerates subdomains using DNS brute-forcing techniques with comprehensive wordlists.
3. Hidden Directory Scanner

Discovers hidden directories and paths that may contain sensitive information or administrative interfaces.
4. Sensitive File Finder

Locates potentially sensitive files such as configuration files, backups, and credential storage.
5. Full Reconnaissance Scan

Comprehensive scan combining all modules for complete target reconnaissance.
Wordlists

The scanner includes carefully curated default wordlists optimized for effective reconnaissance. Users can also provide custom wordlists for specialized scanning requirements.

Default wordlists are located in:

    wordlists/subdomains.txt

    wordlists/directories.txt

Sample Output
text

[+] Initiating Full Reconnaissance Scan
[+] Starting JavaScript File Scan
[+] Starting Subdomain Discovery

[+] Scanning for subdomains on example.com
[+] Loaded 15 subdomains for scanning
[+] Found: www.example.com (93.184.216.34)
[+] Found: mail.example.com (104.16.123.96)
[+] Found: dev.example.com (192.0.78.25)

[+] JavaScript Files Found:
  - https://example.com/main.js
  - https://example.com/analytics.js
  - https://example.com/util.js

[+] Sensitive Files Discovered:
  - https://example.com/.env
  - https://example.com/backup.zip

Contribution

We welcome contributions from the security community! To contribute:

    Fork the repository

    Create your feature branch (git checkout -b feature/your-feature)

    Commit your changes (git commit -am 'Add some feature')

    Push to the branch (git push origin feature/your-feature)

    Open a pull request

Please ensure your code follows PEP8 guidelines and includes appropriate tests.
License

This project is licensed under the MIT License - see the LICENSE file for details.
Disclaimer

This tool is intended for legal security testing and research purposes only. Never use it against systems without explicit permission. The developers assume no liability and are not responsible for any misuse or damage caused by this program.
About Netrindx Solutions

Netrindx Solutions is a cybersecurity firm specializing in offensive security research and defensive strategy development. We provide cutting-edge security solutions to organizations worldwide.

Developed with ❤️ by the security team at Netrindx Solutions
