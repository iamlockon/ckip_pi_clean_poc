# Goal

Identify/Clean PI in ptt posts

# Prequisite

1. setup ckip environment
https://github.com/ckiplab/ckiptagger/wiki/Chinese-README

2. Install `PyPtt`
```
$ pip install pyptt
```
# Usage
1. Create `config.json` according to `config.json.sample`.

2. Run below command.
```
$ python3 main.py
```

# Progress

[V] Extract texts from posts

[V] Identify Phone

[V] Identify Email

[V] Identify Names

[V] Generate matched posts list

# Examples

1. Output if found in email/phone stage:
```
---snip---
[1118 23:48:20][外部] 登入成功
已註冊使用者
post read, took 0.21545720100402832 seconds...
========email/phones stage=========
phone,email check finished, found: True, took 0.0011408329010009766 seconds...
Found: True
 Result:
 [{'path': 'https://www.ptt.cc/bbs/SHU-MISM97/M.XXXXX.html', 'matchType': 'EMAIL', 'match': 'XXXXXXX@gmail.com'}]
 Total run time: [0.21666955947875977] seconds

```
2. Output if found in name stage:

```
---snip---
[1118 23:50:23][外部] 登入成功
已註冊使用者
post read, took 2.306764602661133 seconds...
========email/phones stage=========
phone,email check finished, found: False, took 0.0014760494232177734 seconds...
=======names stage=====
---snip---
model loaded, took 51.79375696182251 seconds...
ckip-preprocessing(ws,pos,ner) finished, took 39.976388931274414 seconds...
name check finished, found: True, took 2.1696090698242188e-05 seconds...
Found: True
 Result:
 [{'path': 'https://www.ptt.cc/bbs/Gossiping/M.1605713218.A.1C9.html', 'matchType': 'NAME', 'match': '張上淳'}]
 Total run time: [94.07862615585327] seconds
```