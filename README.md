# Game Project

Para correr el juego debes seguir las siguientes instrucciones en la terminal:
```sh
cd game
python3 main.py
```
# App Project

```sh
git clone
cd app
```
# Pasos para tener Python en un entorno profesional para cuentas nuevas:
```sh
sudo apt update
sudo apt -y upgrade
sudo apt install -y python3-pip  -> Gestor de paquete de dependencias
python3 -V -> ver la version de python desde consola
pip3 -V  -> Verificar que el paquete este instalado correctamente.
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev -> Dependencias utilices de python
sudo apt install python3.10-venv
python3 -m venv env  -> Creación de entortó virtual
```
```sh
source env/bin/activate
pip3 install -r requirements.txt
python3 main.py
```