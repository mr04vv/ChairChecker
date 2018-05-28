from flask import Flask
from src import Chair
from src import Tag

app = Flask(__name__)
chair = Chair.Chair(1)
chair.addTag("002")
chair.addTag("003")
chair.addTag("002")
chair.addTag("004")
chair2 = Chair.Chair(2)
chair2.addTag("005")
chair2.addTag("006")
chair2.addTag("007")
chair2.addTag("008")

@app.route('/')
def hello_world():
    # return str(Tag.Tag.getChairId("007"))
    return str(Tag.Tag.getTagRelation())
    # return str(chair.getId()) + str(chair2.getId()) + str(chair.getId())
    # return 'hello'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
