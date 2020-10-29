from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test', methods=['GET'])
def test_get():
    received_title = request.args.get('given_title')
    print(received_title)
    return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})

@app.route('/test', methods=['POST'])
def test_post():
    received_title = request.form('given_title')
    print(received_title)
    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)