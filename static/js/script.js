var twitchurl = 'https://api.twitch.tv/kraken/streams/?';
var request = new XMLHttpRequest();
var client_Id = 'osidhfosjfeifjsoifjenpfi'; //developer id
var game = "League%20of%20Legends"; //game type
var limit = 20; //max object

request.open('GET', twitchurl + 'game=' + game + '&client_Id=' + client_Id + '&limit=' + limit);
request.responseType = 'json';
request.send();
request.onload = function () {
    var livestream = JSON.parse(this.response);
    if (request.status >= 200 && request.status < 400) {
        const app = document.getElementsByClassName('preview');
    }
    else {
        console.log('error');
    }
}
