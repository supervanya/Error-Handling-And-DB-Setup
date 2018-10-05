from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)

# Challenge 1: Return the 404.html template
# Edit it such that it displays an interesting message

# Challenge 2: Include the link to homepage i.e. http://localhost:5000 in 404.html.
## YOUR CODE HERE

# Challenge 3: Write an error handler for 500 error
## YOUR CODE HERE

# Challenge 4: Edit the 500.html template to display link to homepage and link to itunes-form.

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html')

@app.route('/500')
def fiver():
    return render_template('500.html')


@app.route('/')
def index():
    return "Hello, World!"

@app.route('/itunes-form')
def ituneForm():
    return render_template('itunes-form.html')

@app.route('/itunes-result', methods = ['POST'])
def resultTunes():
    if request.method == "POST":
        # get the title from POST
        artist   = request.form.get("artist")
        number  = request.form.get("num")

        params = dict(term = artist, limit = number)
        baseurl = "https://itunes.apple.com/search"
        response = requests.get(baseurl, params = params).json()

        # find the right data in the JSON
        author = response["results"][0]["artistName"]
        track_name = response["results"][0]["trackName"]

        return render_template('list.html', results = response['results'])

if __name__ == '__main__':
    app.run(debug = True)
