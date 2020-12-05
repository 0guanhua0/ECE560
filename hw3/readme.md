# hw3

## get file format

```sh
file homework3.pdf
```

it's jpeg

## 3

### nmap

[regex](https://regex101.com/r/JWm3Vu/1)

nmap | grep

```sh
nmap 152.3.64.* | grep -Eo "vcm\S+"
```

### log

```sh
wget http://people.duke.edu/~tkb13/courses/ece560/homework/hw3/auth.log && perl -ne '/Invalid.*\sadmin\s.*\s(\d{1,3}\.{1,3}\d{1,3}\.\d{1,3}\.\d{1,3})/ and print"$1\n"' auth.log | sort | uniq
```

breakdown

[regex](https://regex101.com/r/yaASWb/1)

get file

```sh
wget http://people.duke.edu/~tkb13/courses/ece560/homework/hw3/auth.log
```

perl regex then sort then get unique

```sh
perl -ne '/Invalid.*\sadmin\s.*\s(\d{1,3}\.{1,3}\d{1,3}\.\d{1,3}\.\d{1,3})/ and print"$1\n"' auth.log | sort | uniq
```

### web

download all html file

```sh
wget -r http://target.colab.duke.edu/app/
```

```sh
grep '<form>' -r target.colab.duke.edu
```

## regex

### netid

```sh
/[a-zA-Z]{1,3}[\d]+/
```

### url

start with (http|https) use ?: to ignore this group in reference, then ://en.wikipedia.org/wiki/, then use grouping for reference

```sh
/^(?:http|https):\/\/en.wikipedia.org\/wiki\/(.+)/
```

[example](https://regex101.com/r/PHn6Yw/2/)

### pi

[pi](https://www.angio.net/pi/digits.html)

search for 12345, shows up near 47,000, download 100,000

start with 3., any number of digit, 12345, use group for reference

[example](https://regex101.com/r/jyQyLn/2)

grep -E regex -o print matching part

pipe to tr to remove \n

```sh
grep -Eo "(^3\.\d*12345)" pi.txt | tr -d '\n' | md5sum
```

## screen

[guide](https://maojr.github.io/screencheatsheet/)

## hashcat

create input file, format hash:salt

e.g.

```sh
5cf2ff593419bcf3d22c62e65a82128a:ly
```

```sh
hashcat -m 20 -a 3 input --force
```

use mode 20, for salt:md5 hash, a 3 brute force

## john

```sh
wget http://people.duke.edu/~tkb13/courses/ece560/homework/hw3/shadow
```

```sh
screen
john shadow --fork=16
```

```sh
john -show shadow
```

## MFA

[guide](https://www.digitalocean.com/community/tutorials/how-to-set-up-multi-factor-authentication-for-ssh-on-ubuntu-16-04)

first install Google Authenticator on phone, then scan QR code in the end

```sh
sudo apt-get install libpam-google-authenticator
google-authenticator
```

just click yes on setup, then follow guide

to stop MFA, comment following lines

```sh
sudo vi /etc/ssh/sshd_config
#AuthenticationMethods publickey,password publickey,keyboard-interactive
sudo vi /etc/pam.d/sshd
#auth required pam_google_authenticator.so nullok

sudo systemctl restart sshd.service
```

## hydra

store guess user name in user

```sh
hydra -L user -P /usr/share/wordlists/metasploit/adobe_top100_pass.txt ssh://target.colab.duke.edu
```

valid user name: scott

## prompt

[guide](https://www.cyberciti.biz/faq/bash-shell-change-the-color-of-my-shell-prompt-under-linux-or-unix/)

## recon

[regex](https://regex101.com/r/Kvo58S/1)

```sh
input="hosts"
while IFS= read -r line
do
  nmap -sV -Pn "$line" | perl -ne '/Nmap.*for (.*) \((.*)\)/ and print "$1,$2,"' >> res.csv
  nmap -sV -Pn "$line" | perl -ne '/22.*  ([\w .]+) \(/ and print "$1\n"' >> res.csv
done < "$input"
```

## pdf+zip

```sh
zip tmp.zip fd.jpg <public key>
cat hw3.pdf tmp.zip > hw3_poly.pdf
zip -A hw3_poly.pdf
```
