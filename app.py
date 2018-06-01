from flask import Flask, request, render_template, redirect, url_for
# from gevent import pywsgi
# from geventwebsocket.handler import WebSocketHandler
from geventwebsocket import WebSocketServer, WebSocketApplication, Resource
# import time
# from websocket import create_connection
import threading
import json
import socket
from contextlib import closing
import time
from websocket import create_connection
from src import Tag, Chair
import subprocess

subprocess.Popen(["/usr/local/bin/fluentd -c /Users/mo-ri-/Works/Research/RFID/fluent/fluent_mac.conf"],
                 stdout=subprocess.PIPE, shell=True)

app = Flask(__name__)
ws = None
j2 = ""
# chair = Chair.Chair(1)
# chair.addTag("3000300833B2DDD9014000000014")
# chair.addTag("3000300833B2DDD9014000000016")
# chair.addTag("3000300833B2DDD9014000000017")
# chair.addTag("3000300833B2DDD9014000000018")
# chair2 = Chair.Chair(2)
# chair2.addTag("3000300833B2DDD9014000000011")
# chair2.addTag("3000300833B2DDD9014000000012")
# chair2.addTag("3000300833B2DDD9014000000015")
# chair2.addTag("3000300833B2DDD9014000000019")


def func2():

    host = '192.168.11.152'
    port = 3002
    bufsize = 4096

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ws1 = create_connection("ws://192.168.11.152:9999/pipe")
    with closing(sock):
        sock.bind((host, port))
        while True:
            j = sock.recv(bufsize).decode("utf-8").split("\t")
            j2 = json.loads(j[1])
            ChatApplication.j2 = j2

            for info in j2['tags']:
                splited_info = info.split(":")
                splited_info[1] = int(splited_info[1])+(3*(int(j2['rw_id'])-1))
                chair_id = Tag.Tag.getChairId(splited_info[0])
                # print(chair_id)
                if chair_id is not None:
                    # print(chair_id)
                    if chair_id not in ChatApplication.existChairs:
                        ChatApplication.existChairs.append(chair_id)
                        # print(chair_id)

                    # chair.rssi[splited_info] = splited_info[3]
                    # ChatApplication.rssi = chair.rssi

            ws1.send("Hello, World")
            ChatApplication.result = ws1.recv()
            ChatApplication.existChairs = []

            # print(j2)


def func3():
    ws1 = create_connection("ws://192.168.11.152:9999/pipe")
    while True:

        ws1.send("Hello, World")
        time.sleep(1)
        ChatApplication.result = ws1.recv()
        # print("Received '%s'" % result)
        time.sleep(1)

    # ws.close()


class ChatApplication(WebSocketApplication):

    j2 = ""
    result = ""
    chair_id = []
    existChairs = []
    rssi = []
    chair_list = []

    def on_open(self):
        print('Some client connected!')

    def on_message(self, message):
        if message is None:
            return
        # ChatApplication.count = ChatApplication.count + 1
        # print(ChatApplication.j2)
        # self.broadcast(str(ChatApplication.existChairs))
        self.broadcast(str(ChatApplication.existChairs))
        # self.broadcast("morimori")

    def broadcast(self, message):
        for client in self.ws.handler.server.clients.values():
            client.ws.send(message)

    def on_close(self, reason):
        print('Connection closed!')


def func1():
    WebSocketServer(
        ('192.168.11.152', 9999),
        Resource([
            ('^/pipe', ChatApplication),
        ]),
        debug=False
    ).serve_forever()


@app.route('/')
def index():
    return render_template('index.html', chair_list=Chair.Chair.chair_list, text=ChatApplication.j2)


@app.route('/add')
def index2():
    tags = []
    res = request.args.get('res')
    if len(Chair.Chair.chair_list) is not 0:
        for i in Chair.Chair.chairs:
            tags.append(i.tags)
        return render_template('add.html', list=Chair.Chair.chair_list, tags=Tag.Tag.tag_chair_relation, tags_c=tags, chairs=Chair.Chair.chairs, res=res)
    else:
        return render_template('add.html', res=res)


@app.route('/delete', methods=['POST'])
def index3():
    if request.method == 'POST':
        Tag.Tag.deleteTagRelation(request.form['delete'])

    return redirect(url_for('index2'))


@app.route('/add/tag', methods=['POST'])
def index4():
    if request.method == 'POST':
        res = Chair.Chair.chairs[int(request.form['chair_id'])].addTag("3000300833B2DDD90140000000"+request.form['name'])
        if res is True:
            return redirect(url_for('index2', res=1))
        else:
            return redirect(url_for('index2', res=0))


@app.route('/add/chair', methods=['POST'])
def index5():
    if request.method == 'POST':
        if len(Chair.Chair.chair_list) is not 0:
            length = Chair.Chair.chair_list[-1]
            Chair.Chair(length+1)
        else:
            Chair.Chair(1)
    return redirect(url_for('index2'))


@app.route('/delete/chair', methods=['POST'])
def index6():
    if request.method == 'POST':
        for chair in Chair.Chair.chairs:
            if chair.id == int(Chair.Chair.chair_list[int(request.form['c_id'])]):
                chair.deleteChair()
    return redirect(url_for('index2'))


if __name__ == "__main__":
    thread_1 = threading.Thread(target=func1)
    thread_1.start()
    thread_2 = threading.Thread(target=func2)
    thread_2.start()

    app.run(host='192.168.11.152', port=5000)
