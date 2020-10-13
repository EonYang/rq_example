from setuptools import setup

setup(
    name='rq_demo',
    packages=['rq_demo'],
    install_requires=[
        'redis>=3.5.3',
        'rq>=1.5.2'
    ],
)
