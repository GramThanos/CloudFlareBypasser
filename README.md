# R-CloudFlareBypasser
This script use for bypass cloudlfare and get real up :) by tring to find the IP of possible subdomains.


# Usage

Clone repo and install requirements
```bash
git clone https://github.com/GramThanos/CloudFlareBypasser.git
cd CloudFlareBypasser
```

Call script
```bash
python3 R-CloudFlareBypasser.py
```

If you want to check a bigger list of subdomains, update the existing one using one from [SecLists](https://github.com/danielmiessler/SecLists/tree/master/Discovery/DNS)
e.g. using the top 50000 subdomains:
```bash
wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/deepmagic.com-prefixes-top50000.txt -O dom.txt
```
