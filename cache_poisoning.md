#Cache Poisoning

X-Cache: miss -> missed the cache (request sent to web server directly)
X-Cache: hit  -> hit the cached (not the web server)

Get the cached key

    Pragma: x-get-cache-key
 

1. Find a point of injection that is reflected in the response (get param, header, cookie)
2. Confirm that this "point of injection" is not part of the cached keys.
4. Create a payload (xss, redirect, etc...)
    - string from a GET params or cookie (-> escape the string and XSS)
    - host from x-headers-type (-> redirect to exploit server)

   
Param Miner:

- Guess query params: some query params are excluded from cached key
- Guess everything!
