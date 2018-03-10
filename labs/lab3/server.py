import zmq

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.REP)
sock.bind("tcp://127.0.0.1:5678")
sock1 = context.socket(zmq.PUB)
sock1.bind("tcp://127.0.0.1:5679")

# Run a simple "Echo" server
while True:
    username, message = sock.recv_pyobj()
    sock.send_string("")
    sock1.send_pyobj((username, message))


'''

zyldeMacBook-Pro:untitled1 apple$ python3 client.py Bob
User Bob Connected to the chat server.
[Alice]: Hi from Alice
[Bob]>Hello world
[Bob]>

zyldeMacBook-Pro:untitled1 apple$ python3 client.py Alice
User Alice Connected to the chat server.
[Alice]>Hi from Alice
[Bob]: Hello world
[Alice]>
'''