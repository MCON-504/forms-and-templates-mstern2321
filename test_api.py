import requests


class TestAPI:
    server_url = "http://localhost:5001"
    def call_hello_world(self):
        print("Testing / endpoint...")
        response = requests.get(f"{self.server_url}/")
        print("Response status code:", response.status_code)
        print("Check that this is a json or text response")
        print(f"Response content type:{response.headers.get('Content-Type')}")
        print("Response text:", response.text)

    def test_about_endpoint(self):
        print("Testing /about endpoint...")
        response = requests.get(f"{self.server_url}/about")
        print("Response status code:", response.status_code)
        print("Check that this is a json response")
        print(f"Response content type:{response.headers.get('Content-Type')}")
        print("Response json:", response.json())

    def test_greet_endpoint(self):
        print("Testing /greet/<name> endpoint...")
        name = "Lila"
        response = requests.get(f"{self.server_url}/greet/{name}")
        print("Response status code:", response.status_code)
        print("Check that this is a text response")
        print(f"Response content type:{response.headers.get('Content-Type')}")
        print("Response text:", response.text)


    def get_calculate_endpoint(self):
        print("Testing /calculate endpoint...")
        params = {
            "num1": 10,
            "num2": 5,
            "operation": "add"
        }
        response = requests.get(f"{self.server_url}/calculate", params=params)
        print("Response status code:", response.status_code)
        print("Check that this is a json response")
        print(f"Response content type:{response.headers.get('Content-Type')}")
        print("Response json:", response.json())


    def test_echo_endpoint(self):
        print("Testing /echo endpoint...")
        data = {"message": "Hello, API!"}
        response = requests.post(f"{self.server_url}/echo", json=data)
        print("Response status code:", response.status_code)
        print("Check that this is a json response")
        print(f"Response content type:{response.headers.get('Content-Type')}")
        print("Response json:", response.json())

    def test_status_endpoint(self):
        print("Testing /status<int:status_code> endpoint...")
        for status_code in [200, 201, 204, 400, 401, 403, 404, 500, 503]:
            response = requests.get(f"{self.server_url}/status{status_code}")
            print("Response status code:", response.status_code)
            print("Response text:", response.text)

    def test_custom_header(self):
        print("Testing custom header in /about endpoint...")
        headers = {"X-Custom-Header": "FlaskRocks"}
        response = requests.get(f"{self.server_url}/about", headers=headers)
        print("Response status code:", response.status_code)
        print("Check that this is a json response")
        print(f"Response content type:{response.headers.get('Content-Type')}")
        print("Response json:", response.json())

    def test_exception_endpoint(self):
        print("Testing /exception endpoint...")
        response = requests.get(f"{self.server_url}/exception")
        print("Response status code:", response.status_code)
        print("Check that this is a text response")
        print(f"Response content type:{response.headers.get('Content-Type')}")
        print("Response text:", response.text)


    def run_tests(self):
        print("Running API tests...")
        self.call_hello_world()
        print("\n===================.\n")
        self.test_about_endpoint()
        print("\n===================.\n")
        self.test_greet_endpoint()
        print("\n===================.\n")
        self.get_calculate_endpoint()
        print("\n===================.\n")
        self.test_echo_endpoint()
        print("\n===================.\n")
        self.test_status_endpoint()
        print("\n===================.\n")
        self.test_custom_header()
        print("\n===================.\n")
        print("All tests completed.")


if __name__ == '__main__':
    api = TestAPI()
    api.run_tests()

