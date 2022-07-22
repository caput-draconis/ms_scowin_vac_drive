FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app/
# RUN git clone https://github.com/caput-draconis/ms_scowin_vac_drive.git
COPY . /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
EXPOSE 8085
RUN python consumer.py
CMD [ "python","manage.py", "runserver", "0.0.0.0:8085" ]