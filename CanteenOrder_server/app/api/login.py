from flask import jsonify, request
from app.api import bp
from app.database import db
import json

@bp.route('/login', methods=['GET'])
def getUser():
    """获取用户信息"""
    data = request.args.get('telnumber')
    telnumber = int(data)
    getUser_sql = "select * from user where telnumber = {}".format(telnumber)

    user = db.get_data_DB(getUser_sql)
    print(user)
    return jsonify(user[0])

@bp.route('/signup', methods=['POST'])
def insertUser():
    """新增用户信息"""
    cnt = db.get_data_DB("select count(*) from user")[0][0]
    data = request.data
    data = json.loads(request.data)
    insertUser_sql = "insert into user values({}, '{}', '{}', '{}')".format(cnt, data['username'],
                                                                      data['telnumber'], data['password'])
    db.update_DB(insertUser_sql)
    return jsonify(cnt)
