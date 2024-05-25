#!/bin/bash
# This updates the code

# Navigate to your project directory
cd /home/ubuntu/foodiefinder

# Pull the latest code from Git
echo "Pulling latest code from Git..."
git pull origin main

# Activate your virtual environment
echo "Activating virtual environment..."
source /home/ubuntu/env/scripts/activate

# Run Django management commands
echo "Running Django management commands..."
python manage.py collectstatic --noinput
python manage.py migrate

# Restart the services (e.g., Gunicorn and Nginx)
echo "Restarting Gunicorn..."
sudo systemctl restart gunicorn

echo "Restarting Nginx..."
sudo systemctl restart nginx

echo "Reloading Supervisor..."
sudo supervisorctl reload

echo "Deployment completed successfully."
