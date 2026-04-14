from flask import Flask, render_template, request  # Flask 웹 기능 불러오기
from gpiozero import LED  # 라즈베리파이 GPIO로 LED 제어

app = Flask(__name__)  # Flask 애플리케이션 생성

red_led = LED(21)  # GPIO 21번 LED 설정

@app.route('/')  # 기본 URL('/')로 접속했을 때 실행되는 함수
def home():
    return render_template("index.html")  # index.html 파일을 웹 브라우저에 표시

@app.route('/data', methods=['POST'])  # /data 경로로 POST 요청이 들어오면 실행
def data():
    data = request.form['led']  # HTML 에서 led 값 가져오기

    if(data == 'on'):  # 값이 'on'이면
        red_led.on()  # LED 켜기
    elif(data == 'off'):  # 값이 'off'이면
        red_led.off()  # LED 끄기

    return home()  # 처리 후 메인 페이지 다시 표시

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80")  # 80번 포트로 서버 실행