# PENETRATION-TESTING-TOOL

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: SHABNAM SHARMA

*INTERN ID*: CT12WE04

*DOMAIN*: CYBER SECURITY & ETHICAL HACKING

*DURATION*: 12 WEEKS

*MENTOR*: NEELA SANTHOSH KUMAR 

## DESCRIPTION OF THE TASK 

# BUILD A TOOLKIT WITH MULTIPLE MODULES (E.G., PORT SCANNER, BRUTE-FORCER) FOR PENETRATION TESTING

# A PYTHON-BASED MODULAR TOOLKIT WITH DETAILED DOCUMENTATION

# Introduction

The Penetration Testing Toolkit is a beginner-friendly, Python-based project designed to demonstrate fundamental concepts of ethical hacking. It includes two key modules: a Port Scanner that checks for open ports on a target system, and a Brute-Force Tool that attempts to guess passwords using a custom wordlist. The toolkit is modular, making it easy to expand with additional features or tools in the future.

To relate it to daily life: imagine your computer is like a house. The port scanner checks which doors or windows are open, while the brute-forcer tries different keys to see which one unlocks the front door. This project allows you to act like a digital security inspector, identifying vulnerabilities before someone with bad intentions does.

# Main Features

1. Modular Architecture
The toolkit is built with a clean and extensible module-based structure, allowing seamless integration of additional tools in the future (e.g., vulnerability scanners, directory brute-forcers, etc.). Each feature is organized within its own Python module for clarity and maintainability.

2. Port Scanning Module
Implements TCP port scanning using Python’s socket module. It systematically attempts connections to a range of ports on a target IP, identifying open ports and potential network entry points—an essential first step in reconnaissance.

3. Brute-Force Attack Simulator
A simulation of a password brute-force attack that reads from a user-defined wordlist file. It attempts each password against a hypothetical login system, helping users understand how easily weak passwords can be exploited.

4. Custom Wordlist Support
Users can supply their own wordlist file for the brute-force module, allowing for flexible testing scenarios. This promotes better understanding of dictionary-based attacks.

5. Command-Line Interface (CLI)
A user-friendly interface built with Python’s argparse module, allowing users to specify the target, module, and wordlist directly via terminal commands. This provides a hands-on experience similar to real-world penetration testing tools.

6. Beginner-Friendly Design
No external libraries are required. The toolkit uses only Python’s built-in modules and includes clear output messages, making it ideal for students, educators, or beginners exploring cybersecurity concepts.

# How It Works

1. The user runs the toolkit using command-line arguments, specifying a module (e.g., `port_scan` or `brute_force`) and the target.
   
2. The `main.py` script uses `argparse` to parse user input.
   
3. Based on the selected module:
   - For **port scanning**, it scans ports 1-10 (customizable) on the target IP using TCP sockets.
   - For **brute-force**, it loads a wordlist file and simulates trying each password on a fake login system.
     
4. The output is printed to the terminal showing scan results or brute-force attempts.

# LIMITATIONS

1. Only scans ports 1–10 (limited port range).

2. Brute-force is simulated; doesn't interact with real login forms.

3. No multithreading; runs sequentially (may be slow).

4. No UDP scanning or banner grabbing support.

5. Basic error handling (no logging or advanced reporting).

6. No live target verification before scanning.

7. Meant for educational use only — not for real-world attacks.

8. Doesn’t support full authentication systems or sessions.

9. No GUI — CLI-based only.

10. Not tested for production or large-scale targets.

## OUTPUT

![image](https://github.com/user-attachments/assets/e31a1a6b-0fea-4829-a405-821719da2b1e)

