from flask import Flask, render_template, request
from Maths.mathematics import summation, substraction, multiplication
# Import the Maths package here

app = Flask("Mathematics Problem Solver")


def validate_numbers(function):
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = function(num1, num2)
        return str(result)
    except:
        return str("Ingresa numeros válidos")


@app.route("/")
def render_index_page():
    return render_template("index.html")


@app.route("/sum")
def sum_route():
    return validate_numbers(summation)


@app.route("/sub")
def sub_route():
    return validate_numbers(substraction)


@app.route("/mul")
def mul_route():
    return validate_numbers(multiplication)

    
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
