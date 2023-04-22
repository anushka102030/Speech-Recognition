from flask import Flask, request, send_from_directory, session, render_template
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy

import speechprocesssing as sp
# import rospy
# from std_msgs.msg import String

app = Flask(__name__, static_folder='./Frontend/build', static_url_path='/')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'TEST_SECRET_KEY'

db = SQLAlchemy(app)


class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    # result = db.Column("result", db.String(100))
    # data_ui = db.Column("data_ui", db.String(100))
    data_hub = db.Column("data_hub", db.String(100))

    def __init__(self, data_hub):
        # self.result = result
        # self.data_ui = data_ui
        self.data_hub = data_hub



@app.route('/api/get', methods=['GET'])
@cross_origin()
def test():
    return {
        'result': 'REACT FLASK AND HEROKU APP'
    }

@app.before_first_request
def create_tables():
    db.create_all()


@app.route("/view")
def view():
    return render_template("view.html", values = users.query.order_by(users._id.desc()).first())


# @app.route("/view_last", methods = ['GET'])
# def query_db():
#     return users.query.first()


@app.route('/api/client_message', methods=['POST'])
@cross_origin()
def process_post():
    # pub = rospy.Publisher('coffeeInfo', String, queue_size=10)
    # rospy.init_node('talker', anonymous=True)
    
    
    data = request.get_json()
    print(data)
    data_hub ,data_ui = sp.process(data)
    #data_hub = sp.processForCompVis(data)

    # pub.publish(data_hub)
    json_obj = {
        'result': 'Server received message!',
        'msg': data_ui,
        'msg_hub': data_hub
    }
    #print(data_ui)
    print(data_hub)

    # data_ui = str(data_ui)
    # data_ui = "hello"
    # data_hub = str(data_hub)
    usr = users(data_hub)
    db.session.add(usr)
    db.session.commit()

    #g.baristabot = json_obj
    #session['baristabot'] = json_obj
    #session.modified = True
    #session.permanent = True
    return json_obj

# @app.route('/api/hub-get', methods=['GET'])
# @cross_origin()
# def hub_data():
#     return g.get('baristabot')
#     # if not session.get("baristabot") == None:
#     #     return session['baristabot']
#     # else:
#     #     return "Key not found"

@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder,'index.html')

if __name__ == "__main__":
    db.create_all()
    app.run()