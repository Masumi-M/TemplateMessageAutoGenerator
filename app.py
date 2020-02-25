from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    _title = "Auto-Generator of Template Message"
    _messageFile = {"title": "Title", "desc": "Description"}
    return render_template('index.html', title=_title, messageFile=_messageFile)

@app.route('/exchangeMessage', methods=['GET', 'POST'])
def exchangeMessage():
    _title = "Auto-Generator of Template Message"
    if request.method == 'GET':
        print('GET Request')
    elif request.method == 'POST':
        print('POST Request')
        print(request.form['title_input'])
        print(request.form['description_input'])
        _messageFile = {"title": str(
            request.form['title_input']), "desc": str(request.form['description_input'])}
        print(_messageFile)

    return render_template("index.html", title=_title, messageFile=_messageFile)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
