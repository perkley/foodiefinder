#!/bin/bash
# This updates the code

# Navigate to your project directory
cd /home/ubuntu/foodiefinder

# Stash what was changed
sudo git stash

# Pull the latest code from Git
echo "Pulling latest code from Git..."
git config --global --add safe.directory /home/ubuntu/foodiefinder
git pull origin main

# Activate your virtual environment
echo "Activating virtual environment..."
source /home/ubuntu/env/bin/activate

# Make the requirements.txt file
pipenv requirements > requirements.txt
pip install -r requirements.txt

# Run Django management commands
echo "Running Django management commands..."
python manage.py collectstatic --noinput
python manage.py migrate

echo "Restarting Nginx..."
sudo service nginx restart

echo "Reloading Supervisor..."
sudo supervisorctl reload

echo "Update completed successfully."
