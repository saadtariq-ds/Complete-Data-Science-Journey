## Building URL Dynamically
## Variable Rule
## Jinja2 Template

'''
1. {{ }} Expression to print output in HTML
2. {%...%} conditions, for loops
3. {#...#} this is for comments
'''


from flask import Flask, render_template, request, redirect,url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1> Welcome to Flask Lecture <h1></html>"

@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == "POST":
        name=request.form['name']
        return f"Hello: {name}"
    return render_template('form.html')

## Variable Rule
# @app.route('/success/<int:score>')
# def success(score):
#     return "The marks you got is, " + str(score)

@app.route('/success/<int:score>')
def success(score):
    if score >= 50:
        result = "PASS"
    else:
        result = "FAIL"

    return render_template('result.html', results=result)

@app.route('/successresults/<int:score>')
def successresults(score):
    if score >= 50:
        result = "PASS"
    else:
        result = "FAIL"

    exp = {'score':score, 'result':result}

    return render_template('result1.html', results=exp)

## if confition
@app.route('/sucessif/<int:score>')
def successif(score):

    return render_template('result.html',results=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html',results=score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('successresults',score=total_score))



if __name__ == "__main__":
    app.run(debug=True)