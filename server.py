from flask import Flask, render_template, request

app = Flask(__name__)

# # ルートにおいて、index.htmlをレンダリングさせる
@app.route('/')
def index():
    title = "Auto-Generator of Template Message"
    jsonFile = {"title": "sample_title", "desc": "sample_desc"}
    return render_template('index.html', title=title, json=jsonFile)

# # testというリクエスト受けた時に、実行する関数
@app.route('/exchangeData', methods=['GET', 'POST'])
def exchangeData():
    if request.method == 'GET':
        print('GET Request')
        res = request.args.get('get_value')
    elif request.method == 'POST':
        print('POST Request')
        res = request.form['post_value']
    return res


# # Localhostを立てるためのコマンド
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
