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


register_big_button.addEventListener("mouseleave", function (event) {
    event.target.style.color = "white";
});

register_big_button.addEventListener("mouseenter", function (event) {
    event.target.style.color = "#0079D3";
});

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


forgotPassword.addEventListener("click", () => {
    document.getElementsByClassName("modal-backdrop fade show")[0].remove(); // Remove the backdrop that wasn't being removed with just the below line
    $("#modalRequest").toggle();
});

document.getElementById("loginButton").addEventListener("click", function (event) {

    event.preventDefault();

});

document.getElementById("forgotPassSubmit").addEventListener("click", function (event) {

    event.preventDefault();
    const forgotPasswordText = document.getElementById("forgotpwdemail");
    const forgotPasswordSpan = document.getElementById("forgot_pwd_email_error");
    forgotPasswordSpan.style.color = "red";
    if (!forgotPasswordText.value.trim()) {
        forgotPasswordSpan.innerText = "Email cannot be empty";
        forgotPasswordText.focus();
        forgotPasswordText.style.borderColor = "red";
        return;
    } else {
        if (forgotPasswordText.value.match(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/)) {
            forgotPasswordSpan.innerText = "";
            forgotPasswordText.style.borderColor = "";
        } else {
            forgotPasswordSpan.innerText = "Please enter a valid email";
            forgotPasswordText.focus();
            forgotPasswordText.style.borderColor = "red";
        }
    }
});

document.getElementById("loginButton").addEventListener("click", function (event) {

    event.preventDefault();
    window.location.href = "/login.html";

    // const username = document.getElementById("username");
    // // const usernameSpan = document.getElementById("username_error");

    // const password = document.getElementById("password");
    // // const passwordSpan = document.getElementById("password_error");
    // // passwordSpan.style.color = "red";
    // // usernameSpan.style.color = "red";

    
    // let formData = new FormData();
    //     formData.append("username", username.value);
    //     formData.append("password", password.value);
        
    //     fetch(apiUrl+"/login", {
    //         method: 'POST',
    //         body: formData
    //     }).then(resp => resp.json()).then(function (response) {
    //         console.log(response);
    //         if(response["success"] === "true"){
    //             sessionStorage.setItem("username", username.value);
    //             window.location.href = "/dashboard.html";
    //         }
    //     });
    
    // if (!password.value.trim()) {
    //     passwordSpan.innerText = "Please enter your password";
    //     password.focus();
    //     password.style.borderColor = "red";
    // } else {
    //     password.style.borderColor = "";
    //     passwordSpan.innerText = "";
    // }
    // if (!username.value.trim()) {
    //     username.style.borderColor = "red";
    //     username.focus();
    //     usernameSpan.innerText = "Please enter a username";
    // } else {
    //     usernameSpan.innerText = "";
    //     username.style.borderColor = "";
    // }
    // if (username.value && password.value) {
    //     //call API
        
    //     //alert("Valid");
    // }
});

document.getElementById("registerButton").addEventListener("click", function (event) {
    event.preventDefault();
    const fullName = document.getElementById("registerName");
    const fullNameError = document.getElementById("register_name_error");

    const username = document.getElementById("registerUsername");
    const usernameError = document.getElementById("register_username_error");

    const password = document.getElementById("registerPassword");
    const passwordError = document.getElementById("register_password_error");

    if (!password.value.trim()) {
        passwordError.innerText = "Please enter a password";
        password.focus();
        password.style.borderColor = "red";
    } else {
        password.style.borderColor = "";
        passwordError.innerText = "";
    }
    if (!username.value.trim()) {
        username.style.borderColor = "red";
        username.focus();
        usernameError.innerText = "Please enter a username";
    } else {
        if (!username.value.match(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/)) {
            username.style.borderColor = "red";
            username.focus();
            usernameError.innerText = "Please enter a valid email address";
            return;
        } else {
            usernameError.innerText = "";
            username.style.borderColor = "";
        }
    }
    if (!fullName.value.trim()) {
        fullName.style.borderColor = "red";
        fullName.focus();
        fullNameError.innerText = "Please enter your name";
    } else {
        fullNameError.innerText = "";
        fullName.style.borderColor = "";
    }

    if (username.value && fullName.value && password.value) {
        alert("valid");
        // call register api
    }

});