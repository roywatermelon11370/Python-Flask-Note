from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)
notelst=[]
noteTem={'title':'','content':'','tags':[]}
setts={'rmAnim' : False, 'darkMode' : False}

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/add")
def add():
    return render_template('add.html')


@app.route("/manage")
def manage():
    return render_template('manage.html')


@app.route("/settings")
def settings():
    return render_template('settings.html')


@app.route("/search")
def search():
    return render_template('search.html')


if __name__=='__main__':
	app.run('localhost',9000,debug=True)