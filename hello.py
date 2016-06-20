from flask import Flask
from prime import primenos
app = Flask(__name__)

@app.route('/<number>')
def primes():
	return primenos(number)

@app.route('/')
def hundred_primes():
	return str(primenos(100))
