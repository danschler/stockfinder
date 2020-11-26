from flask import Flask
import finanzen_fundamentals.stocks as ff

app = Flask(__name__)


@app.route("/<ticker>")
def print_ticker(ticker):
    ff.search_stock("519000")
    return 1


if __name__ == "__main__":
    app.run(debug=True)
