from flask import jsonify, request
from app.api import bp
from app.database import db
import json

userID = 0

@bp.route('/getUserInfo', methods=['GET'])
def getUserInfo():
    """获取用户信息"""
    getUserInfo_sql = "select * from user where userID = {}".format(userID)

    userinfo = db.get_data_DB(getUserInfo_sql)
    print(userinfo)
    return jsonify(userinfo[0])

@bp.route('/updateUserInfo', methods=['PUT'])
def updateUserInfo():
    """"更改用户信息"""
    data = json.loads(request.data)
    updateUserInfo_sql = "update user set {} = '{}' where userID = {}".format(list(data.keys())[0],
                                                                              list(data.values())[0], userID)
    print(updateUserInfo_sql)
    return jsonify(db.update_DB(updateUserInfo_sql))

@bp.route('/getDeliveredInfo', methods=['GET'])
def getDeliveredInfo():
    """获取收货信息"""
    getDeliveredInfo_sql = "select * from deliveredinfo where userID = {}".format(userID)
    userinfo = db.get_data_DB(getDeliveredInfo_sql)
    print(userinfo)
    return jsonify(userinfo)

@bp.route('/insertDeliveredInfo', methods=['POST'])
def insertDeliveredInfo():
    """新增收货信息"""
    cnt = db.get_data_DB("select count(*) from deliveredinfo")[0][0]
    data = json.loads(request.data)
    InsertDeliveredInfo_sql = "insert into deliveredinfo values({}, {}, '{}', '{}', '{}')".format(cnt, userID,
                                                                                                list(data.values())[0],
                                                                                                list(data.values())[1],
                                                                                                list(data.values())[2])
    print(InsertDeliveredInfo_sql)
    db.update_DB(InsertDeliveredInfo_sql)
    # updateUserInfo_sql = "update user set "
    return jsonify(cnt)

@bp.route('/updateDeliveredInfo', methods=['PUT'])
def updateDeliveredInfo():
    """"更改用户信息"""
    data = json.loads(request.data)
    updateDeliveredInfo_sql = "update deliveredinfo set {} = '{}' where {} = {}".format(list(data.keys())[1],
                                                                                        list(data.values())[1],
                                                                                        list(data.keys())[0],
                                                                                        list(data.values())[0])
    print(updateDeliveredInfo_sql)
    return jsonify(db.update_DB(updateDeliveredInfo_sql))
