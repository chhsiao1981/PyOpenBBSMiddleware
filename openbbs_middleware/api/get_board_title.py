# -*- coding: utf-8 -*-


def get_board_title(bid, params):
    '''XXX mock-data'''
    result = {
        'bsn': 'sn-%s' % (bid),
        'bid': bid,
        'title': '這是 title',
        'flag': 0,
        'boardType': 1,
        'cat': '站務',
        'onlineCount': 100000,
        'moderators': [
            {
                'usn': 'sn-teemo',
                'uid': 'teemo',
            },
            {
                'usn': 'sn-okcool',
                'uid': 'okcool',
            },
        ],
        'read': False,
    }

    return None, result
