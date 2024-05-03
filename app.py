from flask import Flask
import time
import random

app = Flask(__name__)



@app.route('/')
def hello_world():
    j=1
    loop_range=random.randint(100000000,200000000)
    for i in range(200000000):
        j+=1
    result = "Helloworld" + str(j)
    return result


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



