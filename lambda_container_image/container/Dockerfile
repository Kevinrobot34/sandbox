FROM public.ecr.aws/lambda/python:3.9

RUN  pip3 install requests

COPY app.py   ./
CMD ["app.handler"]      
