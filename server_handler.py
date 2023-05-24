import os

def process_server(server):
    if server == "west":
        server = "west.albion-online-data.com"
    elif server == "east":
        server = "east.albion-online-data.com"
    return server