from flask import Flask, render_template, request

app = Flask(__name__)

# # ルートにおいて、index.htmlをレンダリングさせる
@app.route('/')
def index():
    _title = "Auto-Generator of Template Message"
    _messageFile = {"title": "sample_title_init", "desc": "sample_desc_init"}
    return render_template('index.html', title=_title, messageFile=_messageFile)

# # testというリクエスト受けた時に、実行する関数
@app.route('/exchangeMessage', methods=['GET', 'POST'])
def exchangeMessage():
    _title = "Auto-Generator of Template Message"
    if request.method == 'GET':
        print('GET Request')
        # res = request.args.get('title_input')
    elif request.method == 'POST':
        print('POST Request')
        print(request.form['title_input'])
        print(request.form['description_input'])
        _messageFile = {"title": str(
            request.form['title_input']), "desc": str(request.form['description_input'])}

    return render_template("index.html", title=_title, messageFile=_messageFile)


# # Localhostを立てるためのコマンド
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
