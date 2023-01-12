# Fargasht
Fargasht is a simple program to simulate evolution in nature using neural networks and machine learning
## Use
### first clone the repository
```
git clone https://github.com/Null-byte-00/Fargasht/
```
### enter directory
```
cd Fargasht
```
### create a virtual enviroment
```
virtualenv venv
```
### activate virtual enviroment
windows(Powershell):
```
.\venv\script\activate.ps1
```
linux:
```
source venv/bin/activate
```
### Install requirements
```
pip install -r requirements.txt
```
### run the simulator
```
python main.py
```
## How it works?
first you run the program you'll see 100 planktons randomly moving around. each of these creatures have their own neural network. but their brain connections are 
completely random so they are moving randomly.
after each generation all the population dies. but those who are on the right side of the screen have a chance to mate and create the next generation
<br>here is generation zero<br>
![alt text](https://github.com/Null-byte-00/Fargasht/blob/main/gen0.gif)
<br>and here is generation 91<br>
![alt text](https://github.com/Null-byte-00/Fargasht/blob/main/gen91.gif)
<br>as you can see the planktons' brains have evolved to go to the right side of the screen
