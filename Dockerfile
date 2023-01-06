FROM python:3.8.10-slim
RUN apt-get update
RUN apt-get install -y python3-opencv
RUN apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0
RUN pip3 install --upgrade pip
WORKDIR /app
COPY . /app
RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
RUN pip3 --no-cache-dir install -r requirements.txt

RUN pip3 install opencv-python-headless

CMD ["gunicorn", "-b" , "0.0.0.0:8000", "run:app"]