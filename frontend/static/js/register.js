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

document.getElementById("login").addEventListener('click', function (event) {

    event.preventDefault();
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