#!/bin/bash

echo "Setting up development environment..."

# Initialize localization files
echo "Initializing localization files..."
cp localization/ar.json localization/en.json localization/fr.json localization/ber.json ./web/localization/

# Initialize AI models
echo "Initializing AI models..."
python python/src/ai_models/qwen_model.py --initialize
python python/src/ai_models/deepseek_model.py --initialize

# Install web dependencies
echo "Installing web dependencies..."
cd web
npm install

echo "Development environment setup complete."
