# -*- coding: utf-8 -*-


def get_user_post_list(username, params):
    '''XXX mock-data'''
    result = {
        'list': [
            {
                'pid': 'pid',
                'postTime': 1234567891,
                'updateTime': 1234567891,
                'title': '我～是～誰～？',
                'bid': 'WhoAmI',
                'read': False,
                'flag': 0,
                'cat': '問題',
                'nReader': 1,
                'nRecommend': -1000,
            },
        ],
        'nextBID': 'WhoAmI',
        'nextPID': 'pid2',
        'nextTime': 1234567890,
    }

    return None, result
