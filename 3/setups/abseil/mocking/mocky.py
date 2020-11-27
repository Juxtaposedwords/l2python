import requests


# Class Example is meant ot provide a single method for making an external call, which we mock out for hermetic testing.
class Example:
    def __init__(self):
        self.get = requests.get

    def Get(self, input: str) -> int:
        return requests.get(input).status_code

if __name__ == '__main__':
    x = Example()
    print('Status code: %d' % x.Get('https://imgs.xkcd.com/comics/making_progress.png'))