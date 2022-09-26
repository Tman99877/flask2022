from flask import Flask, render_template, request
import os           
app = Flask(__name__)

IMG_FOLDER = os.path.join('static', 'pics')

app.config['UPLOAD_FOLDER'] = IMG_FOLDER


@app.route("/")
def Display_IMG():
     esdeath = os.path.join(app.config['UPLOAD_FOLDER'], 'esd.jpg')
     return render_template("homepage.html", user_image=esdeath)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            pass # do something
        elif  request.form.get('action2') == 'VALUE2':
            pass # do something else
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('homepage.html', form=form)
    
    return render_template("homepage.html")


@app.route("/")                
def home():                    
    return render_template("homepage.html")


                                           
    
if __name__== "__main__":
    app.run(debug=True)