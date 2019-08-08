
```console
$ make setup

python3 -m venv .venv
```

```console
$ . .venv/bin/activate
(.venv) $
```

```console
(.venv) $ make req dev

pip install -r requirements.txt
pip install -r dev-requirements.txt
```

```console
(.venv) $ make routes

pycodestyle app.py coord/model.py extensions.py
pyflakes app.py coord/model.py extensions.py
python app.py exit
c: {'x': 0, 'id': 'test', 'y': 0}
all: [{'x': 0, 'id': 'test', 'y': 0}]
```

```console
(.venv) $ make run

./.venv/bin/python app.py
c: {'id': 'test', 'y': 0, 'x': 0}
all: [{'id': 'test', 'y': 0, 'x': 0}]
Bottle v0.12.17 server starting up (using GunicornServer())...
Listening on http://127.0.0.1:5000/
Hit Ctrl-C to quit.

[2019-08-08 17:46:21 -0400] [16455] [INFO] Starting gunicorn 19.9.0
[2019-08-08 17:46:21 -0400] [16455] [INFO] Listening at: http://127.0.0.1:5000 (16455)
[2019-08-08 17:46:21 -0400] [16455] [INFO] Using worker: sync
[2019-08-08 17:46:21 -0400] [16460] [INFO] Booting worker with pid: 16460
```
