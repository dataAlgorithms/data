'''
templates/table.html

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Agile Data Science</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Bootstrap example in Agile Data Science, 2.0">
    <meta name="author" content="Russell Jurney">
    <link href="/static/bootstrap.min.css" rel="stylesheet">
    <link href="/static/bootstrap-theme.min.css" rel="stylesheet">
  </head>

  <body>
    <div id="wrap">

      <!-- Begin page content -->
      <div class="container">
        <div class="page-header">
          <h1>Agile Data Science</h1>
        </div>
        <p class="lead">Executives</p>
        <table class="table">
          <thead>
              <th>Name</th>
              <th>Company</th>
              <th>Title</th>
          </thead>
          <tbody>
            {% for executive in executives -%}
            <tr>
              <td>{{executive.name}}</td>
              <td>{{executive.company}}</td>
              <td>{{executive.title}}</td>
            </tr>
            {% endfor -%}
          </tbody>
        </table>
      </div>

      <div id="push"></div>
    </div>

    <div id="footer">
      <div class="container">
        <p class="muted credit"><a href="http://shop.oreilly.com/product/0636920025054.do">Agile Data Science</a> by <a href="http://www.linkedin.com/in/russelljurney">Russell Jurney</a>, 2016
      </div>
    </div>
    <script src="/static/bootstrap.min.js"></script>
  </body>
</html>
'''

from flask import Flask, render_template
from pymongo import MongoClient
import bson.json_util

# Set up Flask
app = Flask(__name__)

# Set up Mongo
client = MongoClient() # defaults to localhost
db = client.agile_data_science

# Fetch from/to totals, given a pair of email addresses
@app.route("/executive/<name>")
def executive(name):
  executives = db.executives.find({"name": name})
  return render_template('table.html', executives=list(executives))

if __name__ == "__main__": 
    app.run(debug=True)
