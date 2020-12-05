# hw4

## get homework

zoom in, a link is on upper left

```sh
https://tinyurl.com/nice560h4
```

## overflow

```sh
# disable ASLR
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
# turn off NX， gcc flag
gcc -fno-stack-protector -z execstack

# run demo to get address from terminal. In my vm, buffer_ptr: 0x555555558040, func_ptr 0x555555558140 change those in attack.asm
./demo
```

attack asm

```asm
; https://en.wikibooks.org/wiki/X86_Assembly/Interfacing_with_Linux#syscall
; http://6.s081.scripts.mit.edu/sp18/x86-64-architecture-guide.html
mov rax, 1   ; use the `write` [fast] syscall
mov rdi, 1   ; write to stdout, 1st arg
mov rsi, buffer_ptr+message-$$ ; msg address, 2nd arg
mov rdx, message_len  ; msg len, 3th arg
syscall         ; make syscall
```

## backup with rsnapshot

[guide](https://wiki.archlinux.org/index.php/Rsnapshot)

### set up ssh

```sh
sudo ssh-keygen
sudo ssh-copy-id <client addr>
```

### config rsnapshot

on backup server

```sh
sudo apt-get install rsnapshot -y
sudo mkdir /backup
sudo chmod 777 /backup
```

edit conf

```conf
snapshot_root   /backup
cmd_ssh /usr/bin/ssh
retain  nightly 7
retain  weekly  4
backup  <netID>@<vm addr>:/home/<netID> netID/
```

run test

```sh
rsnapshot configtest
```

backup

```sh
sudo rsnapshot nightly
sudo rsnapshot weekly
```

### honeypot

set up EC2 free tier, allow inbound traffic from 60022

[crowie](https://cowrie.readthedocs.io/en/latest/INSTALL.html)

```sh
sudo vi /etc/ssh/sshd_config
sudo yum install git python-virtualenv libssl-dev libffi-dev build-essential libpython3-dev python3 authbind virtualenv -y
git clone http://github.com/cowrie/cowrie
cd cowrie
vi etc/cowrie.cfg
pip install --upgrade pip
pip install --upgrade -r requirements.txt
bin/cowrie start
```

access honeypot as root, input random string as password

```sh
ssh root@<ec2 ip> -p <port num>
```

[change port](https://cowrie.readthedocs.io/en/latest/INSTALL.html#authbind)

log

```sh
sudo vi var/log/cowrie/cowrie.log
sudo vi var/log/cowrie/cowrie.json
```

### DoS

kali

```sh
git clone https://github.com/dotfighter/torshammer.git
chmod 777 torshammer.py
./torshammer.py -t <ip addr> -r 512
time curl  http://vcm-16036.vm.duke.edu/
```

### shell

#### dog

```sh
curl http://people.duke.edu/~tkb13/images/reg-chair.jpg | sha512sum
```

#### ping

```sh
for i in {16000..16100}; do
    ping vcm-$i.vm.duke.edu -w 1 -c 1 2>&1 | grep -qP "1 received" && echo "vcm-$i.vm.duke.edu ok"
    ping vcm-$i.vm.duke.edu -w 1 -c 1 2>&1 | grep -qP "not known|0 received" && echo "vcm-$i.vm.duke.edu down"
done
```

#### bin file

```sh
strings cryptotest.pyc
hd cryptotest.pyc
```

#### md5

```sh
find /usr/lib/python3.7 -name "*.py" -exec md5sum '{}' \;
```

### logs

#### Reconnaissance

previous files are normal

file iasgcap_00011_20130204070402: many ssh with new keys from same ip. possible ssh dictionary attack

#### Actual SSH Attacks

file iasgcap_00011_20130204070402: ssh new keys

#### Successful SSH authentication

file iasgcap_00012_20130204080402: normal ssh login

#### External Tools Downloaded

file iasgcap_00012_20130204080402: ftp

#### External Target attacks

file iasgcap_00012_20130204080402: host ssh other ip
