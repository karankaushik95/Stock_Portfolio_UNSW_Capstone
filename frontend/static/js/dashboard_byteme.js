document.getElementById("Logout").addEventListener("click", function(event){
    sessionStorage.clear();
    console.log("Did things");
    window.location.href = "/index.html";
});