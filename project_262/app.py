from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
	return render_template("index.html")

if __name__ == "__main__":
	app.run()


@app.route('/' , methods=['POST'])
def math_operations():
	equation = request.form['text']
	operation = request.form['operation']
	result = "https://newton.now.sh/api/v2//" + operation + "/" + equation
	data = request.get(result).json()
	answer = data['result']
	return render_template("index.html", result=answer, equation=equation )
