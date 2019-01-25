
#deze gooit een broker de lucht in?
docker run --name mqtt --restart=always --net=host -tid -v /volume1/docker/mqtt/config:/mqtt/config:ro -v /volume1/docker/mqtt/log:/mqtt/log -v /volume1/docker/mqtt/data/:/mqtt/data/ toke/mosquitto
#maakt een folder voor persistentie?
mkdir -p /volume1/docker/mqtt/config
#insall mqtt.fx op windows om te testen
-->Succes
