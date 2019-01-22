from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact')
def contacts():
    return render_template('contact.html')



@app.route('/courses')
def courses():
    return render_template('courses.html')


@app.route('/disclaimer')
def disclaimer():
    return render_template('disclaimer.html')


@app.route('/pricing')
def pricing():
    return render_template('pricing.html')


@app.route('/email', methods= ['POST', 'GET'])
def emailing():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result = result)

@app.route('/privacy')
def privacy():
    return render_template("privacy.html")


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404


if __name__=='__main__':
    app.run(host="0.0.0.0", port=7000, debug=True)



