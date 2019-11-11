const apiUrl = "http://127.0.0.1:5000"

const username = document.getElementById("username");
const usernameSpan = document.getElementById("username_error");

const password = document.getElementById("password");
const passwordSpan = document.getElementById("password_error");
passwordSpan.style.color = "red";
usernameSpan.style.color = "red";

document.getElementById("login").addEventListener('click', function (event) {

    event.preventDefault();
    if (!password.value.trim()) {
        passwordSpan.innerText = "Please enter your password";
        password.focus();
        password.style.borderColor = "red";
    } else {
        password.style.borderColor = "";
        passwordSpan.innerText = "";
    }
    if (!username.value.trim()) {
        username.style.borderColor = "red";
        username.focus();
        usernameSpan.innerText = "Please enter a username";
    } else {
        usernameSpan.innerText = "";
        username.style.borderColor = "";
    }
    if (username.value.trim() && password.value.trim()) {
        let formData = new FormData();
        formData.append("username", username.value);
        formData.append("password", password.value);
        fetch(apiUrl + "/login.html", {
            method: 'POST',
            redirect: "follow",
            body: formData
        }).then(response => {
            if (response.redirected)
                window.location.href = response.url;
            else {
                username.style.borderColor = "red";
                username.focus();
                password.focus();
                password.style.borderColor = "red";
                passwordSpan.innerText = "Please check your credentials and try again";
            }
        });
    }

});