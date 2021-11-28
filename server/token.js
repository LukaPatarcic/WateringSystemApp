
const serverKey = process.env.FCM_TOKEN;
const FCM = require('fcm-node');
const db = require('./db');
const fcm = new FCM(serverKey);

const sendMessage = (notification) => {
    const tokens = db.getTokens();
    const message = {
        registration_ids: tokens,
        notification,
    };
    fcm.send(message, function(err, response){
        if (err) {
            console.log("Something has gone wrong!", err);
        } else {
            console.log("Successfully sent with response: ", response);
        }
    });
}


module.exports = { sendMessage }