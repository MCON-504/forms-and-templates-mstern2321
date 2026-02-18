from http import HTTPStatus

from flask import Flask, request, current_app

app = Flask(__name__)

@app.before_request
def before_request():
    print("Headers:", dict(request.headers))
    print("Cookies:", request.cookies)
    current_app.logger.info("Before request: method: %s path: %s", request.method, request.path)

@app.after_request
def after_request(response):
    print(response)
    response.headers["X-Custom-Header"] = "FlaskRocks"
    return response

@app.teardown_request
def teardown_request(exception):
    if exception:
        current_app.logger.error("Teardown request with exception: %s", exception)
    else:
        current_app.logger.info("Teardown request without exception")

@app.route("/")
def hello():
    return "<p>Welcome to My Flask API!</p>"

@app.route("/about")
def about():
    return {"name": "Your Name",
            "course": "MCON-504 - Backend Development",
            "semester": "Spring 2025"
            }

@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}! Welcome to the Flask."

@app.route("/exception")
def message_with_exception():
    raise ValueError("This is a test exception")

@app.route("/calculate")
def calculate():
    try:
        num1 = float(request.args.get("num1", 0))
        num2 = float(request.args.get("num2", 0))
        operation = request.args.get("operation", "add")

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 != 0:
                result = num1 / num2
            else:
                return {"error": "Cannot divide by zero"}, 400
        else:
            return {"error": "Invalid operation"}, 400

        return {"result": result}
    except ValueError:
        return {"error": "Invalid input. Please provide numeric values."}, 400

@app.route("/echo", methods=["POST"])
def echo():
    if request.is_json:
        json_data = request.get_json()
        return {**json_data, "echoed": True}

@app.route("/status<int:status_code>")
def status(status_code: int):
    status = HTTPStatus(status_code)
    return status.phrase, status_code


if __name__ == "__main__":
    app.run(host="localhost", port=5001,debug=True)
