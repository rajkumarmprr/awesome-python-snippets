FROM python:3.11
EXPOSE 6000
WORKDIR /src
COPY . .
RUN pip install flask
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "6000"]