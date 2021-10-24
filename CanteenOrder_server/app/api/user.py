from flask import jsonify
from app.api import bp


@bp.route('/user', methods=['GET'])
def UserInfo():
    """测试 API 是否通"""
    return jsonify('111')