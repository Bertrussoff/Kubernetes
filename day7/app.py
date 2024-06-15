from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/ingress')
def ingress_test():
    return 'Ingress Test'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
