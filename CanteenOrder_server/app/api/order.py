from flask import jsonify, request
from app.api import bp
from app.database import db
import json

userID = 0
@bp.route('/insertOrderInfo', methods=['POST'])
def insertOrderInfo():
    """新增订单信息"""
    cnt = db.get_data_DB("select count(*) from `order`")[0][0]
    data = json.loads(request.data)
    print(data)
    InsertOrderInfo_sql = "insert into `order` values({}, {}, {}, {}, {}, '{}', '{}', {})".format(cnt, userID,
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
