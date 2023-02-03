<h1 align="center">
    TLDbrute
  <br>
</h1>

<h4 align="center">A simple utility to generate domain names with all possible TLDs</h4>


<p align="center">
  <a href="#install">🏗️ Install</a>  
  <a href="#usage">⛏️ Usage</a> 
  <a href="#use-cases">💡 Use Cases</a> 
  <br>
</p>


# Install
```sh
git clone https://github.com/Sybil-Scan/tldbrute
cd tldbrute
pip install .
```


# Usage

```sh
(~) >>> tldbrute -d google.com


 ________   ___  __            __
/_  __/ /  / _ \/ /  ______ __/ /____
 / / / /__/ // / _ \/ __/ // / __/ -_)
/_/ /____/____/_.__/_/  \_,_/\__/\__/


                 - by Sybil Scan Research <research@sybilscan.com>


google.aboutme
google.academy
google.accountant
google.accountants
google.actor
google.addme
............
............
google.adlt
google.adult
google.advisor
google.ae.org
google.afam
```

# Use Cases


Organizations often register/operate under different TLDs (due to a variety of reasons that include different languages, demographic, etc). [TLDbrute](https://github.com/Sybil-Scan/tldbrute) takes a domain name or a list of domains as input and spits out all possible variations of domain names containing different TLDs. Which then can be combined with a another tool such as [dnsx](https://github.com/projectdiscovery/dnsx) to resolve the results.


```sh
(~) >>> tldbrute -d google.com | dnsx -a -resp -silent


 ________   ___  __            __
/_  __/ /  / _ \/ /  ______ __/ /____
 / / / /__/ // / _ \/ __/ // / __/ -_)
/_/ /____/____/_.__/_/  \_,_/\__/\__/


                 - by Sybil Scan Research <research@sybilscan.com>

google.ai [216.239.32.29]
google.boats [216.239.34.21]
google.boats [216.239.32.21]
google.boats [216.239.38.21]
google.boats [216.239.36.21]
google.ca [142.250.206.131]
google.ac [172.217.160.228]
google.ch [172.217.161.3]
............
............
google.co.uk [142.250.76.195]
google.cn [142.250.206.163]
google.cm [142.250.192.195]
google.co [142.250.183.206]
```
