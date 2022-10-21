FROM jwilder/nginx-proxy:alpine

# COPY proxy.conf /etc/nginx/proxy.conf
COPY conf.d/custom.conf /etc/nginx/conf.d/custom.conf
COPY vhost.d/default /etc/nginx/vhost.d/default
