# Crypto-Pi
Unique way of viewing cryptocurrency chart
## Installation
### 1. Turn on SPI
```commandline
sudo raspi-config
```
Select `Interfacing Options`, `SPI` then select `Yes`
### 2. Install dependencies for Waveshare display
```commandline
sudo apt-get update
sudo apt-get install python3-pip python3-pil python3-numpy
sudo pip3 install RPi.GPIO
```
### 3. Install drivers for Waveshare display
```commandline
git clone https://github.com/waveshare/e-Paper.git
pip3 install ./e-Paper/RaspberryPi_JetsonNano/python/
```
### 4. Download crypto-pi source
```commandline
git clone https://github.com/lumtwj/crypto-pi.git
cd crypto-pi
```
### 5. Install crypto-pi dependencies
```commandline
sudo apt-get install python3-matplotlib
```
## Setup
### 1. Setup crontab
```commandline
crontab -e
```
### 2. Add the following line:
```commandline
*/5 * * * * /home/pi/crypto-pi/fetch_crypto_job.sh
```
This schedule crypto-pi to fetch latest chart every 5 minutes
### 3. Schedule crypto-pi to display chart on boot
```commandline
sudo cp crypto-pi.service /lib/systemd/system/crypto-pi.service
sudo systemctl enable crypto-pi
```
### 4. Start crypto-pi service
```commandline
sudo systemctl start crypto-pi
```
## Customising
### 1. Editing configuration file
```commandline
nano config.js
```
### 2. Adding more token
```json
{
  "token_list": ["bitcoin", "ethereum"]
}
```
