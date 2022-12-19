All below content coming from a book named `The web application hacker's handbook finding and exploiting security flaws`

- **Chapter 2: Core Defense Mechanisms**
    
    ## Intro
    
    - The security problem is untrusted user input
    - 4 core elements of defense mechanisms: handling user access, user input, attackers, managing web application
    
    > Knowing your enemy is the first rule of warfare
    > 
    
    ## Handling user access
    
    - **Authentication**: mechanisms suffer from **both design and implementation**. Attackers can identify other users’ usernames, guess their passwords, or bypass the login function by its logic
    - **Session management**: attackers can find the mechanism of generating a token session → the session is ideally expired, usually in encrypted form to prevent tampering
    - **Access control**: needs to implement some fine-grained logic, numerous user roles which specific privileges separately, specific functions come with transaction limits and other checks
    
    ## Handling User Input
    
    - Must handle user input in a safe manner
    - Input validation and do not employ protective mechanisms everywhere
    
    ## Varieties of Input
    
    - Must impose very stringent validation checks on a specific item of input
    - Must tolerate a broader range of possible input or arbitrary (any type) input
    - Reject the request and log the incident for potential investigation
    
    ## Approaches to Input Handling
    
    - Employing a blacklist, but blacklist-based filters can be bypassed
    - Employing a whitelist, but the application can be confused by apostrophes or hyphens
    
    ## Sanitization
    
    - Input will be suitably encoded or “escaped” before processing
    - Being often highly effective and difficult to achieve if several kinds of potentially malicious data
    
    ## Safe Data Handling
    
    - Using safe programming methods
    - Cannot be applied to every kind of task
    
    ## Semantic Checks
    
    - some input supplied by the attacker is identical to the input that an ordinary, nonmalicious user may submit
    - needs to validate that the account number submitted belongs to the user who has submitted it
    
    ## Boundary Validation
    
    - Taking measures to defend itself against malicious input
    - Data may be trusted and processed without any further checks or concerns about possible attacks
    - Data validation is performed at each of these trust boundaries
    - Similar defenses would need to be implemented at the relevant trust boundaries
    
    ## Multistep Validation and Canonicalization
    
    - Attackers can smuggle malicious data through the validation mechanism
    - Perform sanitization steps recursively, continuing until no further input modifications
    - Q: get an example code of Multistep Validation
    
    ## Handling attackers
    
    - **Handling Errors**: the product application should never return any
    system-generated messages or other debug information in its responses. Effective error handling is often integrated with the application’s logging
    mechanisms

    - **Maintaining Audit Logs**: Effective audit logs typically record the time of each event, the IP address from which the request was received, and the user’s account and store audit logs on an autonomous system that accepts only update messages from the main application

    - **Alerting Administrators:** can use a combination of factors to diagnose that a determined attack is underway and can aggregate related events into a single alert where possible. Typically use a mixture of signature- and anomaly-based rules to identify malicious use

    - **Reacting to Attacks:** built-in mechanisms to react defensively
    
    - **Managing the Application:** manage user accounts and roles, access monitoring
    and audit functions, perform diagnostic tasks, and configure aspects of the
    application’s functionality

---

- **Chapter 3: Web application Technology**
    
    A short primer on the key technologies encountering attacks 
    
    **The HTTP Protocol**
    
    - Is core communications protocol, message-based model
    - Retrieving static text-based resources, using the stateful TCP protocol as its transport
    mechanism
    
    ## HTTP Header
    
    - [https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)
    
    ## HTTP Method
    
    - [https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
    - The GET method is designed to retrieve resources. The POST method is designed to perform actions
    
    ## URLs
    
    - Unique identifier for a web resource through which that resource can be retrieved:
        
        ```html
        protocol://hostname[:port]/[path/]file[?param=value]
        ```
        
    - Not only absolute form, but also URLs may be specified relative to a particular
    host, or relative to a particular path on that host
    
    ## REST
    
    - Representational state transfer
    - Requests and responses contain representations of the current
    state of the system’s resources
    - URLs containing parameters within the query string do themselves
    conform to REST constraints (REST-style URL)
    
    ## Cookies
    
    - The cookie mechanism enables the server to send items of data to the client, which
    the client stores and resubmits to the server
    - Consist of a name/value pair
    - diff cookie / local storage / cache storage
    
    ## Status Codes
    
    [https://developer.mozilla.org/en-US/docs/Web/HTTP/Status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
    
    Can use custom status code for request
    
    ```html
    1xx — Informational.
    2xx — The request was successful.
    3xx — The client is redirected to a different resource.
    4xx — The request contains an error of some kind.
    5xx — The server encountered an error full filling the request.
    ```
    
    ## HTTPS
    
    - HTTP tunneled over the secure transport mechanism, Secure Sockets
    Layer (SSL)
    - Protects the privacy and integrity of data passing over the
    network
    
    ## HTTP Proxies
    
    - Relaying the requests to the relevant web servers and forwarding their responses back to the browser
    - Extracting the hostname and port and using these to direct the
    request to the correct destination web server
    - If the proxy allows the request, it keeps the TCP connection open, and pure TCP-level relay to the destination web server
    - Virtual host configure, web proxy
    
    ## HTTP Authentication
    
    Encode the user credentials 
    
    - Basic is a simple authentication mechanism using Base64-encoded (is insecure)
    - NTLM using Windows NTLM protocol.
    - The Digest using MD5 checksums
    
    Any HTTP message can be protected from eavesdropping attacks by using HTTPS
    as a transport mechanism
    
    ## Web Functionality
    
    - **Server-Side Functionality**: When a user requests a dynamic resource, the server’s response
    is created on the fly, and each user may receive content that is uniquely customized for him or her
        - Technologies
            - Scripting languages such as PHP, VBScript, and Perl
            - Web application platforms such as [ASP.NET](http://asp.net/) and Java
            - Web servers such as Apache, IIS, and Netscape Enterprise
            - Databases such as MS SQL, Oracle, and MySQL
            - Other back-end components such as file systems, SOAP-based web services,
            and directory service
    - **Client-Side Functionality**: receive user input and actions and present
    the results to the user, it needs to provide a client-side user interface
        - Technologies
            - HTML
            - Hyperlinks
            - Forms
            - CSS
            - JavaScript
            - VBScript
    - **Document Object Model (DOM):** abstract representation of an HTML document that can be queried and manipulated through its API (required)
        - Technologies
            - Ajax
            - JSON
    - **Same-Origin Policy**: key mechanism implemented within browsers that
    is designed to keep content that came from different origins from interfering
    with each other
    - **HTML5**
    - **Web 2.0**
    - **Browser Extension Technologies**: custom code to extend the browser’s
    built-in capabilities in arbitrary ways
    - **State and Sessions**: track the state of each user’s interaction with the application across multiple requests
    - **Encoding Schemes**: ensure that these mechanisms can safely handle unusual characters and binary data
    - **URL Encoding**: encode any problematic characters
    within the extended ASCII character set so that they can be safely transported
    over HTTP (with % prefix)
    - **Unicode Encoding**: %u prefix followed by the character’s Unicode code point expressed in
    hexadecimal
    - **HTML Encoding**: represent problematic characters so that they can be
    safely incorporated into an HTML document
        - Base64 Encoding: allows any binary data to be safely represented using only
        printable ASCII characters
        - Hex Encoding: using ASCII characters to represent the hexadecimal block
    - R**emoting and Serialization Frameworks**: allows developers to partly abstract away from
    the distributed nature, conventional desktop application