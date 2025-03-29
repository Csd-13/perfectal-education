import 'package:flutter/material.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(AppLocalizations.of(context)!.app_name),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(AppLocalizations.of(context)!.welcome_message),
            ElevatedButton(
              onPressed: () {
                // Add AI model switching logic here
              },
              child: Text(AppLocalizations.of(context)!.switch_ai_model),
            ),
          ],
        ),
      ),
    );
  }
}