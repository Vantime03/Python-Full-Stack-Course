// allow user to click send email


function send_mail(){
    const nodemailer = require('nodemailer');

    var transporter = nodemailer.createTransport({
        service: 'hotmail',
        auth: {
            user: 'van.b.luong@hotmail.com',
            pass: ``
        }
    })

    var mailOptions = {
        from: 'van.b.luong@hotmail.com',
        to: 'p2ptoollending@gmail.com',
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
