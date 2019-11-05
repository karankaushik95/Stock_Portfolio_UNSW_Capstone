const apiUrl = "http://127.0.0.1:5000"

// if (!sessionStorage.get("username")){
//     window.location.href = "/index.html";
// }



function logout() {
    document.getElementById("Logout").addEventListener("click", function (event) {
        sessionStorage.clear();
        window.location.href = "/index.html";
    });
}

function search() {

    const searchButton = document.getElementById("search_button");
    searchButton.addEventListener("click", function (event) {
        event.preventDefault();
        let formData = new FormData();
        const searchTerm = document.getElementById("inlineFormInputGroup").value.trim();
        //console.log(searchTerm);
        if(!searchTerm){
            return;
        }
        formData.append("search", searchTerm);
        fetch(apiUrl + "/search", {
            method: 'POST',
            body: formData
        }).then(resp => resp.json()).then(function (response) {
            //console.log(response);
            const clearUI = document.getElementById("dashboard_heading");
            while(clearUI.firstChild){
                clearUI.removeChild(clearUI.firstChild);
            }
            //clearUI.innerHTML="<div class=\"row\">\n<div class=\"col-12 py-5\"><h4>Search for \"" + searchTerm + "\" yielded the following results:</h4>";
            //clearUI.innerHTML+="<thead>\n<tr>\n<th>Name</th>\n<th>Symbol</th>\n<th>Type</th>\n<th>Market</th>\n<th></th>\n</tr>\n</thead>\n";
            
            const div1 = document.createElement("div");
            div1.setAttribute("class", "row")
            
            const div2 = document.createElement("div");
            div2.setAttribute("class", "col-12 py-5");

            const heading = document.createElement("h4");
            heading.innerText = "Search for \"" + searchTerm + "\" yielded the following results:";

            const div3 = document.createElement("div");
            div3.setAttribute("class", "item-wrapper");

            const div4 = document.createElement("div");
            div4.setAttribute("class", "table-responsive");

            const table = document.createElement("table");
            table.setAttribute("class", "table info-table table-striped");

            const thead = document.createElement("thead");
            
            const tr1 = document.createElement("tr");
            
            const th1 = document.createElement("th");
            th1.innerText = "Name";

            const th2 = document.createElement("th");
            th2.innerText = "Symbol";

            const th3 = document.createElement("th");
            th3.innerText = "Type";

            const th4 = document.createElement("th");
            th4.innerText = "Market";

            const th5 = document.createElement("th");

            const tbody = document.createElement("tbody");
            
            div1.appendChild(div2);
            div2.appendChild(heading);

            div3.appendChild(div4);
            div4.appendChild(table);

            table.appendChild(thead);
            thead.appendChild(tr1);
            
            tr1.appendChild(th1);
            tr1.appendChild(th2);
            tr1.appendChild(th3);
            tr1.appendChild(th4);
            tr1.appendChild(th5);

            table.appendChild(tbody);

            clearUI.appendChild(div1);
            clearUI.appendChild(div3);
            
            
            for (item of response.bestMatches){
                const tr = document.createElement("tr");
                
                const td1 = document.createElement("td");
                td1.style.cursor ="pointer";

                const td2 = document.createElement("td");
                td2.style.cursor ="pointer";

                const td3 = document.createElement("td");
                const td4 = document.createElement("td");
                const td5 = document.createElement("td");

                const buttonDiv = document.createElement("div");
                //buttonDiv.setAttribute("class", "btn btn-success has-icon btn-rounded");

                const button = document.createElement("div");
                button.setAttribute("class", "btn btn-success btn-rounded");
                button.setAttribute("data-toggle", "tooltip");
                button.setAttribute("title", "Add to watchlist");
                button.setAttribute("data-animation", "true");
                button.setAttribute("data-placement", "auto");


                //const button = document.createElement("button");
                //button.setAttribute("class", "mui-btn mui-btn--fab mui-btn--danger");
                button.innerText = "+";

                buttonDiv.appendChild(button);

                td5.appendChild(buttonDiv);

                td2.innerText = item["1. symbol"];
                td1.innerText = item["2. name"];
                td3.innerText = item["3. type"];
                td4.innerText = item["4. region"];
                
                tr.appendChild(td1);
                tr.appendChild(td2);
                tr.appendChild(td3);
                tr.appendChild(td4);
                tr.appendChild(td5);


                td1.addEventListener("mouseenter", function(event){
                    td1.style.backgroundColor = "#e6e6e6";
                    td2.style.backgroundColor = "#e6e6e6";
                });
                td1.addEventListener("mouseleave", function(event){
                    td1.style.backgroundColor = "";
                    td2.style.backgroundColor = "";
                });

                td2.addEventListener("mouseenter", function(event){
                    td1.style.backgroundColor = "#e6e6e6";
                    td2.style.backgroundColor = "#e6e6e6";
                });
                td2.addEventListener("mouseleave", function(event){
                    td1.style.backgroundColor = "";
                    td2.style.backgroundColor = "";
                });

                td1.addEventListener("click", function(event){
                    event.preventDefault();
                    showStockInfo(clearUI, td2.value);
                });
                td2.addEventListener("click", showStockInfo(clearUI, td2.value));

                tbody.appendChild(tr);
            } 
        });
    });
}

function showStockInfo(dashboard, stockCode){
    console.log(stockCode);
}


logout();
search();