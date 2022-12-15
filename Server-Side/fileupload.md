# File upload vulnerabilities

Get details at [here](https://portswigger.net/web-security/file-upload)

Type of file upload vulnerabilities attack:
 - Malicious Files
 - Public File Retrieval 

---

[Lab 1](https://portswigger.net/web-security/file-upload/lab-file-upload-remote-code-execution-via-web-shell-upload)

Description of this lab: log in to your own account using the following credentials: wiener:peter, upload a basic PHP web shell and use it to exfiltrate the contents of the file /home/carlos/secret. Submit this secret using the button provided in the lab banner

Using this PHP script to make file evil.php

```php
    <?php 
        echo file_get_contents('/home/carlos/secret'); 
    ?>
```

Log in with wiener:peter, uploading evil.php at upload avatar. After uploading file, modify URL like `example.com/files/avatars/evil.php`, see its response `zSkiPK4JTu7lRHsDH7P0ExrgGoWZnDsr`. Go back home and submit secret, and solved the lab.

[Lab 2](#)

[Lab 3](#)

[Lab 4](#)

[Lab 5](https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-obfuscated-file-extension)

Description of this lab: obfuscation technique to bypass defense (only upload JPG or PNG file)

It seems has filtered extension name of uploaded file, do the same as lab 1, but we need to change file name to `evil.php%00.png` (%00 meaning null (NUL in ASCII), when file is uploaded, system can not understand this, then it removes part after %00, then file name will be evil.php). We got secret `rakmOG0R8Z69H8eQEahqObm8nuSsf3r7`, go back home and submit, then solved the lab.