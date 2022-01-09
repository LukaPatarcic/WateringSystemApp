import 'dart:convert';

import 'package:app/models/album.dart';
import 'package:http/http.dart' as http;

Future<String> fetchWaterLevel() async {
  final response = await http
      .get(Uri.parse('https://watering-system.spolnici.com/getWaterLevel'));

  if (response.statusCode == 200) {
    // If the server did return a 200 OK response,
    // then parse the JSON.
    return response.body;
  } else {
    // If the server did not return a 200 OK response,
    // then throw an exception.
    throw Exception('Failed to load album');
  }
}

Future sendToken(String? token) async {
  return http.post(
    Uri.parse('https://watering-system.spolnici.com/saveToken'),
    headers: {"Content-Type": "application/json"},
    body: json.encode({'token': token}),
  );
}
