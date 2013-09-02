__Author__ = "Charlie"

from flask import Flask
l5r = Flask(__name__)

@l5r.route("/about")
def about():
    return 'a service to generate character sheets for l5r'

@l5r.route("/raw/v1")
def raw_pdfs():
    return 'pdfs'

if __name__ == '__main__':
    l5r.run()