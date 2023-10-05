FROM nginx

ENV CONF_DIR=/etc/nginx/conf.d

RUN rm $CONF_DIR/default.conf

COPY ./nginx.conf /etc/nginx/templates/default.conf.template
