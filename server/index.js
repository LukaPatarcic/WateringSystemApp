require('dotenv').config()
const express = require('express')
const db = require('./db')
const app = express()
const port = 3000
const fcm = require('./token')
app.use(express.json())

app.get('/', (req, res) => {
    res.send('Hello World!')
})

app.post('/saveWaterLevel', (req, res) => {
    const waterLevel = req.body.waterLevel;
    if(!waterLevel) {
        res.status(400);
        res.send('Bad Request');
        return;
    }
    db.saveWaterLevel(waterLevel);
    res.send('OK')
})

app.get('/getWaterLevel', (req, res) => {
    const waterLevel = db.getWaterLevel();
    res.send(waterLevel?.toString());
})

app.post('/sendMessage', (req, res) => {
    const notification = req.body.notification;
    if(!notification) {
        res.status(400);
        res.send('Bad Request');
        return;
    }
    fcm.sendMessage(notification);
    res.send('OK')
})

app.post('/saveToken',(req, res) => {
    const token = req.body.token;
    console.log(token)
    if(!token) {
        res.status(400);
        res.send('Bad Request');
        return;
    }
    db.saveToken(token);
    res.send('OK')
})

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})