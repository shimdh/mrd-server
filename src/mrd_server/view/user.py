# -*- coding: utf-8 -*-

from flask import request
from ..mrd_server.util.protocol import ProtocolTypes, ResultCodes
from ..mrd_server.util.checkdata import checkContainKeys


def register():
    result = dict(
        type=ProtocolTypes.RegisterUser,
        result=ResultCodes.Success
    )

    if request.form['data']:
        got_data = json.loads(request.form['data'])

        from_keys = ['nickname', 'password']
        if checkContainKeys(from_keys, got_data):
            if got_data['nickname'] == '' or got_data['password'] == '':
                result["result"] = ResultCodes.InputParamError
            else:
                if len(got_data['nickname']) < 4:
                    result['result'] = ResultCodes.ShortNickname
                elif len(got_data['password']) < 4:
                    result['result'] = ResultCodes.ShortPassword
                else:
                    import re
                    check_all_letters = lambda given_value: re.match("^[A-Za-z0-9_-]*$", given_value)
                    if (
                        not check_all_letters(got_data['nickname']) or
                        not check_all_letters(got_data['password'])
                    ):
                        result['result'] = ResultCodes.InputParamError
                    else:
                        reserved_nickname = [
                            'system', 'admin', 'administrator', 'root'
                        ]
                        if got_data['nickname'] in reserved_nickname:
                            result["result"] = ResultCodes.InputParamError
                        else:
                            if User.query.filter_by(
                                    nickname=got_data['nickname']).first():
                                result['result'] = ResultCodes.NicknameExist
                            else:
                                user_data = User(
                                    got_data['nickname'],
                                    got_data['password']
                                )
                                db_session.add(user_data)
                                result['result'] = commitData()
        else:
            result["result"] = ResultCodes.InputParamError
    else:
        result["result"] = ResultCodes.AccessError

    return str(json.dumps(result))

register.methods = ['POST']