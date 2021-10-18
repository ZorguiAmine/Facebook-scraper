FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

#upgrade pip
RUN pip install --upgrade pip

# set working directory
WORKDIR ./src

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]