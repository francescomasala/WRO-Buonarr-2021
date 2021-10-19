from pybricks.messaging import BluetoothMailboxServer, TextMailbox
server = BluetoothMailboxServer()
mbox  = TextMailbox('AutoBus-Server', server)

def server():
    print("[!] Waiting for connection")
    server.wait_for_connection()
    print("[!] Connected")
    mbox.wait()
    print(mbox.read())
    mbox.send("Prova-WRI - Server")

def client():
    print("[!] Waiting for connection")
    client.connect(SERVER)
    print("[!] Connected")
    mbox.send("Prova-WRI - Server")
    mbox.wait()
    print(mbox.read())

