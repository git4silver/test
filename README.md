# Minimal Flask Demo

Prosty projekt testowy do sprawdzenia reverse discovery.

## Pliki
- `app.py` — minimalna aplikacja Flask
- `requirements.txt` — zależności
- `Dockerfile` — obraz Dockera

## Endpointy
- `GET /` — podstawowa odpowiedź JSON
- `GET /health` — health check

## Uruchomienie lokalnie
```bash
pip install -r requirements.txt
python app.py
```

Aplikacja będzie dostępna pod:
- `http://localhost:5000/`
- `http://localhost:5000/health`

## Uruchomienie w Dockerze
```bash
docker build -t minimal-flask-demo .
docker run -p 5000:5000 minimal-flask-demo
```

## Po co ten projekt
To jest mały, sensowny projekt wejściowy do testów:
- odczytu struktury plików
- wykrywania Flask + Docker
- generowania reconstructed brief
- generowania architecture reconstruction
- generowania gap analysis
