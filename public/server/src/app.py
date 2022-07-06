from flask import Flask, render_template, request, url_for
import maplegg

#Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route("/search")
def search():
      return render_template('search.html')

@app.route("/user_info", methods=['POST', 'GET'])
def user_info():
      if request.method == 'POST':
        user = maplegg.get_data(str(request.form['nickname']))
        return render_template('user_info.html', user=user)
      else:
        return render_template('user_info.html')
            

if __name__=="__main__":
   app.run(host="0.0.0.0", port="5000", debug=True)
   # host 등을 직접 지정하고 싶다면
   # app.run(host="127.0.0.1", port="5000", debug=True)