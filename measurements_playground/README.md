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
1. Przejdź do katalogu zawierającego skrypt i uruchom go poleceniem
```bash
python3 test_subscribe.py
```
2. Będąc na malinie, uruchom skrypt `send.py`
```bash
python3 send.py
```
