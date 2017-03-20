from flask import *
from datetime import *
import random

app = Flask(__name__)

item = [
    {
        "src" : "https://scontent.fhan2-2.fna.fbcdn.net/v/t1.0-9/12243328_985456551526614_7139423683245428893_n.jpg?oh=fcdda138cbc785bdeb755339335d59e1&oe=5958D99A",
        "title" : "Quynh Anh Da Lat",
        "tags" : "#Quynh anh#Da Lat"
    },
    {
        "src" : "https://scontent.fhan2-2.fna.fbcdn.net/v/t1.0-9/10801672_773080326097572_942631531282475704_n.jpg?oh=8ceac7202b8dc44fecb9b3b0307e4201&oe=5968F6BA",
        "title" : "Quynh Anh DAV",
        "tags" : "#Quynh Anh#DAV"
    },
    {
        "src" : "https://scontent.fhan2-2.fna.fbcdn.net/v/t1.0-9/10462419_855540464518224_4979605342075222592_n.jpg?oh=6d031d2fd48d099fa57823d40f47869b&oe=592D7CB2",
        "title" : "Quynh Anh NCKH",
        "tags" : "#Quynh anh#NCKH"
    },
    {
        "src" : "https://scontent.fhan2-2.fna.fbcdn.net/v/t1.0-9/10997989_872194206186183_5981688287188892662_n.jpg?oh=6275da5eb065239e780cd07a89f3fbb2&oe=596E86D3",
        "title" : "Quynh Anh Avar",
        "tags" : "#Quynh anh"
    },
    {
        "src" : "https://scontent.fhan2-2.fna.fbcdn.net/v/t1.0-9/11174905_880435155362088_7198567411807692348_n.jpg?oh=30d1b0295b7114c4f4a37743775cb568&oe=5970A19A",
        "title" : "Quynh Anh Avar",
        "tags" : "#Quynh anh"
    }
]

@app.route('/') #init link
def hello_world():
    return redirect(url_for("login"))

number_of_visiter = 0

@app.route('/login') #init link
def login():
    global number_of_visiter
    number_of_visiter += random.randint(1,100)
    current_time_on_server = str(datetime.now())
    return render_template("login.html", current_time = current_time_on_server, number_visiter=number_of_visiter)

@app.route('/quynhanh') #init link
def quynhanh():
    return render_template("quynhanh.html", girl_list = item)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()