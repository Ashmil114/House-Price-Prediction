from flask import Flask, render_template, request
import predict

# import util

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def predict_home_price():
    price = ""
    if request.method == "POST":
        total_sqft = float(request.form["total_sqft"])
        location = request.form["location"]
        bhk = int(request.form["bhk"])
        bath = int(request.form["bath"])

        print(location, total_sqft, bhk, bath)
        try:
            price = predict.predict_price(location, total_sqft, bath, bhk)
            if price is False:
                price = "Location not found in the dataset."
        except Exception as e:
            price = "Error in prediction: " + str(e)

    return render_template("index.html", price=price)


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    # util.load_saved_artifacts()
    app.run(debug=True)
