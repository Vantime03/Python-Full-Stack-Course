// allow user to click send email

function send_mail(){
    const nodemailer = require('nodemailer');

    var transporter = createTransport({
        service: 'gmail',
        auth: {
            user: 'P2PToolLending@gmail.com',
            pass: 'Z6srur92XUYHckA'
        }
    })

    var mailOptions = {
        from: 'P2PToolLending@gmail.com',
        to: 'van.b.luong@hotmail.com',
        subject: 'test email',
        text: 'this is a test'
    }

    transporter.sendMail(mailOptions, function (error, info) {
        if (error) {
            console.log(error);
        } else {
            console.log('Email sent: ' + info.response);
        }
    })
}

send_mail()
