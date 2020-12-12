FROM caddy:2.1.1-builder AS builder

RUN xcaddy build --with github.com/sillygod/cdp-cache@f714848204c38ecd5e45da15246d0ce3fe66de26

FROM caddy:2.1.1
COPY --from=builder /usr/bin/caddy /usr/bin/caddy
COPY ./Caddyfile /etc/caddy/Caddyfile