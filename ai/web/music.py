# -*- coding:utf-8 -*-
# Author:ZDY
# Date: 2024/3/29 10:29 AM

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/')
def hello_world():
    return 'Hello, World!'


# 相似 top k
@app.route('/similar', methods=['POST'])
def post_json():
    data = request.get_json(force=True)
    # 这里你可以处理你的数据
    print(data)

    # 返回一个响应
    return jsonify({'code': 200, 'data': data}), 200



# 分享-生成二维码




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)
