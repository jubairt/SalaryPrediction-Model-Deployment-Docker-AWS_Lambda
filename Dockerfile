# for lamda container

FROM public.ecr.aws/lambda/python:3.10

WORKDIR /var/task

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY model.pkl .
COPY lambda_function.py .

CMD ["lambda_function.lambda_handler"]
