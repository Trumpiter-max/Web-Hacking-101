# Testing for Web Sockets security vulnerabilities

Details at [here](https://portswigger.net/web-security/websockets)

---

[Lab 1](https://portswigger.net/web-security/websockets/lab-manipulating-messages-to-exploit-vulnerabilities): Manipulating messages to exploit vulnerabilities

Description of this lab: use a Web Socket message to trigger an alert() popup in the support agent's browser

This lab includes Live chat function. We need to send this HTML code `<img src=1 onerror='alert(1)'>` in live chat. Checking how client sends payload to server in web socket history of burp suite, we can see that specific symbol being alternative like `&lt;img src=1 onerror=&#39;alert(1)&#39;&gt;`. You need to type normal message like `test` first then modify it like this `{"message":"<img src=1 onerror='alert()'>;"}` and solved the lab.

[Lab 2](https://portswigger.net/web-security/websockets/lab-manipulating-handshake-to-exploit-vulnerabilities): Manipulating handshake to exploit vulnerabilities

This lab has same description of previous lab, but we need to exploit handshake. 

Try to use same technique in lab 1, and our IP address will be banned. So we need to reset this lab instance or using some other methods for changing IP address like using flag `X-Forwarded-For` in HTTP header.

In fact, we can do it same as lab 1, but we need to modify payload like this, also payload should be obfuscated:

```json
    {"message":"<img src=1 oNeRrOr=alert`1`>"}
    {"user":"You","content":"<img src=1 oNeRrOr=alert`1`>"}
``` 



