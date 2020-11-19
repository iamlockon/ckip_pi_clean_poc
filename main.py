from ckiptagger import data_utils, construct_dictionary, WS, POS, NER
from utils.file_io import read_article
import re, time


name_t = "NAME"
email_t = "EMAIL"
phone_t = "PHONE"

# Get contents
pre_read_post = time.time()
# url = "https://www.ptt.cc/bbs/SHU-MISM97/M.XXXXXX2.A.BB6.html" # will find email
url = "https://www.ptt.cc/bbs/Gossiping/M.1605713218.A.1C9.html" # will find name
title, content, push_list = read_article(url)
post_read_post = time.time()
print(f"post read, took {post_read_post - pre_read_post} seconds...")

# init list, sentinel
res = []
found = 0
# find emails, phones(regex)
print("========email/phones stage=========")
pre_regex = time.time()
for txt in (title, content):
    # emails
    m = re.search(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]*[a-zA-Z])", txt)
    if m != None:
        res.append({"path": url, "matchType": email_t, "match": m.group(0)})
        found = 1
        break # once we add one post to list, we abort
    # phones
    p = re.search(r"((\d{2,3}-?|\(\d{2,3}\))\d{3,4}-?\d{4}|(?:0|886-?)9\d{2}-?\d{3}-?\d{3})", txt) # local/mobile regex
    if p != None:
        res.append({"path": url, "matchType": phone_t, "match": p.group(0)})
        found = 1
        break # once we add one post to list, we abort
post_regex = time.time()
print(f"phone,email check finished, found: {found == True}, took {post_regex - pre_regex} seconds...")

# NER, time-consuming.
end_time = post_regex
if not found:
    print("=======names stage=====")
    pre_load_model = time.time()
    ws = WS("./data")
    pos = POS("./data")
    ner = NER("./data")
    post_load_model = time.time()
    print(f"model loaded, took {post_load_model - pre_load_model} seconds...")

    pre_ckip = time.time()
    sentence_list = [title, content]
    # ws, pos, ner in order
    ws_list = ws(sentence_list)
    pos_list = pos(ws_list)
    entity_list = ner(ws_list, pos_list)
    del ws, pos, ner
    post_ckip = time.time()
    print(f"ckip-preprocessing(ws,pos,ner) finished, took {post_ckip - pre_ckip} seconds...")
    # find names
    pre_entity = time.time()
    for i, sentence in enumerate(sentence_list):
        for _,_,t,word in sorted(entity_list[i]):
            if t == 'PERSON':
                res.append({"path": url, "matchType": name_t, "match": word})
                found = 1
                break
        if found: # spare time
            break
    post_entity = time.time()
    end_time = post_entity
    print(f"name check finished, found: {found == True}, took {post_entity - pre_entity} seconds...")

print(f"Found: {found == True}\n Result:\n {res}\n Total run time: [{end_time - pre_read_post}] seconds")
