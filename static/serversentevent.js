var source = new EventSource('/tweets');
source.onmessage = function (event) {
    var tweetDivContainer = document.getElementById('tweet-container');
    tweetDivContainer.innerHTML = event.data;
}