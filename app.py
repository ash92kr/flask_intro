from flask import Flask, render_template, request
import random
import requests
from bs4 import BeautifulSoup
import csv
import datetime    # 사용자가 검색한 시간도 저장

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
    

@app.route("/lunch")
def lunch():
    list = ["20층", "짜장면", "김밥", "탕수육"]
    
    pick = random.choice(list)
    return render_template("lunch.html", pick=pick)



@app.route("/lunch2")
def lunch2():
    
    list = ['20층', '짜장면', '김밥', '탕수육']
    dict = {"20층":"http://recipe1.ezmember.co.kr/cache/recipe/2015/06/18/411a74b8d58d66a050320c9c3e22d192.jpg",
    "짜장면":"http://ojsfile.ohmynews.com/STD_IMG_FILE/2016/1214/IE002069160_STD.jpg",
    "김밥":"http://www.jungsungman.com/site_data/food_mst/1464827426_8yid7rQI_food11.jpg",
    "탕수육":"http://www.cultureline.kr/webgear/weblog_pds/313/DSCN7945.JPG"}
    
    pick = random.choice(list)
    image = dict[pick]
    return render_template("lunch2.html", pick=pick, image=image)


@app.route("/lotto")
def lotto():
    num_list = list(range(1, 46))
    
    lucky=random.sample(num_list, 6)
    return render_template("lotto.html", lucky=sorted(lucky))

# 사용자가 포털에 던진 값을 보여준다
@app.route("/naver")
def naver():
    return render_template("naver.html")


@app.route("/google")
def google():
    return render_template("google.html")


# hell로 요청을 보내면 hello2.html 문서를 연다
@app.route("/hello2")
def hello2():
    return render_template("hello2.html")

@app.route("/hi")
def hi():
    user_name = request.args.get('name')  # ?뒤의 값을 받을 때 name의 값을 받아 hi.html에 user_name을 보내준다
    return render_template("hi.html", user_name=user_name)


# 5교시 실습 - get 방식
@app.route("/yourname")
def yourname():
    return render_template("yourname.html")

@app.route("/study")
def study():
    yourname = request.args.get('name')
      
    study_list = ['자바', '파이썬', '도커', '하둡', '스파크', 'R', 'SQL']
    study_dict = {"자바": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQztZLle-auV_sLs40DTCKChKNxi2sju4GEDGIga5bTiHc2TLmMA",
    "파이썬":"https://thebook.io/img/covers/cover_006855.jpg",
    "도커":"https://subicura.com/assets/article_images/2017-01-19-docker-guide-for-beginners-1/docker-logo.png",
    "하둡":"http://files.idg.co.kr/itworld/image/u152168/hadoop_logo_290x218.jpg",
    "스파크":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTh8pVwk7l6jGlTII62YiV4BwA2dqS2VLJxSQRwhbwBWfVadQCUCw",
    "R":"http://www.urbanbrush.net/web/wp-content/uploads/edd/2017/09/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7-2017-09-04-%EC%98%A4%EC%A0%84-11.32.44.png",
    "SQL":"https://images-na.ssl-images-amazon.com/images/I/51i7bJ0NRLL._SX385_BO1,204,203,200_.jpg",
    }
    
    pick = random.choice(study_list)
    image = study_dict[pick]
    return render_template("study.html", yourname=yourname, pick=pick, image=image)
    
    
# 6교시
@app.route("/summoner")
def summoner():
    return render_template("summoner.html")

@app.route("/opgg")
def opgg():
    # print(request.args.get('summoner')
    summoner = request.args.get('summoner')   # print는 bash에 나오고 return은 html 문서에 나온다
    url = 'http://www.op.gg/summoner/userName='   # url과 summoner를 합친다
    print(url+summoner)
    # html = requests.get(url+summoner)   # html 전체 문서를 가져온 것
    
    html = requests.get(url+summoner).text
    soup = BeautifulSoup(html, 'html.parser')
    
    # select는 배열이 출력되므로 text를 붙일 수 없다
    win = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
    lose = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')

    # win에 정보가 있을 때랑 없을 때 분기 = 예외처리
    if len(win) == 0:
        win_i = "0승"
    else:
        win_i = win[0].text
    
    if len(lose) == 0:
        lose_i = "0패"
    else:
        lose_i = lose[0].text
    
    # return html.text
    # print(type(win))  # win의 타입이 bs4의 element여서 바로 리턴 불가
    # return win.text
    
    # list.txt를 열고 data를 입력한다음 닫을 것
#    f = open("list.txt", 'a+')
#    data = "소환사의 이름은 {} {}/{}입니다.".format(summoner, win_i, lose_i)
#    f.write(data)
#    f.close()
    
    f = open('list.csv', 'a+', encoding='utf-8', newline='')   # 개행
    csvfile = csv.writer(f)
    data = [summoner, win_i, lose_i, datetime.datetime.now()]   # 4가지의 정보 입력(datetime은 모듈, 그 안의 datetime.now()함수 사용)
    csvfile.writerow(data)  # 행 단위로 입력
    f.close()
    
    return render_template("opgg.html", summoner=summoner, win=win_i, lose=lose_i)
    

@app.route('/log')
def log():
    f = open('list.csv', 'r', encoding='utf-8')
    logs = csv.reader(f)
    
    return render_template("log.html", logs=logs)

# 8교시

    
    
    
    
    
    
    
    
    
    
    
