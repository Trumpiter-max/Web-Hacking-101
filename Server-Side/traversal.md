# Directory traversal

Get detail at [here](https://portswigger.net/web-security/file-path-traversal)

---

[Lab 1](https://portswigger.net/web-security/file-path-traversal/lab-simple): simple file path traversal

Description of this lab: retrieve the contents of the `/etc/passwd` file

Firstly, we need to find what is relative to file path, we can find at image of product have path in source code. For example:
```html
    <section class="product">
        <h3>Hydrated Crackers</h3>
        <img src="/resources/images/rating2.png">
        $40.06
        <img src="/image?filename=54.jpg">
            <label>Description:</label>
            ...
        <div class="is-linkback">
            <a href="/">Return to list</a>
        </div>
    </section>
```

Image source have parameter `?filename`, try to replace `54.jpg` to `51.jpg` with `edit attribute` or expand URL like this `example.com/image?filename=51.jpg` then website will load 51.jpg. Replace it with payload `../../../etc/passwd` then solved the lab. 

[Lab 2](#)

[Lab 3](#)

[Lab 4](https://portswigger.net/web-security/file-path-traversal/lab-superfluous-url-decode): superfluous URL-decode

Description of this lab: retrieve the contents of the `/etc/passwd` file in the display of product images, performs a URL-decode of the input before using it

It has same solution of lab 1, but we need to modify payload, replace `/` to `%252f`. Final payload `..%252f..%252f..%252fetc/passwd` then solved the lab

