FROM jwilder/nginx-proxy:alpine

# COPY nginx.conf /etc/nginx/nginx.conf
COPY conf.d/custom.conf /etc/nginx/conf.d/custom.conf
COPY vhost.d/www.openuser.xyz /etc/nginx/vhost.d/www.openuser.xyz
COPY vhost.d/www.openuser.xyz /etc/nginx/vhost.d/www.openuser.xyz_location
# COPY vhost.d/default /etc/nginx/vhost.d/default
# COPY proxy.conf /etc/nginx/proxy.conf

# symlink multiple host
RUN ln -s /etc/nginx/vhost.d/www.openuser.xyz /etc/nginx/vhost.d/openuser.xyz && \
    ln -s /etc/nginx/vhost.d/www.openuser.xyz_location /etc/nginx/vhost.d/openuser.xyz_location
