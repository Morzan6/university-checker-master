FROM nginx

RUN ["rm", "/etc/nginx/conf.d/default.conf"]
COPY uwsgi_params /etc/nginx/conf.d/
RUN ["ln", "-s", "/opt/conf/mysite_nginx.conf", "/etc/nginx/conf.d/"]
CMD ["nginx", "-g", "daemon off;"]
