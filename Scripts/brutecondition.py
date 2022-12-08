import string

def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                            concurrentConnections=5,
                            requestsPerConnection=100,
                            pipeline=False
                            )
        
    for word in string.printable:
        engine.queue(target.req, [word.rstrip()])


def handleResponse(req, interesting):
    # currently available attributes are req.status, req.wordcount, req.length and req.response
    if "Welcome back" in req.response:
        table.add(req)