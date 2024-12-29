from flask import request, Flask, render_template, redirect, url_for

app = Flask("Mathematics Problem Solver")
names = []


def create_new_record(name):
    names.append(name)
    return names.index(name)


def get_record(uid):
    return names[uid]


def update_record(uid, name):
    names[uid] = name


def delete_record(uid):
    names.remove(names[uid])


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return "<Login Page>"
    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        return {"message": "ok"}, 200


@app.route("/admin")
def admin():
    return redirect(url_for('login'))


@app.route("/")
def render_index_page():
    return render_template("index.html")


@app.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "GET":
        return {"message": "GET request"}, 200
    elif request.method == "POST":
        return {"message": "POST request"}, 200


# Create Operation
@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == 'POST':
        name = request.form['name']
        record = create_new_record(name)
        return redirect(url_for('read', uid=record))
    return render_template("create.html")


# Read operation
@app.route("/read/<int:uid>", methods=["GET"])
def read(uid):
    record = get_record(uid)
    return render_template('read.html', record=record, uid=uid)


# Update operation
@app.route('/update/<int:uid>', methods=["GET", "POST"])
def update(uid):
    if request.method == "POST":
        name = request.form['name']
        update_record(uid, name)
        return redirect(url_for('read', uid=uid))

    record = get_record(uid)
    return render_template('update.html', record=record, uid=uid)


@app.route('/delete/<int:uid>', methods=['POST'])
def delete(uid):
    delete_record(uid)
    return redirect('/')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
