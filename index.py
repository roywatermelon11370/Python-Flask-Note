from flask import Flask,render_template,request,redirect,url_for,flash
app=Flask(__name__)
notelst=[]
noteTem={'id':'','ttle':'','conten':'','tgs':[]}
setts={'rmAnim' : False, 'theme':'light'}


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
    return render_template('index.html', notelst=notelst, setts=setts)


@app.route("/add")
def add():
    return render_template('add.html', setts=setts)


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
    return redirect('/')


@app.route("/detail/<int:addId>", methods=['GET'])
def ShowDetail(addId):
    curr=findItemById(addId)
    return render_template('detail.html',noteitem=curr, setts=setts)


@app.route("/edit/<int:editId>", methods=['GET'])
def edit(editId):
    curr=findItemById(editId)
    if(curr!=0):
        tagsShow=','.join(list(curr['tags']))
    else:
        tagsShow=0
    return render_template('edit.html',noteitem=curr,tags=tagsShow, setts=setts)


@app.route("/editAction", methods=['POST'])
def editAction():
    currId=int(request.form['id'])
    ttle=request.form['title']
    conten=request.form['content']
    tagsAll=request.form['tags']
    tgs=set(tagsAll.split(','))
    curr=findItemById(currId)
    notelst.remove(curr)
    notelst.append({'id':currId,'title':ttle,'content':conten,'tags':tgs})
    return redirect('detail/{}'.format(currId))


@app.route("/manage")
def manage():
    return render_template('manage.html', notelst=notelst, setts=setts)


@app.route("/manageAction", methods=['POST'])
def manageAction():
    checkedId=request.form.getlist('noteitem')
    for i in checkedId:
        curr=findItemById(int(i))
        notelst.remove(curr)
    return redirect('/')


@app.route("/delete/<int:delId>", methods=['GET'])
def delete(delId):
    curr=findItemById(delId)
    notelst.remove(curr)
    return redirect('/')


@app.route("/settings")
def settings():
    return render_template('settings.html', setts=setts)


@app.route("/settingsSave",methods=['POST'])
def settSave():
    theme=request.form['theme']
    setts.update({'theme': theme})
    return redirect('/')


@app.route("/search")
def search():
    keyWord=request.args.get('keyword')
    results=[]
    if keyWord:
        for i in notelst:
            for j in i['tags']:
                if j==keyWord:
                    results.append(i)
        return render_template('search.html',resultlst=results,keyword=keyWord,setts=setts)
    return  render_template('search.html',keyword=False,resultlst=False, setts=setts)
 

if __name__=='__main__':
	app.run('localhost',9000,debug=True)