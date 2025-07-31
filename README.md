

# Subdomain Finder 🔍

A simple tool to discover subdomains of a given domain.  
This project is created for learning and security research purposes only.

## 🚀 Features
- Finds subdomains of a given target
- Fast and lightweight
- Easy to use from the command line

## 📦 Installation

Clone this repository:
# NOTE:- whenever you want chnage the wordlist just give the location of the file in the code.
## The whole code was developed in python
And the list.txt is taken from[seclist]  https://github.com/danielmiessler/SecLists/blob/master/Discovery/DNS/subdomains-top1million-110000.txt?raw=true

## The whole code was developed in python


📂 Data Source
This project uses a wordlist file for subdomain enumeration:

File: list.txt

Original Path / Source: SecLists — Discovery/DNS

(SecLists is a popular collection of multiple types of lists for security assessments.)

🙌 Credits
Wordlist: Daniel Miessler's SecLists

Tool Development: Chaitanya Ch


```bash
git clone https://github.com/iamchaitanya-6/subdomain-finder.git
cd subdomain-finder
python subfinder.py -d example.com



