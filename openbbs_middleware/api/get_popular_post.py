# -*- coding: utf-8 -*-


def get_popular_post(params):
    '''XXX fake-data'''
    result = {
        'list': [
            {
                'pid': 'pid',
                'postTime': 1234567891,
                'updateTime': 1234567891,
                'title': '最新的文章',
                'bid': 'WhoAmI',
                'read': False,
                'flag': 0,
                'cat': '問題',
                'nReader': 1,
                'nRecommend': -1000,
            },
        ],
        'next': 'pid2',
        'nextTime': 1234567890,
    }

    return None, result
