# Access control vulnerabilities

Get details at [here](https://portswigger.net/web-security/access-control)

Type of access control attack:
 - Network sniffing
  - Capture network traffic to find sensitive data 
  - Capture user credentials
  - Keystroke monitoring
 - Impersonation (spoofing/masquerading)
  - Social engineering
  - Fictitious Subscriber
 - Rogue Infrastructure
  - Rogue mean an unauthorized resource
 - Replay attacks
  - Encrypted credentials are stolen and played back

---

[Lab 1](https://portswigger.net/web-security/access-control/lab-unprotected-admin-functionality): Unprotected admin functionality

Description of this lab: delete the user carlos

There are no hints in code, so we will find hidden files, we found `robots.txt` (a file using for preventing robot crawling data), we got

```
    User-agent: *
    Disallow: /administrator-panel
```

Modifying URL to go to /administrator-panel and delete carlos, then solved the lab.

[Lab 12](https://portswigger.net/web-security/access-control/lab-multi-step-process-with-no-access-control-on-one-step): Multi-step process with no access control on one step

Description of this lab: log in using the credentials `wiener:peter` and exploit the flawed access controls to promote yourself to become an administrator, and we can log in the credentials' administrator:admin

We need to upgrade user `wiener` without using upgrade function in admin panel. Firstly, login with admin, then using burp suite to inspect upgrade process of user carlos, website will send a payload `action=upgrade&confirmed=true&username=carlos`, then send it to burp repeater. Making new session and log in with user wiener, copy cookie and replace it at repeater with `action=upgrade&confirmed=true&username=wiener`, send it with repeater again and solved the lab.

