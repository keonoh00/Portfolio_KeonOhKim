const weatherHTML = document.querySelector(".js-weather")
const API_KEY = "34b0bb68fd557ec1ee6a176f22eccc4e";
const LOCAT = "location";

function getWeather(lati, long) {
    // then call the function after getting the fetch response
    fetch(
        `https://api.openweathermap.org/data/2.5/weather?lat=${lati}&lon=${long}&appid=${API_KEY}&units=metric`
    ).then(function(response) {
        return response.json();
    }).then(function(json){
        const cityName = json.name;
        const absTemp = json.main.temp;
        const maxTemp = json.main.temp_max;
        const minTemp = json.main.temp_min;
        const humidity = json.main.humidity;
        const feelTemp = json.main.feels_like;
        weatherHTML.innerText = `${absTemp} @ ${cityName}`
    });
}

function saveLocation(locationObj) {
    localStorage.setItem(location, JSON.stringify(locationObj));
}

function gotLocation(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    const locationObj = {latitude, longitude};
    saveLocation(locationObj);
    getWeather(latitude, longitude);
}

function lostLocation() {
    // If the location is error this is just sample coordinate to generate weather but does not save location
    console.log("Location Error!");
    const longitude = 127.0276;
    const latitude = 37.4980;
    const locationObj = {latitude, longitude};
    getWeather(latitude, longitude);
}

function askForLocation() {
    // this is an api to get current position
    navigator.geolocation.getCurrentPosition(gotLocation, lostLocation);
}

function loadLocation() {
    const loadedLocation = localStorage.getItem(LOCAT);
    if (loadedLocation === null) {
        askForLocation(); 
    } else {
        const location = JSON.parse(loadedLocation);
        getWeather(location.lati, location.long);
    }
}

function init() {
    loadLocation();
}

init();