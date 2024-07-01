# Smart Environmental Monitoring Sensor (SEMS)
A multi-modular environmental sensor project using Python, Flask, Flask-SocketIO, and Bootstrap that displays real-time temperature, air quality, radiation, and other sensor readings using your Raspberry Pi.

![SEMS](img/SEMS.gif) 
  
## Writeup
https://abhinavballa.github.io/SEMSweb/

## Prerequisites
Make sure to install the necessary drivers on your Raspberry Pi.
  
## Steps on how to run on Raspberry Pi
1. Clone the repository
```
git clone https://github.com/matthewlimm/SEMS
```
2. Create a Python virtual environment
```
python -m venv .venv
source .venv/bin/activate
```
3. Install the dependencies
```
pip install -r requirements.txt
```
4. Run the application
```
flask run --host=0.0.0.0
```
5. Access the application using the following URL
```
http://<IP>:5000
```
