FROM python:3.7
COPY . /app
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone
WORKDIR ./app
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]
