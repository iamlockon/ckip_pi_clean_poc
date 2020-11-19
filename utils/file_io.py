from utils.ptt import login, logout
from PyPtt import PTT
import sys
bot = login()

# read uri, return title, content, push list
def read_article(url):
    board, aid = bot.get_aid_from_url(url)
    post_info = bot.get_post(board, aid)
    if post_info is None:
        print('post_info is None')
        return ""

    if post_info.delete_status != PTT.data_type.post_delete_status.NOT_DELETED:
        if post_info.delete_status == PTT.data_type.post_delete_status.MODERATOR:
            print(f'[板主刪除][{post_info.author}]')
        elif post_info.delete_status == PTT.data_type.post_delete_status.AUTHOR:
            print(f'[作者刪除][{post_info.author}]')
        elif post_info.delete_status == PTT.data_type.post_delete_status.UNKNOWN:
            print(f'[不明刪除]')
        return ""

    if post_info.is_lock:
        print('[鎖文]')
        return ""

    if not post_info.pass_format_check:
        print('[不合格式]')
        return ""

    # title, content and push list 
    title = post_info.title
    content = post_info.content
    push_list = post_info.push_list
    return (title, content, push_list)



if __name__ == "__main__":
    pass