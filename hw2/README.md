# hw2

## 0 get real hw2

on mac

## generate rsa key

```sh
ssh-keygen -m pem
```

## private key to pem file

```sh
openssl rsa -in .ssh/id_rsa -text > .ssh/id_rsa.pem
```

download the enc file and scp to kali server

## [enc file](http://target.colab.duke.edu:8000/)

now Kali

## decrypt enc

```sh
openssl rsautl -decrypt -inkey id_rsa.pem -in secret-<netid>.key.enc -out key.bin
```

## decrypt dat

```sh
openssl enc -aes256 -d -K <key in key.bin> -in data-<netid>.dat -out outlayer -iv 00000000000000000000000000000000
```

## check sha1

in homework discription, sha1 of out layer

```sh
998f7d4bd40948c6a5a6139b5893e550abc9aa89
```

```sh
sha1sum outlayer
```

if match, proceed

## inner layer

get real hostname

```sh
dig target.colab.duke.edu | grep 'vcm-'
```

current hostname

```sh
vcm-15743.vm.duke.edu
```

use veracrypt to open outlayer, password is the hostname

## 9 vpn

turn off any vpn before proceed

### server

on ubuntu server(don't use kali)

```sh
git clone https://github.com/trailofbits/algo.git
cd algo

sudo apt install -y python3-virtualenv

python3 -m virtualenv --python="$(command -v python3)" .env &&
  source .env/bin/activate &&
  python3 -m pip install -U pip virtualenv &&
  python3 -m pip install -r requirements.txt

./algo
```

choose ubuntu server

all default, except the public ip, input your vm addr

### client

find correspond docs in

```sh
docs
```

i use mac, download

```sh
configs/<vm addr>/ipsec/apple/laptop.mobileconfig
```

double click it, mac will install config

then go to network, select vpn, and connect

check [whoer](https://whoer.net/)

if ip matches vm ip, then success

## 10 tor

install tor browser, i use brew

```sh
brew cask install tor-browser
```

open tor, connect then open normal browser(firefox, chrome)

visit [whoer](https://whoer.net/)

## 13 ssl

[guide](https://gist.github.com/fntlnz/cf14feb5a46b2eda428e000157447309)

### generate private key

```sh
openssl genrsa -out CA-key.pem
```

### generate x.509 cert

```sh
openssl req -new -key CA-key.pem -x509 -out CA-cert.pem
```

### install root ca

[guide](https://docs.microsoft.com/en-us/skype-sdk/sdn/articles/installing-the-trusted-root-certificate)

### sign linux server

create private key

```sh
openssl genrsa -out server.pem
```

create signed request, common domain name is server domain name

```sh
openssl req -new -key server.pem -out server.csr
```

sign request

```sh
openssl x509 -req -in server.csr -CA CA-cert.pem -CAkey CA-key.pem -CAcreateserial -out server.crt
```

### install server on linux

```sh
sudo apt install apache2
```

### server config

enable ssl module

```sh
sudo a2enmod ssl
sudo a2ensite default-ssl
```

check cert & key location in `/etc/apache2/sites-enabled/default-ssl.conf`
replace it with the server cert & key

```sh
sudo vi /etc/ssl/certs/ssl-cert-snakeoil.pem
sudo vi  /etc/ssl/private/ssl-cert-snakeoil.key
```

```sh
sudo systemctl start apache2
```

check server status from local terminal

```sh
nc -vz <server-domain> 443
```
