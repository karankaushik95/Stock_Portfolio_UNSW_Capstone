const apiUrl = "http://127.0.0.1:5000"

const about = document.getElementById("About");
const services = document.getElementById("Services");
const home = document.getElementById("Home");
const aboutScroll = document.getElementById("about-scroll").getBoundingClientRect();
const servicesScroll = document.getElementById("services-scroll").getBoundingClientRect();
const bigServices = document.getElementById("bigServices")
const forgotPassword = document.getElementById("forgot_password");

const register_big_button = document.getElementById("register_big_button");

register_big_button.style.color = "white";

//Just two functions for the background of the buttons to change on hover

register_big_button.addEventListener("mouseleave", function (event) {
    event.target.style.color = "white";
});

register_big_button.addEventListener("mouseenter", function (event) {
    event.target.style.color = "#0079D3";
});

// Following 4 functions describe what happens when the buttons at the top at the menu are clicked
about.addEventListener("click", () => {


    window.scrollTo({
        top: aboutScroll.top - 100,
        left: aboutScroll.left - 100,
        behavior: 'smooth'
    });
    about.className = "nav-item active";
    services.className = "nav-item";
    home.className = "nav-item";
});


services.addEventListener("click", () => {

    window.scrollTo({
        top: servicesScroll.top - 75,
        left: servicesScroll.left - 75,
        behavior: 'smooth'
    });
    about.className = "nav-item";
    services.className = "nav-item active";
    home.className = "nav-item";
});

bigServices.addEventListener("click", () => {

    window.scrollTo({
        top: servicesScroll.top - 75,
        left: servicesScroll.left - 75,
        behavior: 'smooth'
    });
    about.className = "nav-item";
    services.className = "nav-item active";
    home.className = "nav-item";
});


home.addEventListener("click", () => {
    window.scrollTo({
        top: 0,
        left: 0,
        behavior: 'smooth'
    });
    about.className = "nav-item";
    services.className = "nav-item";
    home.className = "nav-item active";
});

// A scroll listener on the document to change the active item of the menu at the top of the page

document.addEventListener("scroll", function (event) {
    if (document.documentElement.scrollTop < aboutScroll.top - 100) {
        about.className = "nav-item";
        services.className = "nav-item";
        home.className = "nav-item active";
    } else if (document.documentElement.scrollTop < servicesScroll.top - 100) {
        about.className = "nav-item active";
        services.className = "nav-item";
        home.className = "nav-item";
    } else {
        about.className = "nav-item";
        services.className = "nav-item active";
        home.className = "nav-item";
    }
});


//Just a function that serves as a hyperlink reference upon button click

document.getElementById("loginButton").addEventListener("click", function (event) {

    event.preventDefault();
    window.location.href = "/login.html";

});

//Just a function that serves as a hyperlink reference upon button click
document.getElementById("registerButton").addEventListener("click", function (event) {
    
    event.preventDefault();
    window.location.href = "/register.html";

});