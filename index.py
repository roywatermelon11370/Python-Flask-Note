from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)
notelst=[]
noteTem={'id':'','ttle':'','conten':'','tgs':[]}
setts={'rmAnim' : False, 'darkMode' : False}


def maxIdPlusOne():
    max=-1
    for i in notelst:
        idd=i['id']
        if idd > max:
            max=idd

    return max+1


def findItemById(x):
    for i in notelst:
        if i['id']==x:
            return i
    return 0


@app.route("/")
def index():
    return render_template('index.html', notelst=notelst)


@app.route("/add")
def add():
    return render_template('add.html')


@app.route("/addAction", methods=['POST'])
def addAction():
    id=maxIdPlusOne()
    ttle=request.form['title']
    conten=request.form['content']
    tagsAll=request.form['tags']
    tgs=set(tagsAll.split(','))
    print(ttle)
    print(conten)
    print(tgs)
    notelst.append({'id':id,'title':ttle,'content':conten,'tags':tgs})
    return redirect(url_for('index'))


@app.route("/detail/<int:addId>", methods=['GET'])
def ShowDetail(addId):
    curr=findItemById(addId)
    return render_template('detail.html',noteitem=curr)


@app.route("/edit/<int:editId>", methods=['GET'])
def edit(editId):
    curr=findItemById(editId)
    return render_template('edit.html',noteitem=curr)


@app.route("/editAction", methods=['POST'])
def editAction():
    currId=request.form['id']
    ttle=request.form['title']
    conten=request.form['content']
    tagsAll=request.form['tags']
    tgs=set(tagsAll.split(','))
    curr=findItemById(currId)
    currIndex=curr.index()
    notelst.remove(curr)
    notelst.insert(currIndex,{'id':currId,'title':ttle,'content':conten,'tags':tgs})


@app.route("/manage")
def manage():
    return render_template('manage.html')


@app.route("/delete/<int:delId>", methods=['GET'])
def delete(delId):
    curr=findItemById(delId)
    notelst.remove(curr)
    return redirect('/')


@app.route("/settings")
def settings():
    return render_template('settings.html')


@app.route("/search")
def search():
    return render_template('search.html')


@app.route("/result")
def result():
    return render_template('search_results.html')


if __name__=='__main__':
	app.run('localhost',9000,debug=True)