#python image 
FROM python:3.10.1 

#two python packages 
RUN pip install flask
RUN pip install flask-mysqldb

# ENV PORT=127.0.0.1
#create image
COPY --from=python:3.10.1  /myflask /myflask

ENTRYPOINT echo Install Flask and MySQL Complete 