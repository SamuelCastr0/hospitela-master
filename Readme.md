INSTALL DOCKER AND DOCKER-COMPOSE <br />

```
./install-docker.sh
```

GENERATE CERTIFICATE AND KEY

```
openssl req  -nodes -new -x509  -keyout /etc/openssl/key.pem -out /etc/openssl/cert.pem
```

DEPLOY SERVER

```
docker-compose up --build
```

DEPLOY SERVER (NO LOGS)

```
docker-compose up --build -d
```

ACCESS SERVER ON
http://localhost:80
