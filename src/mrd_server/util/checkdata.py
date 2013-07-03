# -*- coding: utf-8 -*-

from ..mrd_server.model.user import User
import datetime
from database import db_session
from sqlalchemy import exc


def checkSessionId(got_session_id):
    got_user = User.query.filter_by(session_id=got_session_id).first()
    if not got_user:
        return ResultCodes.SessionIdNonExist, None
    else:
        if got_user.session_date < (
                datetime.datetime.now() - datetime.timedelta(minutes=20)):
            got_user.session_id = ''
            db_session.add(got_user)
            try:
                db_session.commit()
                return ResultCodes.SessionIdExpired, None
            except exc.SQLAlchemyError:
                return ResultCodes.DBInputError, None
        else:

            got_user.session_date = datetime.datetime.now()
            db_session.add(got_user)
            try:
                db_session.commit()
                return ResultCodes.Success, got_user
            except exc.SQLAlchemyError:
                return ResultCodes.DBInputError, None


def checkContainKeys(my_list, my_dict):
    return len(
        [x for x in my_list if x in my_dict and my_dict[x]]) == len(my_list)


def commitData():
    try:
        db_session.commit()
        return ResultCodes.Success
    except exc.SQLAlchemyError:
        return ResultCodes.DBInputError