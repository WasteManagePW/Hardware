## Testowa aplikacja do testowania wysyłania pomiarów do brokera [MQTT](https://pl.wikipedia.org/wiki/MQTT)

### Przygotowanie - malina
* Podłącz czujnik do maliny wg schematu (VCC -> 5V, GND -> GND, TRIGG -> GPIO24, ECHO -> GPIO23)
* Przejdź do katalogu `measure_app`
```bash
cd measure_app
```

### Przygotowanie - PC
* Upewnij się, że masz wersję Pythona przynajmniej 3.5
```bash
python3 --version
```
* Zainstaluj `pip`
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```
Jeżeli podczas instalacji trafiłeś na błąd, bardzo możliwe że nie masz wymaganych paczek:
```bash
sudo apt install curl python3-setuptools
```
* Ściągnij paczkę `paho-mqtt`
```bash
python3 -m pip install paho-mqtt --user
```

## Użycie
1. Będąc w tym (`measurements_playground`) katalogu polecam najpierw stworzyć virtual enva:
```bash
sudo apt install python3-venv
python3 -m venv .venv
source .venv/bin/activate
```
2. Następnie ściągamy Django i paho-mqtt
```bash
python -m pip install django paho-mqtt
```
3. I odpalamy server
```bash
cd server/backend
python manage.py runserver --noreload
```
4. Następnie uruchamiamy na malince skrypt do wysyłania wyników pomiarów
```bash
python3 send.py
```
To już koniec! Nasze pomiary (czytane z bazy danych) możemy zobaczyć, logując się w przeglądarce pod linkiem `127.0.0.1:8000/admin` loginem `admin` i hasłem `smartcity`. Następnie klikamy w **Measurements** i odświeżając stronę oglądamy napływające pomiary
