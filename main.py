from flask import Flask, render_template, request

app = Flask(__name__)

# Replace with your API key and base URL
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.currencyapi.com/v3/convert"

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
  from_currency = request.form.get("from")
  to_currency = request.form.get("to")
  amount = float(request.form.get("amount"))

  # Construct the API request URL
  url = f"{BASE_URL}?apiKey={API_KEY}&from={from_currency}&to={to_currency}&amount={amount}"

  # Use requests library to fetch data from the API
  import requests
  response = requests.get(url)
  data = response.json()

  if data["status"] != "success":
    error = data["message"]
    return render_template("index.html", error=error)

  conversion_rate = data["result"]["converted_amount"]
  return render_template("index.html", result=f"{amount} {from_currency} is equal to {conversion_rate:.2f} {to_currency}")

if __name__ == "__main__":
  app.run(debug=True)
