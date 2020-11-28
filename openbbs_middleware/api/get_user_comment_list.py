# -*- coding: utf-8 -*-


def get_user_comment_list(username, params):
    result = {
        'list': [
            {
                'bid': 'SYSOP',
                'pid': 'pid2',
                'cid': 'cid3',
                'postTime': 1234567891,
                'title': '[公告] 你誰啊, 亂公告',
                'comment': '我是站長',
                'flag': 0,
            },
        ],
        'nextBID': 'Joke',
        'nextPID': 'pid1',
        'nextCID': 'cid2',
        'nextTime': 1234567890,
    }

    return None, result
