from PyPtt import PTT
import json, sys, os

ptt_bot = PTT.API()

def login():
    ID, PASS = "", ""
    cwd = os.path.dirname(__file__)
    try:
        with open(os.path.join(cwd, "../config.json"), 'r') as f:
            credentials = json.load(f)
            ID, PASS = credentials["id"], credentials["passwd"]
        ptt_bot.login(ID, PASS)
    except PTT.exceptions.LoginError:
        ptt_bot.log('登入失敗')
        sys.exit()
    except PTT.exceptions.WrongIDorPassword:
        ptt_bot.log('帳號密碼錯誤')
        sys.exit()
    except PTT.exceptions.LoginTooOften:
        ptt_bot.log('請稍等一下再登入')
        sys.exit()
    except Exception as e:
        ptt_bot.log('未知錯誤: ' + str(e))
        sys.exit()
    ptt_bot.log('登入成功')

    if ptt_bot.unregistered_user:
        print('未註冊使用者')

        if ptt_bot.process_picks != 0:
            print(f'註冊單處理順位 {ptt_bot.process_picks}')

    if ptt_bot.registered_user:
        print('已註冊使用者')
    return ptt_bot

def logout():
    ptt_bot.logout()