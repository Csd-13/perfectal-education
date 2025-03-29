import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'screens/home_screen.dart';

void main() {
  runApp(const PerfectalEducationApp());
}

class PerfectalEducationApp extends StatelessWidget {
  const PerfectalEducationApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Perfectal Education',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        fontFamily: 'Naskh',
      ),
      localizationsDelegates: const [
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
        GlobalCupertinoLocalizations.delegate,
      ],
      supportedLocales: const [
        Locale('ar'),
        Locale('en'),
        Locale('fr'),
      ],
      locale: const Locale('ar'),
      home: const HomeScreen(),
    );
  }
}