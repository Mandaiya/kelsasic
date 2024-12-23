FROM nikolaik/python-nodejs:python3.10-nodejs20
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY . /app/
WORKDIR /app/
RUN git clone https://github.com/Mandaiya/kelsasic kelsasic
RUN cd kelsasic && pip3 install -U -r requirements.txt
CMD cd kelsasic && bash start
