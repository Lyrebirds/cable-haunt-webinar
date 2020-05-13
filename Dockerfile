# docker build -t cable-haunt-webinar . 
# docker run --name cable-haunt-webinar -d --rm -it cable-haunt-webinar
# docker exec -it cable-haunt-webinar /bin/bash

FROM ubuntu:eoan

RUN apt-get update
RUN apt-get -y install git python3 python3-pip wget tmux vim git-lfs gdb gdbserver nano locales seccomp libc6-dbg libevent-dev bison automake build-essential pkg-config libncurses5-dev
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade pwntools
RUN pip3 install --upgrade future
RUN pip3 install --upgrade filebytes
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN echo "source /opt/pwndbg/gdbinit.py" > /root/.gdbinit

RUN rm -rf /var/lib/apt/lists/* \
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

WORKDIR /root

COPY . /root

RUN git lfs install
RUN git lfs pull
RUN git submodule update --init --recursive
