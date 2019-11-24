const apiUrl = "http://127.0.0.1:5000"

function portfolioListener() {

    document.getElementById("Portfolios").addEventListener("click", function (event) {

        event.preventDefault();
        populatePortfolios();
    });
}

// Populates all the users portfolios when the portfolio button on the dashboard is clicked
function populatePortfolios() {
    const clearUI = document.getElementById("dashboard_heading");
    // Clears the UI and puts a loader in to wait for the elements to load
    while (clearUI.firstChild) {
        clearUI.removeChild(clearUI.firstChild);
    }
    const loaderDiv = document.createElement("div");
    loaderDiv.setAttribute("id", "loader");
    clearUI.appendChild(loaderDiv);
    fetch(apiUrl + "/user_portfolios", {
        method: 'GET',
    }).then(resp => resp.json()).then(function (response) {
        console.log(response);
        //Remove the loader div and load the data
        loaderDiv.parentElement.removeChild(loaderDiv);

        const div1 = document.createElement("div");
        div1.setAttribute("class", "row")

        const div2 = document.createElement("div");
        div2.setAttribute("class", "col-12 py-5");

        const heading = document.createElement("h4");
        heading.innerText = "Portfolio Management";
        heading.setAttribute("class", "animate-bottom");

        const div3 = document.createElement("div");
        div3.setAttribute("class", "item-wrapper");

        const div4 = document.createElement("div");
        div4.setAttribute("class", "table-responsive");
        div4.setAttribute("class", "animate-bottom");

        const table = document.createElement("table");
        table.setAttribute("class", "table info-table table-striped");

        const thead = document.createElement("thead");

        const tr1 = document.createElement("tr");

        const th1 = document.createElement("th");
        th1.innerText = "Name";

        const th2 = document.createElement("th");

        const tbody = document.createElement("tbody");

        div1.appendChild(div2);
        div2.appendChild(heading);

        div3.appendChild(div4);
        div4.appendChild(table);

        table.appendChild(thead);
        thead.appendChild(tr1);

        tr1.appendChild(th1);
        tr1.appendChild(th2);

        table.appendChild(tbody);

        clearUI.appendChild(div1);
        clearUI.appendChild(div3);

        const tr = document.createElement("tr");
        const td1 = document.createElement("td");
        td1.style.cursor = "pointer";

        const td2 = document.createElement("td");
        td2.style.cursor = "pointer";

        tr.addEventListener("mouseenter", () => {
            tr.style.backgroundColor = "#e6e6e6";
            tr.style.backgroundColor = "#e6e6e6";
        });
        tr.addEventListener("mouseleave", () => {
            tr.style.backgroundColor = "";
            tr.style.backgroundColor = "";
        });

        tr.setAttribute("data-toggle", "modal");
        tr.setAttribute("data-target", "#portfolioModal");
        // Actions when the create portfolio button is clicked
        document.getElementById("createPortfolio").addEventListener("click", function (event) {
            event.preventDefault();
            const portfolioName = document.getElementById("portfolioName");
            const portfolioError = document.getElementById("portfolio_error");

            if (!portfolioName.value.trim()) {
                portfolioError.innerText = "Please enter a name for your portfolio";
                portfolioName.focus();
                portfolioName.style.borderColor = "red";
                return;
            } else {
                if (response && response[portfolioName.value]) {
                    portfolioError.innerText = "Portfolio with this name already exists";
                    portfolioName.focus();
                    portfolioName.style.borderColor = "red";
                    return;
                }
                else{
                    portfolioError.innerText = "";
                    portfolioName.style.borderColor = "";
                    let formdata = new FormData();
                    formdata.append("portfolio_name", portfolioName.value);
                    fetch(apiUrl+"/create_portfolio.html", {
                        method: "POST",
                        body: formdata
                    }).then(response=>{
                        $('#portfolioModal').modal('hide');
                        $('.modal-backdrop').hide();
                        populatePortfolios();
                    });
                }
            }
        });

        td1.innerText = "Create New";

        tr.appendChild(td1);
        tr.appendChild(td2);
        tbody.appendChild(tr);



        
        for (var item in response) {
            const tr = document.createElement("tr");

            const td1 = document.createElement("td");
            td1.style.cursor = "pointer";

            const td2 = document.createElement("td");

            const buttonDiv = document.createElement("div");
            buttonDiv.setAttribute("class", "dropdown");

            const button = document.createElement("button");
            button.setAttribute("class", "btn btn-danger btn-rounded dropbtn");
            button.setAttribute("data-toggle", "tooltip");
            button.setAttribute("title", "Delete portfolio");
            button.setAttribute("data-animation", "true");
            button.setAttribute("data-placement", "auto");

            button.innerText = "-";

            button.addEventListener("click", () => {
                fetch(apiUrl + "/delete_portfolio/" + item, {
                    method: "GET"
                }).then(response => populatePortfolios());
            });

            buttonDiv.appendChild(button);


            td2.appendChild(buttonDiv);

            td1.innerText = item;

            tr.appendChild(td1);
            tr.appendChild(td2);

            tr.addEventListener("mouseenter", () => {
                tr.style.backgroundColor = "#e6e6e6";
                tr.style.backgroundColor = "#e6e6e6";
            });
            tr.addEventListener("mouseleave", () => {
                tr.style.backgroundColor = "";
                tr.style.backgroundColor = "";
            });

            tr.setAttribute("id", item);

            td1.addEventListener("click", function (event) {
                const children = tr.childNodes;
                const stockID = children[0].textContent || children[0].innerText || "";
                console.log(stockID);
                while (clearUI.firstChild) {
                    clearUI.removeChild(clearUI.firstChild);
                }


                const div1 = document.createElement("div");
                div1.setAttribute("class", "row")

                const div2 = document.createElement("div");
                div2.setAttribute("class", "col-12 py-5");

                const heading = document.createElement("h4");
                heading.innerText = stockID;
                heading.setAttribute("class", "animate-bottom");

                const div3 = document.createElement("div");
                div3.setAttribute("class", "item-wrapper");

                const div4 = document.createElement("div");
                div4.setAttribute("class", "table-responsive");
                div4.setAttribute("class", "animate-bottom");

                const table = document.createElement("table");
                table.setAttribute("class", "table info-table table-striped");

                const thead = document.createElement("thead");

                const tr1 = document.createElement("tr");

                const th1 = document.createElement("th");
                th1.innerText = "Name";

                const th2 = document.createElement("th");
                th2.innerText = "Quantity";

                const th3 = document.createElement("th");
                th3.innerText = "Unit Price";

                const th4 = document.createElement("th");
                th4.innerText = "Total Price";

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

                var total_stock = 0;
                var total_price = 0;
                for (var stock in response[stockID]) {
                    //console.log(response[item][stock]);
                    const tr = document.createElement("tr");

                    const td1 = document.createElement("td");
                    td1.innerText = response[stockID][stock]["ticker"];

                    const td2 = document.createElement("td");
                    td2.innerText = response[stockID][stock]["amount"];

                    total_stock += Number(response[stockID][stock]["amount"]);

                    const td3 = document.createElement("td");
                    td3.innerText = response[stockID][stock]["price"];

                    const td4 = document.createElement("td");
                    td4.innerText = Number(response[stockID][stock]["amount"]) * Number(response[stockID][stock]["price"]);
                    total_price+=Number(response[stockID][stock]["amount"]) * Number(response[stockID][stock]["price"]);

                    const td5 = document.createElement("td");

                    const buttonDiv = document.createElement("div");
                    buttonDiv.setAttribute("class", "dropdown");

                    const button = document.createElement("button");
                    
                    button.setAttribute("class", "btn btn-danger btn-rounded dropbtn");
                    button.setAttribute("data-toggle", "tooltip");
                    button.setAttribute("title", "Delete stock");
                    button.setAttribute("data-animation", "true");
                    button.setAttribute("data-placement", "auto");

                    button.innerText = "-";

                    button.addEventListener("click", () => {
                        console.log(response[stockID][stock]["ticker"] + "/" + stockID);
                        fetch(apiUrl + "/remove_portfolio_stock/" + response[stockID][stock]["ticker"] + "/" + stockID, {
                                method: "GET"
                            }).then(resp => resp.json())
                            .then(function (response) {
                                button.parentElement.parentElement.parentElement.parentElement.removeChild(button.parentElement.parentElement.parentElement);
                                // document.getElementById("Portfolios").click();
                                
                                // document.getElementById(item).click();
                            })
                    });

                    buttonDiv.appendChild(button);


                    td5.appendChild(buttonDiv);


                    tr.appendChild(td1);
                    tr.appendChild(td2);
                    tr.appendChild(td3);
                    tr.appendChild(td4);
                    tr.appendChild(td5);

                    tbody.appendChild(tr);
                }
            });

            
            tbody.appendChild(tr);
        }
    });
}


portfolioListener();