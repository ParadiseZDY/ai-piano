# -*- coding:utf-8 -*-
# Author:ZDY
# Date: 2024/3/29 10:29 AM
import json
import random

from flask import Flask, request, jsonify
from flask_cors import CORS

from ai.web import api

app = Flask(__name__)
CORS(app)


def init_app():
    # 1. 读取 json 文件
    with open('../data/target.json', 'r') as file:
        data = json.load(file)

    # 2. 排序 json 文件
    sorted_data = sorted(data, key=lambda x: x['likeCount'] + x['degree'] * 10 - x['unlikeCount'], reverse=True)

    # 3. 取前100个
    top_100 = sorted_data[:100]

    # 将结果保存为全局变量
    app.config['TOP_100'] = top_100
    print("App initialization complete.")


# 首页
@app.route('/')
def hello_world():
    return '破晓！！！!'


# 随机来一首
@app.route('/rand')
def rand_item():
    # 从 TOP_100 中随机抽取一个对象
    item = random.choice(app.config['TOP_100'])
    # 将对象转为 JSON 格式并返回
    return jsonify({'code': 200, 'data': item}), 200


# top k
@app.route('/top')
def top():
    topK = request.args.get("topK", 10)
    if topK > 100:
        topK = 10
    top_N = app.config['TOP_100'][:topK]

    # 返回数据
    retrunData = {}
    retrunData['topK'] = topK;
    retrunData['rendered'] = top_N;
    return jsonify({'code': 200, 'data': retrunData}), 200


# 相似 top k
@app.route('/similar', methods=['POST'])
def post_json():
    data = request.get_json(force=True)
    print(data)

    # 获取topK
    rendered = data['rendered']
    topNum = data['topK']
    if topNum <= 0:
        topNum = 5
    if topNum > 10:
        topNum = 10
    topRendered = api.topK(rendered, topNum, app.config)

    # 返回数据
    retrunData = {}
    retrunData['topK'] = topNum
    retrunData['rendered'] = topRendered

    # 返回一个响应
    return jsonify({'code': 200, 'data': retrunData}), 200


@app.route('/aiCreation', methods=['POST'])
def aiCreation():
    data = request.get_json(force=True)
    print(data)

    # 获取topK
    rendered = data['rendered']

    item = random.choice(app.config['TOP_100'])
    # 将对象转为 JSON 格式并返回
    return jsonify({'code': 200, 'data': item}), 200


if __name__ == '__main__':
    init_app()
    app.run(host='0.0.0.0', port=9999, debug=True)
