
// This function just sets up the initial values of the username and full name of the user on the dashboard below the image
function getUserData(){
    fetch("http://127.0.0.1:5000/user_data", {
        method: 'GET'
    }).then(resp=>resp.json()).then(function(response){
        document.getElementById("user-name").innerText = response["name"];
        document.getElementById("user-email").innerText = response["email"];

        sessionStorage.setItem("name",response["name"]);
        sessionStorage.setItem("username",response["email"]);
    });
}

getUserData();