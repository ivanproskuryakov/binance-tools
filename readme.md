### Installation

```
python -m venv .env
source .env/bin/activate

pip install -r requirements.txt
pip install -r requirements-ubuntu.txt
pip install --force-reinstall -r requirements.txt
```

### Training

```
psql -U postgres
create database ta_train;

ENV=train python db_flush_sync.py
ENV=train python db_populate_ohlc_train.py
ENV=train python model_train_window_gru.py

```

### Running

```
psql -U postgres
create database ta_dev;

ENV=dev python db_flush_sync.py
ENV=dev python predict.py 5m
```

### Testing

```
psql -U postgres
create database ta_test;

ENV=test python -m pytest test
ENV=test python -m pytest --log-cli-level DEBUG -s test/service/test_trader.py
ENV=test python -m pytest test/service/test_trader.py
ENV=test python -m pytest -s test/service/test_trader.py

```