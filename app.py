from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/board", methods=["POST"])
def board_post():
    title_receive = request.form['title_give']
    comment_receive = request.form['comment_give']

    doc = {
        'title':title_receive,
        'comment':comment_receive
    }

    db.boarduser.insert_one(doc)

    return jsonify({'msg': '댓글 완료'})

@app.route("/board", methods=["GET"])
def board_get():
    board_list = list(db.boarduser.find({}, {'_id': False}))
    return jsonify({'boards': board_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)