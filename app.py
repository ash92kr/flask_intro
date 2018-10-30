from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/html_tag")
def html_tag():
    return "<h1>안녕하세요!!!</h1>"  


@app.route("/html_line")
def html_lint():
    return """
    <h1>여러 줄을 보내봅시다.</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    """

@app.route("/html_file")
def html_file():
    return render_template("file.html")   # 파일을 보내서 url로 보내게 한다
    
    
@app.route("/hello_p/<string:name>")  # url -> hello 다음에 어떤 문자가 와도 name 변수로 보낼 수 있다
def hello_p(name):   # 고정된 url 주소
    return render_template("hello.html", people_name=name)  # string:name, name, name은 모두 같은 개념
    
    
@app.route("/cube/<int:number>")   # cube 뒤에 숫자가 올 수 있고, 사용자가 입력한 숫자를 받아 3제곱 후 cube.html을 통해 응답
def cube(number):      # 변수명
    result = number**3   # num*num*num
    return render_template("cube.html", result=result, number=number)   # 왼쪽은 html에서 활용할 변수, 오른쪽은 app.py에서 사용하는 변수
    