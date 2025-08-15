const express = require('express');
const bodyParser = require('body-parser');
const twilio = require('twilio');

const app = express();
const port = 3000;

// Twilio credentials
const accountSid = 'your_account_sid';
const authToken = 'your_auth_token';
const client = twilio(accountSid, authToken);

app.use(bodyParser.urlencoded({ extended: true }));

app.post('/send-sms', (req, res) => {
    const { phone, message } = req.body;

    client.messages
        .create({
            body: message,
            from: 'your_twilio_phone_number',
            to: phone
        })
        .then(() => res.send('SMS sent successfully!'))
        .catch(err => res.status(500).send(`Failed to send SMS: ${err.message}`));
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
