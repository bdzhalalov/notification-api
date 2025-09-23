#!/bin/sh
set -eu

: "${MONGO_INITDB_ROOT_USERNAME:?}"
: "${MONGO_INITDB_ROOT_PASSWORD:?}"
: "${DB_NAME:?}"
: "${DB_USERNAME:?}"
: "${DB_PASSWORD:?}"

echo "Creating DB user '$DB_USERNAME' on DB '$DB_NAME'..."

mongo --quiet --eval "
  db = db.getSiblingDB('$DB_NAME');
  db.createUser({
    user: '$DB_USERNAME',
    pwd: '$DB_PASSWORD',
    roles: [{ role: 'readWrite', db: '$DB_NAME' }]
  });
" --username "$MONGO_INITDB_ROOT_USERNAME" --password "$MONGO_INITDB_ROOT_PASSWORD" --authenticationDatabase "admin"

echo "Database has been created."