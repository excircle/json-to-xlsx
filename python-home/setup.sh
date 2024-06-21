#!/bin/bash

# Install MariaDB Client + SQL Alchemy + Misc pkgs
apt update
apt install libmariadb-dev-compat build-essential vim -y
export MARIADB_CONFIG=/path/to/mariadb_config
python -m pip install sqlalchemy mariadb ipython