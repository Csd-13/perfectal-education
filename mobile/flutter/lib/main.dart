import 'package:flutter/material.dart';
import 'screens/home_screen.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Perfectal Education',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: HomeScreen(),
    );
  }
}
import 'package:firebase_core/firebase_core.dart';
import 'package:perfectal_education/screens/home_screen.dart';
import 'package:perfectal_education/screens/auth_screen.dart';
import 'package:perfectal_education/services/auth_service.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(PerfectalEducationApp());
}

class PerfectalEducationApp extends StatelessWidget {
  final AuthService _authService = AuthService();

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Perfectal Education',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        fontFamily: 'Naskh', // Arabic font
        textTheme: TextTheme(
          bodyLarge: TextStyle(
            locale: Locale('ar'), // Primary Arabic locale
          ),
        ),
      ),
      home: StreamBuilder(
        stream: _authService.authStateChanges,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.active) {
            return snapshot.hasData ? HomeScreen() : AuthScreen();
          }
          return CircularProgressIndicator();
        },
      ),
      // Localization and route configuration
      localizationsDelegates: [
        // Add localization delegates
      ],
      supportedLocales: [
        Locale('ar', 'DZ'), // Arabic (Algeria)
        Locale('fr', 'DZ'), // French
        Locale('en', 'US'), // English
        Locale('it', 'IT'), // Italian
        Locale('de', 'DE'), // German
        Locale('ber'), // Tamazight
      ],
    );
  }
}