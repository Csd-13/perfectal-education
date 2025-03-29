# Perfectal Education

## Overview
Perfectal Education is a comprehensive educational platform designed specifically for the Algerian educational system. The platform integrates advanced AI technologies to deliver personalized learning experiences across multiple languages and educational contexts.

## Key Features
- **Multilingual Support**: Arabic (primary), French, English, Latin, Italian, German, and Tamazight
- **AI-Powered Learning**: Integration with multiple AI models (Qwen 2.5, DeepSeek R1, GPT-4O, Claude 3.5 Haiku)
- **Educational Content Focus**: Strictly focused on Algerian educational content
- **Cross-Platform**: Available on mobile (Android, iOS) and web platforms
- **File Processing**: Support for various educational document formats
- **Smart Notifications**: Daily educational updates and reminders

## New Features
- Enhanced UI with Arabic language support
- Firebase integration for authentication
- Localization support for multiple languages

## Technical Architecture
The application follows a modern, multi-platform architecture:
- **Frontend**: Flutter for mobile, responsive web interface
- **Backend**: Python and Rust for core services
- **AI Integration**: Multiple model support with seamless switching
- **Authentication**: Secure Google Sign-In
- **Data Storage**: Firebase and custom database solutions

## Development Setup

### Prerequisites
- Flutter SDK
- Android Studio / Xcode
- Node.js
- Python 3.8+
- Rust toolchain
- Firebase CLI

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/perfectal-education/perfectal-app.git
   cd perfectal-education
   ```

2. Install dependencies:
   ```
   # Flutter dependencies
   cd mobile/flutter
   flutter pub get
   
   # Python dependencies
   cd ../../python
   pip install -r requirements.txt
   
   # Rust dependencies
   cd ../rust
   cargo build
   ```

3. Configure Firebase:
   ```
   cd ../backend/firebase
   firebase init
   ```

4. Run the development server:
   ```
   cd ../../scripts
   ./setup_development.sh
   ```

## Project Structure
- `mobile/`: Mobile application code (Android, iOS, Flutter)
- `web/`: Web application frontend
- `backend/`: Backend services and API
- `python/`: Python-based AI and service modules
- `rust/`: High-performance Rust components
- `design/`: Design assets and UI mockups
- `localization/`: Language files
- `docs/`: Documentation
- `scripts/`: Utility scripts
- `web/components/sidebar.html`: Sidebar for web interface
- `web/components/notification_panel.html`: Notification panel

## Localization
The application supports multiple languages with special font considerations:
- Arabic: Naskh font
- Tamazight: Tifinagh font
- Other languages: Standard fonts

## Contributing
Please read our [contribution guidelines](docs/developer_guide/contribution.md) before submitting pull requests.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For more information, please contact support@perfectaleducation.dz

---

© 2025 Perfectal Education. All rights reserved.
# perfectal_education
