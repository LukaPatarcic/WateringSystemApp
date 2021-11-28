
const serverKey = process.env.FCM_TOKEN; // Your gcm key in quotes
const token = process.env.DEFAULT_TOKEN; // Receiver device token
const FCM = require('fcm-node');
const fcm = new FCM(serverKey);

const message = { //this may vary according to the message type (single recipient, multicast, topic, et cetera)
    to: token,
    collapse_key: 'your_collapse_key',

    notification: {
        title: 'Title of your push notification',
        body: 'Body of your push notification'
    },

    data: {  //you can send only notification or only data(or include both)
        my_key: 'my value',
        my_another_key: 'my another value'
    }
};

const sendMessage = () => {
    fcm.send(message, function(err, response){
        if (err) {
            console.log("Something has gone wrong!");
        } else {
            console.log("Successfully sent with response: ", response);
        }
    });
}

const saveToken = async (token) => {
}


module.exports = { sendMessage }