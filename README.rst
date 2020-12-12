cdp-cache bug
-------------
cdp-cache does not handle non-empty non-200 responses correctly. The response
content is handled correctly, but the status code is rewritten to 200.

Issue raised here: https://github.com/sillygod/cdp-cache/issues/35

This is a bare-bones example project to illustrate the issue. Run::

    $ docker-compose up

to start the project.

Requests to localhost:5000 are handled by Gunicorn/Django directly while
requests to localhost:8080 are proxied through Caddy (with cdp-cache
installed). The responses from Caddy have the wrong status code::

    $ curl localhost:5000/ -i
    HTTP/1.1 403 Forbidden
    Server: gunicorn/19.9.0
    Date: Thu, 10 Dec 2020 15:32:04 GMT
    Connection: close
    Transfer-Encoding: chunked
    Content-Type: text/html; charset=utf-8

    The status should be 403


    $ curl localhost:8080/ -i
    HTTP/1.1 200 OK
    Content-Type: text/html; charset=utf-8
    Date: Thu, 10 Dec 2020 15:32:10 GMT
    Server: Caddy
    X-Cache-Status: skip
    Content-Length: 24

    The status should be 403


Removing cdp-cache from the Caddyfile resolves the issue::

    $ curl localhost:8080/ -i
    HTTP/1.1 403 Forbidden
    Content-Type: text/html; charset=utf-8
    Date: Thu, 10 Dec 2020 15:44:01 GMT
    Server: Caddy
    Server: gunicorn/19.9.0
    Content-Length: 24

    The status should be 403

Responses without any content are handled correctly, for some reason::

    $ curl localhost:8080/ -i
    HTTP/1.1 403 Forbidden
    Content-Type: text/html; charset=utf-8
    Date: Thu, 10 Dec 2020 15:45:58 GMT
    Server: Caddy
    X-Cache-Status: skip
    Content-Length: 0
