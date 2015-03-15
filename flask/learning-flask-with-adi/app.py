from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

# app.config('DEBUG') = True #

@app.route("/")
def hello():
    return render_template("hello.html")

@app.route('/search', methods = ["GET", "POST"])
def search():
	if request.method == "POST":
		url = "https://api.github.com/search/repositories?q=" + request.form["user_search"]
		print request.form
		response = requests.get(url)
		response_dict = response.json()
		return render_template("results.html", api_data = response_dict)
	else:
		return render_template("search.html")

@app.errorhandler(404)
def not_found(error):
	return "Sorry, I haven't coded that yet. I'll get back to you!", 404

@app.errorhandler(500)
def internal_server_error(error):
	return "My code broke, my bad.", 500

if __name__ == '__main__':
	app.run(host = '0.0.0.0')