import socket

from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host="redis", port=6379)
host = socket.gethostname()


@app.route("/")
def hello():
    redis.incr("hits")
    return (
        "Hello World! "
        f"I have been seen {int(redis.get('hits'))} times. "
        f"My Host name is {host}\n"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
