const functions = require('firebase-functions');

exports.sendNotification = functions.https.onRequest((req, res) => {
    const notification = req.body.notification;
    if (!notification) {
        return res.status(400).send('Notification content is required.');
    }
    console.log('Notification sent:', notification);
    res.status(200).send('Notification sent successfully.');
});
