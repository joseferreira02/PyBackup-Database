#Intall python
FROM python:3.11-slim

#Working directory
WORKDIR /app

#Copy the requirements file
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copy the rest of the application code
COPY . .

#Run the application
CMD ["python", "./cli.py"]