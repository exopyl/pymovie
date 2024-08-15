FROM python:3.8
LABEL version="0.2"

# Workaround https://unix.stackexchange.com/questions/2544/how-to-work-around-release-file-expired-problem-on-a-local-mirror
RUN echo "Acquire::Check-Valid-Until \"false\";\nAcquire::Check-Date \"false\";" | cat > /etc/apt/apt.conf.d/10no--check-valid-until

RUN apt-get update
RUN pip install --upgrade pip

RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY requirements.txt /
RUN pip install -r requirements.txt

#WORKDIR "/mnt"
