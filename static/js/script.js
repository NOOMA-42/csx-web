var twitchurl = 'https://api.twitch.tv/kraken/streams/?';
var request = new XMLHttpRequest();
var game = "League%20of%20Legends"; //game type
var limit = 10; //max object
var Headers = new Headers()
var client_Id = '5bx3vtnirhxbuqth8aedbgtwp2joyt';
var preview, logoavatar;

request.open('GET', twitchurl + 'game=' + game + '&limit=' + limit + '&client_id=' + client_Id, true);
request.responseType = 'json';
request.onload = function () {
    var livestream = this.response.streams;
    if (request.status >= 200 && request.status < 400) {
        for (var i = 0; i<livestream.length; i++) {
            preview = document.querySelectorAll('div.preview img')[i];
            logoavatar = document.querySelectorAll('div.avatar img')[i];
            preview.src = livestream[i].preview.medium;
            logoavatar.src = livestream[i].channel.logo;
            channelname = document.querySelectorAll('div.channel')[i];
            channelname = livestream[i].channel.display_name;
            ownername = document.querySelectorAll('div.ownername')[i];
            ownername = livestream[i].channel.display_name;
        };
    }
    else {
        console.log('error');
    }
}
request.send();
