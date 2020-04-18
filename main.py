from audio.AudioListener import AudioListener
from messaging.server import MessagingServer
from messaging.client import MessagingClient
import sys

if len(sys.argv) < 2:
    print("No argument specified. Accepts: client or server")
    sys.exit(-1)

run_type = sys.argv[1]
listener = AudioListener()

if run_type == 'server':
    server = MessagingServer()
    listener.listen()
    message, address = server.receive_message()

    while True:
        server.send_message(listener.stream_data, address)

elif run_type == 'client':
    client = MessagingClient()
    client.send_message(str.encode("Sending initial message"))

    while True:
        received_audio = client.receive_message()
        listener.play(received_audio)
        