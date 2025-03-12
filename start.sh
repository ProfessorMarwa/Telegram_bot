#!/bin/bash
echo "Starting New Bot Deployment..."
pip install -r requirements.txt
uvicorn bot:app --host 0.0.0.0 --port $PORT
