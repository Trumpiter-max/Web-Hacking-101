# Business logic vulnerabilities

Get detail at [here](https://portswigger.net/web-security/logic-flaws)

--- 

[Lab 1](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-excessive-trust-in-client-side-controls)

Description of this lab: buy a "Lightweight l33t leather jacket", we can login with credentials: `wiener:peter` 

Firstly, we will login with above credentials, then go to home and add "Lightweight l33t leather jacket" to the cart. Go to cart page to check out but it seems we do not have enough money to buy. Using burp suite to inspect what happen when we buy this one, website will send a payload like this `productId=1&redir=PRODUCT&quantity=1&price=133700` when adding item to cart. Using intercept for changing price of product to 10 buck and we can buy this item, then solved the lab.

[Lab 2](#)

[Lab 3](#)

[Lab 4](#)

[Lab 5](#)

[Lab 6](#)

[Lab 7](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-weak-isolation-on-dual-use-endpoint)

Description of this lab: access the administrator account and delete Carlos, we can login with credentials: `wiener:peter`

Try to login with credentials: `wiener:peter`, then we have form modifying data of user. However, we can change username `wiener` to `administrator`, and website will send a payload like `csrf=mm8b3N998XvfO4vR55vwxxlbaZXz6Tpo&username=administrator&current-password=test&new-password-1=test123&new-password-2=test123` to server. Moreover, we can remove parameter `current-password` and send it again to server, then got response 'Password changed successfully!'

Login with new password `test123`, go to admin pannel and delete user carlos, then solved the lab.



