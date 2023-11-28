from flask import Flask, render_template, request
from flask import send_file
import googletrans
import openpyxl
import os
import time

app = Flask(__name__) #초기화

@app.route('/') #라우터
def index():
    return render_template('upload.html')

@app.route('/process', methods=['GET', 'POST'])
def process():
    file = request.files['file'] #파일(엑셀)을 받아서
    file.save(os.path.join('uploads', file.filename))
    workbook = openpyxl.load_workbook(os.path.join('uploads', file.filename)) #os.path.join
    sheet = workbook.active 
    translator = googletrans.Translator()
    for row in sheet.iter_rows(): #엑셀에서 데이터가 존재하는 곳까지 for문 돌기
        for cell in row:
            translated_text = translator.translate(cell.value, dest='en').text #cell 값을 읽어 영어로 바꾼 후, text를 가져옴
            cell.value = translated_text #번역된 text로 cell 값을 update
        time.sleep(0.5)

    workbook.save('transrated_excel.xlsx')

    return render_template("result.html", file_name=file.filename) #result.html로 파일들을 보내

@app.route('/download_report')
def download_report():
    return send_file('transrated_excel.xlsx', as_attachment=True) #as_attachemnt: 첨부파일 형식으로 보내겠다

if __name__ == "__main__":
    app.run(debug=True) #디버깅 용으로 동작