from flask import Flask, render_template

app = Flask(__name__)

#the default landing page
@app.route("/")
def default():
	return render_template('index.html')


@app.route("/ninjas")
def alltheninjas():
	return render_template('ninjas.html')

@app.route("/ninjas/<ninja_color>")
def oneninja(ninja_color):
	if ninja_color == "blue":
		return render_template('blue.html')

	elif ninja_color == "red":
		return render_template('red.html')

	elif ninja_color == "orange":
		return render_template('orange.html')

	elif ninja_color == "purple":
		return render_template('purple.html')
	else:
		return render_template('april.html')

app.run(debug=True)