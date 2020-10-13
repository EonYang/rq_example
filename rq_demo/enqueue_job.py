
from rq_demo.redis_client import redis_client
from rq import Queue

Queue(
    connection=redis_client
).enqueue(
    'rq_demo.sleep.keep_sleeping',
    args=[5],
    job_timeout=600)
