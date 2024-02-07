from flask import Flask, request, jsonify, render_template

# Create flask app
app = Flask(__name__)

@app.route("/",methods=['GET'])
def Home():
    return render_template("index.html")

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def predict():
    if request.method == 'POST':
        # getting input with name = Number1 in HTML form
        num1 = request.form.get("Number1")
        num2 = request.form.get("Number2")

        add = str(int(num1) + int(num2))
        subtract = str(int(num1) - int(num2))
        multiply = str(int(num1) * int(num2))
        divide = str(int(num1) / int(num2))
        
        return render_template("index.html", 
                               Addition = "A + B is {}".format(add),
                               Subtraction = "A - B is {}".format(subtract),
                               Multiplication = "A * B is {}".format(multiply),
                               Division = "A / B is {}".format(divide))
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)