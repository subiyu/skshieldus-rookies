import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication 
from dotenv import load_dotenv
import os
import time

def mail_sender(detected_files):
    load_dotenv()
    SECRET_ID = os.getenv("SECRET_ID")
    SECRET_PASS = os.getenv("SECRET_PASS")

    smtp = smtplib.SMTP('smtp.naver.com', 587)
    smtp.ehlo()
    smtp.starttls()

    smtp.login(SECRET_ID, SECRET_PASS)

    myemail = "dbtnqlsqls001@naver.com"
    youremail = "dbdbtnqls001@naver.com"

    msg = MIMEMultipart()

    msg['Subject'] ="첨부파일 테스트 입니다."
    msg['From'] = myemail
    msg['To'] = youremail

    text = """
    첨부파일 메일 테스트 내용 입니다.
    감사합니다.
    """
    
    contentPart = MIMEText(text) 
    msg.attach(contentPart) 

    with open(detected_files, 'rb') as f : 
        etc_part = MIMEApplication( f.read() )
        etc_part.add_header('Content-Disposition','attachment', filename=etc_file_path)
        msg.attach(etc_part)

    smtp.sendmail( myemail,youremail,msg.as_string() )
    smtp.quit()

DIR_WATCH = "static"
previous_files = set(os.listdir(DIR_WATCH))
detected_files = "detected_files.txt"

while True:
    time.sleep(1)
    print("모니터링중")
    current_files = set(os.listdir(DIR_WATCH))
    new_files = current_files - previous_files
    for filename in new_files:
        file_path = os.path.join(DIR_WATCH, filename)
        with open(file_path,'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("#") or line.startswith("//"):
                    print(f"{file_path} 주석 처리된 라인 {line}")
                    #파일 저장 기능 추가
                    with open(detected_files, 'a', encoding='utf-8') as wf: #'a'는 이어쓰기 'w'는 완전히 새로쓰기
                        wf.write(f"{file_path} 주석 처리된 라인 {line}")
        mail_sender(detected_files) #메일 보내기

    previous_files = current_files
