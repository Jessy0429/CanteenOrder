from flask import jsonify, request
from app.api import bp
from app.database import db
import json

@bp.route('/insertOrderInfo', methods=['POST'])
def insertOrderInfo():
    """新增订单信息"""
    cnt = db.get_data_DB("select count(*) from `order`")[0][0]
    data = json.loads(request.data)
    print(data)
    InsertOrderInfo_sql = "insert into `order` values({}, {}, {}, {}, {}, '{}', '{}', {})".format(cnt, data['userID'],
                                                                                            data['deliveredID'],
                                                                                            data['dishware'],
                                                                                            data['canteenID'],
                                                                                            data['o_time'],
                                                                                            data['d_time'],
                                                                                            data['status'])
    print(InsertOrderInfo_sql)
    db.update_DB(InsertOrderInfo_sql)
    return jsonify(cnt)

@bp.route('/insertOrderDish', methods=['POST'])
def insertOrderDish():
    """新增订单对应菜品信息"""
    data = json.loads(request.data)
    print(data)
    flag = 1
    orderID = data['orderID'];
    for item in data['ShoppingCart']:
        insertOrderDish_sql = "insert into order_dish values({}, {}, {})".format(item['dishID'], orderID, item['dishnum'])
        print(insertOrderDish_sql)
        flag = flag * db.update_DB(insertOrderDish_sql)
    return jsonify(flag)

@bp.route('/getOrderInfo', methods=['GET'])
def getOrderInfo():
    """获取订单信息"""
    data = request.args.get('userID')
    userID = int(data)
    getDeliveredInfo_sql = "select * from orderinfo where userID = {}".format(userID)
    orderinfo = db.get_data_DB(getDeliveredInfo_sql)
    print(orderinfo)
    data = ()
    for item in orderinfo:
        data = data + ((item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], eval(item[10]), item[11]),)
    print(data)
    return jsonify(data)
