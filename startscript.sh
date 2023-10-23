#!/bin/sh

# Installing pipreqs and generating requirements.txt
pip install pipreqs
pipreqs ./app --force --savepath requirements.txt
# Installing dependencies
pip install --no-cache-dir -r reqs.txt
pip install --no-cache-dir -r requirements.txt
# Start your Flask app
python ./app/entrypoint.py