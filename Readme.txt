
#deze gooit een broker de lucht in?
docker run --name mqtt --restart=always --net=host -tid -v /volume1/docker/mqtt/config:/mqtt/config:ro -v /volume1/docker/mqtt/log:/mqtt/log -v /volume1/docker/mqtt/data/:/mqtt/data/ toke/mosquitto
#maakt een folder voor persistentie?
mkdir -p /volume1/docker/mqtt/config
#install mqtt.fx op windows om te testen
-->Succes

#https://www.instructables.com/id/How-To-Useemulate-remotes-with-Arduino-and-Raspber/
apt get install lirc (documentatie klopt niet)

#voor het instaleren van GPIO, https://www.makeuseof.com/tag/automate-garage-door-ifttt-raspberry-pi/
#sudo apt-get -y install python-rpi.gpio

#building subscribers
docker build ./ -t sub
docker-compose up
