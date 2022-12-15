# Authentication vulnerabilities

Detail at [here](https://portswigger.net/web-security/authentication)

Three main factors:
 - knowledge factors
 - possession factors
 - inference factors 

Type of authentication attack:
 - Broad-based phishing campaigns (fake login page, website)
 - Spear phishing campaigns (Targeted phishing)
 - Credential stuffing (Brute-force attack)
 - Password spraying (Dictionary attack)
 - Man-in-the-Middle (MitM) attacks

---

[lab 1](https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-different-responses)

Description of this lab: numerate a valid username, brute-force this user's password, and we have list of users and password

Using turbo intruder extension in burp suite, try to log in then send it to turbo intruder, replace value of payload username and password to `%s`, and use this [script](/Scripts/bruteuser&pass.py) with password.txt and username.txt in [Scripts](/Scripts) folder. Starting to attack and waiting, result is username with password, then solved the lab.

[Lab 2](#)

[Lab 3](#)

[Lab 4](#)

[Lab 5](#)

[Lab 6](https://portswigger.net/web-security/authentication/password-based/lab-broken-bruteforce-protection-ip-block)

Description of this lab: brute-force the victim's password with Candidate passwords, and we have credentials: `wiener:peter` and Victim's username: `carlos`

When use wrong password, website will prevent us from login again a few seconds, so we will use brute force technique with our credentials `wiener:peter`.

Do the same as lab 1, using this [script](/Scripts/brutepass.py) with passonly.txt in [Scripts](/Scripts) folder. Starting to attack and waiting, result is username with password, then solved the lab.



