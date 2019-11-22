const apiUrl = "http://127.0.0.1:5000"


const fullName = document.getElementById("fullname");
const fullNameError = document.getElementById("name_error");

const username = document.getElementById("username");
const usernameError = document.getElementById("username_error");

const password = document.getElementById("password");
const passwordError = document.getElementById("password_error");

passwordError.style.color = "red";
usernameError.style.color = "red";
fullNameError.style.color = "red";

// Basic event listener to check for button click
document.getElementById("login").addEventListener('click', function (event) {

    event.preventDefault();
    //Checks if the password field is empty
    if (!password.value.trim()) {
        passwordError.innerText = "Please enter a password";
        password.focus();
        password.style.borderColor = "red";
    } else {
        password.style.borderColor = "";
        passwordError.innerText = "";
    }
    //Checks if the username field is empty
    if (!username.value.trim()) {
        username.style.borderColor = "red";
        username.focus();
        usernameError.innerText = "Please enter a username";
    } else {
        //Checks for valid email which is used as username. Taken from email-regex.com
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
    //Checks if the full name field not empty
    if (!fullName.value.trim()) {
        fullName.style.borderColor = "red";
        fullName.focus();
        fullNameError.innerText = "Please enter your name";
    } else {
        fullNameError.innerText = "";
        fullName.style.borderColor = "";
    }
    //Once the checks are done, the API is called for the user to be reigstered
    if (username.value && fullName.value && password.value) {
        let formData = new FormData();
        formData.append("regemail", username.value);
        formData.append("regpassword", password.value);
        formData.append("regname", fullName.value);

        fetch(apiUrl + "/signup.html", {
            method: 'POST',
            body: formData
        }).then(response => {
            if (response.redirected)
                window.location.href = response.url;
            else {
                username.style.borderColor = "red";
                username.focus();
                usernameError.innerText = "An account with that email already exists";
            }
        });
    }

});