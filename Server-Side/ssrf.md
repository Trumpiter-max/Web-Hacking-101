# Server-side request forgery (SSRF)

Get details at [here](https://portswigger.net/web-security/ssrf)

Type of SSRF attack:
 - Server SSRF Attacks
 - Back-End SSRF attacks

---

[lab 1](https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-localhost)

Description of this lab: change the stock check URL to access the admin interface at http://localhost/admin and delete the user carlos

Look at any post, it has `check stock` button, try to click, we can see website send a payload like this `stockApi=http%3A%2F%2Fstock.weliketoshop.net%3A8080%2Fproduct%2Fstock%2Fcheck%3FproductId%3D1%26storeId%3D1` to server. At stockApi parameter, this is the URL of this website, change it to `stockApi=http%3A%2F%2Flocalhost%2Fadmin`, and it worked. We need delete user carlos, and we have this code from response of previous payload

```html
    <a href="/admin/delete?username=carlos">
```

The final payload is `stockApi=http%3A%2F%2Flocalhost%2Fadmin%2Fdelete%3Fusername%3Dcarlos`, and solved the lab.

[Lab 2](#)

[Lab 3](https://portswigger.net/web-security/ssrf/lab-ssrf-with-blacklist-filter)

Description of this lab: change the stock check URL to access the admin interface at http://localhost/admin and delete the user carlos. Try payload of lab 1, the response is "External stock check blocked for security reasons", it seems block keyword of lab 1, we need to change localhost to 127.1 (it will return 127.0.0.1, moreover 127.0.0.1 is blocked), a to %2561 (%25 is %, url is). The final payload `http%3A%2F%2F127.1%2F%2561dmin`. The final payload `stockApi=http%3A%2F%2F127.1%2F%2561dmin%2Fdelete%3Fusername%3Dcarlos` and solved the lab.