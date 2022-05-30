FROM 123oqlz9q/A:slim-buster

#clonning repo 
RUN git clone https://github.com/123oqlz9q/A.git /root/iqthon
#working directory 
WORKDIR /root/iqthon

# Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/iqthon/bin:$PATH"

CMD ["python3","-m","iqthon"]
