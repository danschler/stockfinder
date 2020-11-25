from flask import Flask

app = Flask(__name__)


@app.route("/<ticker>")
def print_ticker(ticker):
    return "Ticker: %s!" % ticker


if __name__ == "__main__":
    app.run(debug=True)
