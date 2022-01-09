import 'package:app/services/http_service.dart';
import 'package:app/services/push_notification_service.dart';
import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';

import 'models/album.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  await PushNotificationService().setupInteractedMessage();
  await PushNotificationService().getToken();
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Pet Watering System',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Pet Watering System'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);
  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  late Future<String> futureWaterLevel;
  @override
  void initState() {
    super.initState();
    futureWaterLevel = fetchWaterLevel();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Container(
        height: double.infinity,
        child: Padding(
          padding: EdgeInsets.all(20),
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.center,
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              // Column(children: [Text("ASDAS")],),
              Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text(
                    "CURRENT WATER LEVEL",
                    style: TextStyle(fontSize: 24),
                  ),
                  SizedBox(height: 20),
                  FutureBuilder<String>(
                    future: futureWaterLevel,
                    builder: (context, snapshot) {
                      if (snapshot.hasData) {
                        return Text((snapshot.data as String) + "%",
                          style: TextStyle(fontSize: 36, fontWeight: FontWeight.bold),);
                      } else if (snapshot.hasError) {
                        return Text('${snapshot.error}');
                      }
                      // By default, show a loading spinner.
                      return const CircularProgressIndicator();
                    },
                  ),
                  SizedBox(height: 20),
                  ElevatedButton(
                      onPressed: () async {
                        var data = await fetchWaterLevel();
                        setState(() {
                          futureWaterLevel = Future.value(data);
                        });
                      },
                      child: Text("Refresh"))
                ],
              )
            ],
          ),
        ),
      ),
    );
  }
}
