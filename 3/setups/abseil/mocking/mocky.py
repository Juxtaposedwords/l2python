import requests


# Class Example is meant ot provide a single method for making an external call, which we mock out for hermetic testing.
class Example:
    def __init__(self):
        self.get = requests.get

    def Get(self, input: str) -> int:
        return requests.get(input).status_code