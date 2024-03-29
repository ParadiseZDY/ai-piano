# -*- coding:utf-8 -*-
# Author:ZDY
# Date: 2024/3/29 10:29 AM

from flask import Flask, jsonify
from flask import request

from ai.service import search

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# top k
@app.route('/top')
def top():
    resp = search.queryWithVector(10, request.args.get("query"))
    return jsonify(resp)


# 分享-生成二维码


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
