// allow user to click send email
document.getElementById('send').addEventListener('click', () => {
    let Email = document.getElementById('email').value

    const nodemailer = require('nodemailer');

    
    var transporter = createTransport({
        service: 'gmail',

        auth: {
            user: 'P2PToolLending@gmail.com',
            pass: `pass = ${pass}`
        }
    })

    var mailOptions = {
        from: 'P2PToolLending@gmail.com',
        to: document.getElementById('email').value,
        subject: document.getElementById('subject').value,
        text: document.getElementById('textarea1').value
    };

    transporter.sendMail(mailOptions, function (error, info) {
        if (error) {
            console.log(error);
        } else {
            console.log('Email sent: ' + info.response);
        }
    });
})


