#!/bin/bash

echo "Running tests..."

# Run Flutter tests
echo "Running Flutter tests..."
cd mobile/flutter
flutter test

# Run Python tests
echo "Running Python tests..."
cd ../../python
pytest

# Run Rust tests
echo "Running Rust tests..."
cd ../../rust
cargo test

# Run Web tests
echo "Running Web tests..."
cd ../../web
npm test

echo "All tests completed."
