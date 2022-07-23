import json
import pika
import django
from sys import path
import os

#path.append('E:\BIT-FSE-Projects\C2-Assignment2\ms_scowin_vac_drive\ms_scowin_vac_drive\settings.py') #Your path to settings.py file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ms_scowin_vac_drive.settings') 
django.setup()
from vac_drive.models import Student

# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', heartbeat=600, blocked_connection_timeout=300))
# connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit_mq'))
# amqp_url = os.environ['AMQP_URL']

amqp_url = 'amqp://rabbit_mq?connection_attempts=10&retry_delay=10'
url_params = pika.URLParameters(amqp_url)

# connect to rabbitmq
connection = pika.BlockingConnection(url_params)
channel = connection.channel()
channel.queue_declare(queue='vacdrive')

def callback(ch, method, properties, body):

    print("Received in vacdrive...")
    print(body)
    data = json.loads(body)
    print(data)

    if properties.content_type == 'student_created':
        if not isinstance(data,list):
            data = [data]
        for d in data:
            student = Student.objects.create(id=d['id'], studentName=d['studentName'], dob=d['dob'], gender=d['gender'], aadharID=d['aadharID'], existingComorbidites=d['existingComorbidites'])
            student.save()
            print("student created")
        
    elif properties.content_type == 'student_updated':       
        student = Student.objects.get(id=data['id'])
        student.studentName = data['studentName']
        student.dob = data['dob']
        student.gender = data['gender']
        student.aadharID = data['aadharID']
        student.existingComorbidites = data['existingComorbidites']
        student.save()
        print("student updated")    
    ch.basic_ack(delivery_tag=method.delivery_tag)
  
channel.basic_consume(queue='vacdrive', on_message_callback=callback)
print("Started Consuming...")
channel.start_consuming()
