from pybricks.messaging import BluetoothMailboxServer, TextMailbox, screen
server = BluetoothMailboxServer()
mbox  = TextMailbox('AutoBus-Server', server)

def server():
    screen.print("[!] Waiting for connection")
    server.wait_for_connection()
    screen.print("[!] Connected")
    mbox.wait()
    screen.print(mbox.read())
    mbox.send("Prova-WRI - Server")

def client():
    screen.print("[!] Waiting for connection")
    client.connect(SERVER)
    screen.print("[!] Connected")
    mbox.send("Prova-WRI - Server")
    mbox.wait()
    screen.print(mbox.read())