# Project-2020-Emerging-Technologies

# Linux
```bash
export FLASK_APP=app.py
python3 -m flask run
```

# Windows
```bash
set FLASK_APP=app.py
python -m flask run
```

```bash
docker build . -t app-image
docker run --name app-container -d -p 5000:5000 app-image
```
