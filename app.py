import random
import string
from flask import Flask

app = Flask(__name__)

@app.route('/')
def rannum():
   x =random.randint(500000,9000000)
   y = str(x)
   return y
   if __name__ == '__main__':
   app.run()
