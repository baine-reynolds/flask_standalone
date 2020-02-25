from app import app
from redis import Redis
from rq import Queue

r = Redis(app.config["REDIS_HOST"], app.config["REDIS_PORT"]) # add app.config["REDIS_PASSWORD"] later
q = Queue(connection=r)


@app.route("/")
def index():
    trigger_backend("Hello", "world")
    return("Triggered new background event.")


def trigger_backend(arg1, arg2):
    q.enqueue(background_task, arg1, arg2)

def background_task(arg1, arg2):
    print(f"Backend says {arg1} {arg2}!")
    return