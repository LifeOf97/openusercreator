FROM jwilder/nginx-proxy:alpine

# COPY vhost.d/default /etc/nginx/vhost.d/default
COPY vhost.d/www.openuser.xyz /etc/nginx/vhost.d/www.openuser.xyz
COPY vhost.d/openuser.xyz /etc/nginx/vhost.d/openuser.xyz
COPY conf.d/custom.conf /etc/nginx/conf.d/custom.conf
# COPY proxy.conf /etc/nginx/proxy.conf

# symlink multiple host
RUN ln -s /etc/nginx/vhost.d/www.openuser.xyz /etc/nginx/vhost.d/openuser.xyz
