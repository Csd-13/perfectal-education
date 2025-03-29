#!/bin/bash

echo "Deploying application..."

# Deploy Flutter app
echo "Deploying Flutter app..."
cd mobile/flutter
flutter build apk --release

# Deploy Web app
echo "Deploying Web app..."
cd ../../web
npm run build

# Deploy Backend
echo "Deploying Backend..."
# Add backend deployment steps here

echo "Deployment complete."
