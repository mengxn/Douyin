import json
from urllib.parse import urlparse

from flask import Flask, render_template, request
from douyin import Douyin

app = Flask(__name__)

douyin_domains = [
    'v.douyin.com'
]
schemes = [
    'https', 'http'
]


@app.route('/')
def index():
    return render_template('index.html', search_result=None)


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    url_parse = urlparse(query)
    if url_parse.scheme not in schemes or url_parse.netloc not in douyin_domains:
        return render_template('index.html', error='未找到链接, 请确保输入的链接以"http://" 或者 "https://" 开头')

    urls = Douyin().run(query)
    return render_template('index.html', search_result=urls)


@app.route('/mix', methods=['GET'])
def mix():
    query = request.args.get('url')
    url_parse = urlparse(query)
    if url_parse.scheme not in schemes or url_parse.netloc not in douyin_domains:
        return render_template('index.html', error='未找到链接, 请确保输入的链接以"http://" 或者 "https://" 开头')

    return json.dumps(Douyin().run(query))


if __name__ == '__main__':
    app.run(debug=True)
    pass
