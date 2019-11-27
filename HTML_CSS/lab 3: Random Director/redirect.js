function random_choice (len) {
    return Math.floor(Math.random() * Math.floor(len)); 
}

let direct_to_social_media = () => {
    let site = [
        "https://www.facebook.com/",
        "https://twitter.com/",
        "https://www.instagram.com/?hl=en",
        "https://www.whatsapp.com/",
        "https://www.tumblr.com/"
    ]
    let n = random_choice(site.length)
    location.assign(site[n])
}

let direct_to_news = () => {
    let site = [
        'https://www.msn.com/',
        'https://www.yahoo.com/',
        'https://news.google.com/?hl=en-US&gl=US&ceid=US:en',
        'https://www.usatoday.com/',
        'https://www.cnn.com/'
    ]
    let n = random_choice(site.length)
    
    location.assign(site[n])
}


document.querySelector(".news_div").addEventListener('click', () => {
    setTimeout(direct_to_news, 5000); 
})

document.querySelector(".social_media_div").addEventListener("click", () => {
    direct_to_social_media();
})


