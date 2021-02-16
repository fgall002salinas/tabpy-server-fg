from tabpy.tabpy_tools.client import Client
client = Client('http://localhost:9004/')
client.set_credentials('kikin', 'karate10')

# Deploying a Function

# * Add Function


def add(x, y):
    import numpy as np
    return np.add(x, y).tolist()


client.deploy('add', add, 'Adds two numbers x and y', override=True)
