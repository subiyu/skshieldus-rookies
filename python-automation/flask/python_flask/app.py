from flask import Flask, render_template, request
import feedparser

app = Flask(__name__) #초기화

@app.route('/') #라우터설정(기본 페이지)
def hello_world():
    return render_template('index.html')

@app.route('/rss', methods=['GET', 'POST']) #http://127.0.0.1:5000/rss
def rss():
    rss_url = request.form['rss_url'] #request(index.html의 form data)에서 name=rss_url 인 input값을 rss_url로 지정
    feed = feedparser.parse(rss_url) 
    return render_template('rss.html', feed=feed)

if __name__ == "__main__":
    app.run(debug=True) #디버깅 용으로 동작