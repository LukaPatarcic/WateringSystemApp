require('dotenv').config()
const express = require('express')
const app = express()
const port = 3000
const fcm = require('./token')
app.use(express.json())

app.get('/', (req, res) => {
    res.send('Hello World!')
})

app.get('/sendMessage', (req, res) => {
    fcm.sendMessage();
    res.send('OK')
})

app.post('/savePushNotificationToken',(req, res) => {
    const token = req.body.token;
    console.log(token);
    res.send('OK')
})

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})