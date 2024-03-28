var emotion = document.getElementById("emotionText").innerText.trim().toLowerCase();
function setPlaylist(emotion) {
    var playlistFrame = document.getElementById("playlistFrame");

    // Remove existing iframes if any
    playlistFrame.innerHTML = '';

    // Create a new iframe element
    var iframe = document.createElement('iframe');
    
    iframe.width = "750px";
    iframe.height = "450px";
    iframe.frameborder = "0";
    iframe.allowtransparency = "true";
    iframe.allow = "encrypted-media";

    // Update the iframe src based on the emotion
    switch (emotion) {
        case "happy":
            iframe.src = "https://open.spotify.com/embed/playlist/7rGWH3tMJCIhyzde9s5MmF?utm_source=generator";
            break;
        case "sad":
            iframe.src = "https://open.spotify.com/embed/playlist/1HRECRGJpEU3HKs2iaPwIA?utm_source=generator";
            break;
        case "anxious":
            iframe.src = "https://open.spotify.com/embed/playlist/3CDqrZDcgn0phmqpcGaWyZ?utm_source=generator";
            break;
        default:
            // Default playlist link or error handling
            break;
    }

    // Append the iframe to the playlistFrame element
    playlistFrame.appendChild(iframe);
}

// Call setPlaylist function with the initial emotion
setPlaylist(emotion);