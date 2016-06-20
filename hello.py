from flask import Flask
from prime import primenos
app = Flask(__name__)

@app.route('/')
def hundred_primes():
	return str(primenos(100))

@app.route('/<int:number>', methods=['GET'])
def primes(number):
	return str(primenos(number))

if __name__ == '__main__':
	app.run(debug = True)
