FROM python:3.11

WORKDIR /src/usr/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["py-afl-fuzz", "-i", "seeds/initial_seeds", "-o", "afl-out/", "--", "python3", "fuzz_totient_afl.py"]