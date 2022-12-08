# Insecure deserialization

Get detail at [here](https://portswigger.net/web-security/deserialization)

---

[Lab 1](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-modifying-serialized-objects)

Description of the lab: log in to your own account using the following credentials: wiener:peter and edit the serialized object in the session cookie to exploit this vulnerability and gain administrative privileges. Then, delete Carlos's account

Try to log in with `wiener:peter`, and we can see cookie in user session `Tzo0OiJVc2VyIjoyOntzOjg6InVzZXJuYW1lIjtzOjY6IndpZW5lciI7czo1OiJhZG1pbiI7YjowO30%3d`. Decode it with base64 and result is `O:4:"User":2:{s:8:"username";s:6:"wiener";s:5:"admin";b:0;}7`, modify this cookie, `O:4:"User":2:{s:8:"username";s:6:"wiener";s:5:"admin";b:1;}7` and encode it to base64 `YE86NDoiVXNlciI6Mjp7czo4OiJ1c2VybmFtZSI7czo2OiJ3aWVuZXIiO3M6NToiYWRtaW4iO2I6MTt9N2A=`

Using burp intercept to modify cookie, then go to admin panel, delete user carlos, and solved the lab (modify cookie every step). 

[Lab 4](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-arbitrary-object-injection-in-php)

Description of the lab: create and inject a malicious serialized object to delete the morale.txt file from Carlos's home directory. You will need to obtain source code access to solve this lab, log in credentials: wiener:peter

