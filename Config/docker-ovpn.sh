# curl -sSL https://get.docker.com | sh
# Pick a name for the $OVPN_DATA data volume container, it will be created automatically.

OVPN_DATA="ovpn-data"
IP=`curl --silent ipecho.net/plain`
CLIENTNAME="databox"
#IMAGE=kylemanna/openvpn
IMAGE=matrixanger/rpi-ovpn

echo $IP, $OVPN_DATA, $CLIENTNAME

# Initialize the $OVPN_DATA container that will hold the configuration files and certificates

docker volume create --name $OVPN_DATA
docker run -v $OVPN_DATA:/etc/openvpn --rm $IMAGE ovpn_genconfig -u udp://$IP
docker run -v $OVPN_DATA:/etc/openvpn --rm -it $IMAGE ovpn_initpki

# Start OpenVPN server process
docker run -v $OVPN_DATA:/etc/openvpn -d -p 1194:1194/udp --cap-add=NET_ADMIN $IMAGE

# Generate a client certificate without a passphrase
docker run -v $OVPN_DATA:/etc/openvpn --rm -it $IMAGE easyrsa build-client-full $CLIENTNAME nopass

# Retrieve the client configuration with embedded certificates
docker run -v $OVPN_DATA:/etc/openvpn --rm $IMAGE ovpn_getclient $CLIENTNAME > $CLIENTNAME.ovpn

