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
    return render_template("file.html")
    
@app.route("/hello/<string:name>")
def hello():
    