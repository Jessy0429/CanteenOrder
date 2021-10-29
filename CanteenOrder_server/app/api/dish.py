from flask import jsonify, request
from app.api import bp
from app.database import db
import json

@bp.route('/getCanteenInfo', methods=['GET'])
def getCanteenInfo():
    """获取食堂信息"""
    getCanteenInfo_sql = "select * from canteen"

    canteeninfo = db.get_data_DB(getCanteenInfo_sql)
    print(canteeninfo)
    return jsonify(canteeninfo)

@bp.route('/getStoreInfo', methods=['GET'])
def getStoreInfo():
    """获取商家信息"""
    getStoreInfo_sql = "select * from store"

    storeinfo = db.get_data_DB(getStoreInfo_sql)
    print(storeinfo)
    return jsonify(storeinfo)

@bp.route('/getCt_StInfo', methods=['GET'])
def getCt_StInfo():
    """获取食堂商家视图信息"""
    getCt_StInfo_sql = "select * from ct_st"

    ct_stinfo = db.get_data_DB(getCt_StInfo_sql)
    data = ()
    for item in ct_stinfo:
        data = data + ((item[0], eval(item[1])),)
    print(data)
    return jsonify(data)

@bp.route('/getDishInfo/<int:storeID>', methods=['GET'])
def getDishInfo(storeID):
    """获取食堂商家视图信息"""
    getDishInfo_sql = "select * from dish where storeID = {}".format(storeID)
    dishinfo = db.get_data_DB(getDishInfo_sql)
    print(dishinfo)
    return jsonify(dishinfo)