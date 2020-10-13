
from redis import StrictRedis
REDIS = {
    'host': 'localhost',
    'port': 6379
}

redis_client = StrictRedis(
    **REDIS,
    charset='utf-8',
)
