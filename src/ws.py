from websocket_server import WebsocketServer


def func1():
    def new_client(client, server):
        server.send_message_to_all("Hey all, a new client has joined us")

    def send_msg_allclient(client, server, message):
        server.send_message_to_all("Hey all:" + message)

    server = WebsocketServer(9999, host='192.168.11.152')
    server.set_fn_new_client(new_client)
    server.set_fn_message_received(send_msg_allclient)
    server.run_forever()
