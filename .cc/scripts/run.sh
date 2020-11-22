#!/bin/bash

. __/bin/activate

python -m openbbs_middleware.main -i production.ini.template -p 3457
