# -*- coding:utf-8 -*-
# Author:ZDY
# Date: 2024/3/29 10:29 AM

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

#top k

#分享-生成二维码


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
