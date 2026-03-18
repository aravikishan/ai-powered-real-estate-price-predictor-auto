#!/bin/bash
set -e
echo "Starting AI-Powered Real Estate Price Predictor..."
uvicorn app:app --host 0.0.0.0 --port 9132 --workers 1
