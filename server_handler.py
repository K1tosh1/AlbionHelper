import os

def process_server(server):
    if server == "west":
        server = "west.albion-online-data.com/api/v2/stats/prices/"
    elif server == "east":
        server = "east.albion-online-data.com/api/v2/stats/prices/"
    return server