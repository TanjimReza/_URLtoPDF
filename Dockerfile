FROM ubuntu:20.04
ENV DEBIAN_FRONTEND="noninteractive"
WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app
RUN apt-get -qq update && apt-get -qq install -y tzdata git wkhtmltopdf python3 python3-pip \
    locales python3-lxml \
    curl pv jq \
    p7zip-full p7zip-rar
COPY requirements.txt .
# COPY extract /usr/local/bin
# RUN chmod +x /usr/local/bin/extract
RUN pip3 install --no-cache-dir -r requirements.txt && \
    apt-get -qq purge git

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
COPY . .
# COPY netrc /root/.netrc
RUN chmod +x start.sh

CMD ["bash","start.sh"]
