#!/bin/bash

flaskswagger openbbs_middleware.main:app --host 173.255.216.176:3457 --base-path / --out-dir swagger --from-file-keyword=swagger_from_file --template ./apidoc/template.json

docker container stop swagger-ui
docker container rm swagger-ui
docker run -itd --restart always --name swagger-ui -p 5000:8080 -e SWAGGER_JSON=/foo/swagger.json -v ${PWD}/swagger:/foo swaggerapi/swagger-ui
