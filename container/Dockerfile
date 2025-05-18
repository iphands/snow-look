FROM fedora:latest
RUN dnf update -y
RUN dnf install -y python3 mesa-libGL
COPY src /src
RUN groupadd user -g 1000 && useradd -u 1000 -g 1000 -r -s /bin/bash -c "User" user
RUN mkdir -p /src /data /home/user && chown user:user -R /src /data /home/user
WORKDIR /src
USER user
RUN python3 -mvenv venv && source venv/bin/activate && pip install -r requirements.txt
ENTRYPOINT [ "/bin/bash", "-c", "cd /src && source venv/bin/activate && python3 /src/main.py" ]
