from flask import jsonify, request
from app.api import bp
from app.database import db
import json

userID = 0

@bp.route('/getuserInfo', methods=['GET'])
def getUserInfo():
    """获取用户信息"""
    getUserInfo_sql = "select * from user where userID = {}".format(userID)

    userinfo = db.get_data_DB(getUserInfo_sql)
    return jsonify(userinfo[0])

@bp.route('/updateUserInfo', methods=['POST'])
def updateUserInfo():
    """"更改用户信息"""
    data = json.loads(request.data)
    updateUserInfo_sql = "update user set {} = '{}' where userID = {}".format(list(data.keys())[0], list(data.values())[0], userID)
    print(updateUserInfo_sql)
    return jsonify(db.update_DB(updateUserInfo_sql))