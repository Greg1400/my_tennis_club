#!/bin/bash

# Update and upgrade system packages
echo "Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Install PostgreSQL
echo "Installing PostgreSQL..."
sudo apt install -y postgresql postgresql-contrib

# \Start and enable PostgreSQL servicce
echo "Starting PostgreSQL service..."
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Setup PostgreSQL DB and user
DB_NAME="my_tennis_club"
DB_USER="ghe"
DB_PASSWORD="Arnaud_greg97Django"

echo "Configuring PostgreSQL..."
sudo -i -u postgres psql <<EOF
CREATE DATABASE $DB_NAME;
CREATE USER $DB_USER WITH PASSWORD '$DB_PASS';
ALTER ROLE $DB_USER SET client_encoding TO 'utf8';
ALTER ROLE $DB_USER SET default_transaction_isolation TO 'read committed';
ALTER ROLE $DB_USER SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;
\q
EOF

# Display connection details
echo "PostgreSQL setup is complete."
echo "Database Name: $DB_NAME"
echo "Username: $DB_USER"
echo "Password: $DB_PASS"
echo "Host: localhost"
echo "Port: 5432"


