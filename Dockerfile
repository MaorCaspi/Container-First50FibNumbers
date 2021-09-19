FROM python
MAINTAINER Maor Caspi
ADD fib.py /
CMD [ "python", "./fib.py" ]