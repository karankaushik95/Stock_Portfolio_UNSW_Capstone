// async function fetchHtmlAsText(url) {
//     console.log("async triggered");
//     return await (await fetch(url)).text();
// }

// function loadhome() {
//     document.getElementById("profile").addEventListener("click", async function (event) {
//         event.preventDefault();
//         document.getElementById("dashboard_heading").innerHTML = await fetchHtmlAsText("../index.html");
//     });
// }

// loadhome();