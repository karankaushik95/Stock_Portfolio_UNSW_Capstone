const about = document.getElementById("About");
const services = document.getElementById("Services");
const home = document.getElementById("Home");
const aboutScroll = document.getElementById("about-scroll").getBoundingClientRect();
const servicesScroll = document.getElementById("services-scroll").getBoundingClientRect();

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
})