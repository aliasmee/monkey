#
FROM python:3.4-alpine AS Build
LABEL  Description="This image is a flask app." maintainer="aliasmee"

ENV DIALECT 'mysql'
ENV DRIVER 'pymysql'
ENV DB_USER 'root'
ENV DB_PASSWD ''
ENV DB_HOST ''
ENV DB_PORT '3306'
ENV DB_NAME ''

COPY app /app/
WORKDIR /app


RUN apk update && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN pip install --no-cache-dir --upgrade -r requirements.txt


EXPOSE 5000/tcp

#ENTRYPOINT
ENTRYPOINT ["python"]
CMD ["python", "blog.py"]