FROM astrocrpublic.azurecr.io/runtime:3.0-2

USER root

# Install OpenJDK-17
RUN apt update && \
    apt-get install -y openjdk-17-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Set JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64/

COPY requirements.txt . 
RUN pip install -r requirements.txt

RUN export JAVA_HOME
