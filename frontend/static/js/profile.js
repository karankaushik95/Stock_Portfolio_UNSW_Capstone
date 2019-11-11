window.addEventListener("load", (event)=>{
    document.getElementById("profile-username").innerText = sessionStorage.getItem("email");
    document.getElementById("profile-fullname").innerText = sessionStorage.getItem("name");
    console.log("HERE");
});

window.onload = ()=>{
    document.getElementById("profile-username").innerText = sessionStorage.getItem("email");
    document.getElementById("profile-fullname").innerText = sessionStorage.getItem("name");
    console.log("HERE");
};