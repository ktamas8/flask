from flask import Flask, request, json
app = Flask(__name__)

@app.route('/messages', methods = ['POST'])
def api_message():

    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)

    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"

    else:
        return "415 Unsupported Media Type ;)"

if __name__ == '__main__':
    app.run()

# curl -H "Content-type: text/plain" -X POST http://localhost:5000/messages -d 'Hello Data'
# curl -H "Content-type: application/json" -X POST http://localhost:5000/messages -d '{"message":"Hello Data"}'
# curl -H "Content-type: application/octet-stream" -X POST http://localhost:5000/messages --data-binary @message.bin
