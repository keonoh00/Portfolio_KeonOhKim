const body = document.querySelector("body");

const IMG_NUMBER = 4;

function handleImageLoad() {
    console.log("Finished Image Loading");
}

function paintImage(imgNumber) {
    const image = new Image();
    image.src = `images/${imgNumber + 1}.jpg`
    image.classList.add("bgImage");
    body.prepend(image);
    // if image was loading from api then loadend applies but it is remote so not working
    // image.addEventListener("loadend", handleImageLoad)
}

function genRandNum() {
    const number = Math.floor(Math.random() * IMG_NUMBER);
    return number
}

function init() {
    const randomNumber = genRandNum();
    paintImage(randomNumber)
}


init();