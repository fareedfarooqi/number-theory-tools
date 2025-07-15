FROM python:3.11

RUN apt-get update && \
    apt-get install -y build-essential afl++

WORKDIR /src

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["py-afl-fuzz", "-i", "seeds/initial_seeds", "-o", "afl-out/", "--", "python3", "fuzz_totient_afl.py"]