from flask import Flask
from flask import request as f_req
import json
import urllib.request as u_req

app = Flask(__name__)

# TODO: write verify_token(decided on facebook)
verify_token = 'aaaa'
# TODO: write forwarding URL
forwardingAddressBase = 'http://requestbin.fullcontact.com/1llfi7f1'


# Operation Check
@app.route('/')
def hello_world():
    return 'working'


# Facebook Webhooks verify
@app.route('/facebook', methods=['GET'])
def facebook_verify():
    if f_req.args.get('hub.mode') == 'subscribe':
        if f_req.args.get('hub.verify_token') == verify_token:
            print("token OK")
            return f_req.args.get('hub.challenge')
        else:
            print("token NG")


# Facebook Webhooks forwarding
@app.route('/facebook', methods=['POST'])
def facebook_forwarding():
    print(f_req.data)
    data = json.loads(f_req.data)
    print("{}".format(json.dumps(data, indent=2))) # debug

    json_data = json.dumps(data).encode("utf-8")
    url = forwardingAddressBase + '/facebook'
    method = "POST"
    headers = {"Content-Type": "application/json"}

    request = u_req.Request(url, data=json_data, method=method, headers=headers)
    with u_req.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
    return "ok"


if __name__ == '__main__':
    app.run()
