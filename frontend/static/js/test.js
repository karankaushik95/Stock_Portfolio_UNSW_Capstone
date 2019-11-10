const username = document.getElementById("username");
// const usernameSpan = document.getElementById("username_error");

const password = document.getElementById("password");
// const passwordSpan = document.getElementById("password_error");
// passwordSpan.style.color = "red";
// usernameSpan.style.color = "red";

document.getElementById("login").addEventListener('click', () => {

    let formData = new FormData();
    formData.append("username", username.value);
    formData.append("password", password.value);

    fetch(apiUrl + "/login", {
        method: 'POST',
        body: formData
    }).then(resp => resp.json()).then(function (response) {
        console.log(response);
        if (response["success"] === "true") {
            sessionStorage.setItem("username", username.value);
            window.location.href = "/dashboard.html";
        }
    });
});