const apiUrl = "http://127.0.0.1:5000";

import {initChart, drawChart} from './dashboard_byteme.js';

function watchlist() {

    const clearUI = document.getElementById("dashboard_heading");
    while (clearUI.firstChild) {
        clearUI.removeChild(clearUI.firstChild);
    }
    const loaderDiv = document.createElement("div");
    loaderDiv.setAttribute("id", "loader");
    clearUI.appendChild(loaderDiv);
    fetch(apiUrl + "/user_watchlist", {
        method: 'GET',
    }).then(resp => resp.json()).then(function (response) {

        loaderDiv.parentElement.removeChild(loaderDiv);

        const div1 = document.createElement("div");
        div1.setAttribute("class", "row")

        const div2 = document.createElement("div");
        div2.setAttribute("class", "col-12 py-5");

        // const heading = document.createElement("h4");
        // heading.innerText = "Search for \"" + searchTerm + "\" yielded the following results:";
        // heading.setAttribute("class", "animate-bottom");

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
        th1.innerText = "Stock";

        const th2 = document.createElement("th");
        th2.innerText = "Date added";

        const th5 = document.createElement("th");

        const tbody = document.createElement("tbody");

        div1.appendChild(div2);

        div3.appendChild(div4);
        div4.appendChild(table);

        table.appendChild(thead);
        thead.appendChild(tr1);

        tr1.appendChild(th1);
        tr1.appendChild(th2);
        tr1.appendChild(th5);

        table.appendChild(tbody);

        clearUI.appendChild(div1);
        clearUI.appendChild(div3);

        // console.log(response);
        for (var item in response) {
            // console.log(response[item]);
            const tr = document.createElement("tr");

            const td1 = document.createElement("td");
            td1.style.cursor = "pointer";

            const td2 = document.createElement("td");
            td2.style.cursor = "pointer";

            const td3 = document.createElement("td");
            td3.style.cursor = "pointer";

            // const td4 = document.createElement("td");
            // td4.style.cursor = "pointer";

            // const td5 = document.createElement("td");


            const buttonDiv = document.createElement("div");

            const button = document.createElement("div");
            button.setAttribute("class", "btn btn-danger btn-rounded");

            button.innerText = "-";

            buttonDiv.appendChild(button);

            td3.appendChild(buttonDiv);



            td1.innerText = response[item]["ticker"];

            var time = new Date(response[item]["time_added"]);
            var options = {
                year: 'numeric',
                month: 'short',
                day: 'numeric',
                hour: 'numeric',
                minute: 'numeric',
                hour12: 'true'
            };
            time = time.toLocaleString('en-AU', options);

            td2.innerText = time;


            tr.appendChild(td1);
            tr.appendChild(td2);
            tr.appendChild(td3);

            button.addEventListener("click", function (event) {
                const children = tr.childNodes;
                removeFromwatchlist(children[0].textContent || children[0].innerText || "");
            });

            tr.addEventListener("mouseenter", () => {
                tr.style.backgroundColor = "#e6e6e6";
                tr.style.backgroundColor = "#e6e6e6";
            });
            tr.addEventListener("mouseleave", () => {
                tr.style.backgroundColor = "";
                tr.style.backgroundColor = "";
            });

            td1.addEventListener("click", function (event) {
                const children = tr.childNodes;
                stockData(children[0].textContent || children[0].innerText || "");
            });

            td2.addEventListener("click", function (event) {
                const children = tr.childNodes;
                stockData(children[0].textContent || children[0].innerText || "");
            });

            tbody.appendChild(tr);
        }

    });

}

function populateWatchlist() {

    document.getElementById("Watchlist").addEventListener("click", () => {

        watchlist();

    });
}

function removeFromwatchlist(stockCode) {
    
    fetch(apiUrl+"/remove_watchlist_stock/" + stockCode,{
        method:"GET"
    })
    .then(()=>{
        document.getElementById("Watchlist").click();
    });
    
    // watchlist();
    //console.log(stockCode);
}

function stockData(stockID) {

    const clearUI = document.getElementById("dashboard_heading");
    while (clearUI.firstChild) {
        clearUI.removeChild(clearUI.firstChild);
    }

    const loaderDiv = document.createElement("div");
    loaderDiv.setAttribute("id", "loader");
    clearUI.appendChild(loaderDiv);
    fetch(apiUrl + "/stock/" + stockID, {
        method: 'GET',
    }).then(sresp => sresp.json()).then(function (stockInfo) {
        console.log(stockInfo);


        loaderDiv.parentElement.removeChild(loaderDiv);

        const holderDiv = document.createElement("div");

        const containerDiv1 = document.createElement("div");
        containerDiv1.setAttribute("class", "row")

        const headingDiv = document.createElement("div");
        headingDiv.setAttribute("class", "col-12 py-5");

        const backToSearch = document.createElement("h4");
        backToSearch.innerText = "<- Back";
        backToSearch.setAttribute("class", "animate-bottom");

        backToSearch.style.cursor = "pointer";

        backToSearch.addEventListener("mouseenter", () => {
            backToSearch.style.textDecoration = "underline";
        });

        backToSearch.addEventListener("mouseleave", () => {
            backToSearch.style.textDecoration = "none";
        });


        headingDiv.appendChild(backToSearch);
        containerDiv1.appendChild(headingDiv);

        const contentDiv = document.createElement("div");

        const stockName = document.createElement("h3");
        stockName.innerText = stockInfo["Global Quote"]["01. symbol"]

        // const stockSymbol = document.createElement("p");
        // stockSymbol.innerText = children[1].textContent || children[1].innerText || "";

        const currentPrice = document.createElement("h5");
        currentPrice.innerText = stockInfo["Global Quote"]["05. price"] + " USD";

        contentDiv.appendChild(stockName);
        // contentDiv.appendChild(stockSymbol);
        contentDiv.appendChild(currentPrice);
        contentDiv.setAttribute("class", "animate-bottom");


        holderDiv.appendChild(containerDiv1);
        holderDiv.appendChild(contentDiv);

        clearUI.appendChild(holderDiv);

        backToSearch.addEventListener("click", () => {
            watchlist();
        });

        const graphDiv = document.createElement("div");

        const navbar = document.createElement("nav");
        navbar.setAttribute("class", "navbar navbar-expand-sm bg-light navbar-light");

        const menu = document.createElement("ul");
        menu.setAttribute("class", "navbar-nav");
        menu.setAttribute("id", "navigation-menu");

        const li1 = document.createElement("li");
        li1.setAttribute("class", "nav-item active");
        const a1 = document.createElement("a");
        a1.setAttribute("href", "#");
        a1.setAttribute("class", "nav-link");
        a1.innerText = "1 day";
        li1.appendChild(a1);

        const li2 = document.createElement("li");
        li2.setAttribute("class", "nav-item");
        const a2 = document.createElement("a");
        a2.setAttribute("href", "#");
        a2.setAttribute("class", "nav-link");
        a2.innerText = "5 days";
        li2.appendChild(a2);

        const li3 = document.createElement("li");
        li3.setAttribute("class", "nav-item");
        const a3 = document.createElement("a");
        a3.setAttribute("href", "#");
        a3.setAttribute("class", "nav-link");
        a3.innerText = "1 week";
        li3.appendChild(a3);

        const li4 = document.createElement("li");
        li4.setAttribute("class", "nav-item");
        const a4 = document.createElement("a");
        a4.setAttribute("href", "#");
        a4.setAttribute("class", "nav-link");
        a4.innerText = "1 month";
        li4.appendChild(a4);

        // const li5 = document.createElement("li");
        // li5.setAttribute("class", "nav-item");
        // const a5 = document.createElement("a");
        // a5.setAttribute("href", "#");
        // a5.setAttribute("class", "nav-link");
        // a5.innerText = "YTD";
        // li5.appendChild(a5);

        // const li6 = document.createElement("li");
        // li6.setAttribute("class", "nav-item");
        // const a6 = document.createElement("a");
        // a6.setAttribute("href", "#");
        // a6.setAttribute("class", "nav-link");
        // a6.innerText = "1 year";
        // li6.appendChild(a6);

        // const li7 = document.createElement("li");
        // li7.setAttribute("class", "nav-item");
        // const a7 = document.createElement("a");
        // a7.setAttribute("href", "#");
        // a7.setAttribute("class", "nav-link");
        // a7.innerText = "5 years";
        // li7.appendChild(a7);

        const li8 = document.createElement("li");
        li8.setAttribute("class", "nav-item");
        li8.setAttribute("id", "max-time");
        const a8 = document.createElement("a");
        a8.setAttribute("href", "#");
        a8.setAttribute("class", "nav-link");
        a8.innerText = "Max";
        li8.appendChild(a8);


        menu.appendChild(li1);
        menu.appendChild(li2);
        menu.appendChild(li3);
        menu.appendChild(li4);
        // menu.appendChild(li5);
        // menu.appendChild(li6);
        // menu.appendChild(li7);
        menu.appendChild(li8);

        // navDiv.appendChild(menu);

        navbar.appendChild(menu);

        graphDiv.appendChild(navbar);

        if (stockInfo["Time Series"]["Meta Data"]) {

            const divider = document.createElement("div");
            divider.setAttribute("class", "col-md-6");

            const divider2 = document.createElement("div");
            divider2.setAttribute("class", "grid");

            const divider3 = document.createElement("div");
            divider3.setAttribute("class", "grid-body");

            const divider4 = document.createElement("div");
            divider4.setAttribute("class", "item-wrapper");

            const graph = document.createElement("canvas");
            graph.setAttribute("id", "chartjs-staked-line-chart");
            graph.setAttribute("width", "800");
            graph.setAttribute("height", "500");

            divider4.appendChild(graph);
            divider3.appendChild(divider4);
            divider2.appendChild(divider3);
            divider.appendChild(divider2);

            graphDiv.appendChild(divider);

            const bigData = stockInfo["Time Series"]["Time Series (Daily)"];

            var array = [];
            for (var key in bigData) {
                array.push(bigData[key]["4. close"]);
            }

            var daily = [];
            for (var key in bigData) {

                daily.push(bigData[key]["1. open"]);
                daily.push(bigData[key]["2. high"]);
                daily.push(bigData[key]["3. low"]);
                daily.push(bigData[key]["4. close"]);
                break;
            }

            var myChart = initChart(daily, graph);

            li8.addEventListener('click', () => {


                li8.setAttribute("class", "nav-item active");
                li4.setAttribute("class", "nav-item");
                li3.setAttribute("class", "nav-item");
                li2.setAttribute("class", "nav-item");
                li1.setAttribute("class", "nav-item");

                myChart = drawChart(array, myChart);
            });

            li3.addEventListener('click', () => {

                li3.setAttribute("class", "nav-item active");
                li4.setAttribute("class", "nav-item");
                li8.setAttribute("class", "nav-item");
                li2.setAttribute("class", "nav-item");
                li1.setAttribute("class", "nav-item");

                myChart = drawChart(array.slice(0, 7), myChart);
            });

            li4.addEventListener('click', () => {

                li4.setAttribute("class", "nav-item active");
                li8.setAttribute("class", "nav-item");
                li3.setAttribute("class", "nav-item");
                li2.setAttribute("class", "nav-item");
                li1.setAttribute("class", "nav-item");

                myChart = drawChart(array.slice(0, 31), myChart);
            });

            li2.addEventListener('click', () => {

                li2.setAttribute("class", "nav-item active");
                li4.setAttribute("class", "nav-item");
                li3.setAttribute("class", "nav-item");
                li8.setAttribute("class", "nav-item");
                li1.setAttribute("class", "nav-item");

                myChart = drawChart(array.slice(0, 5), myChart);
            });

            li1.addEventListener('click', () => {

                li1.setAttribute("class", "nav-item active");
                li4.setAttribute("class", "nav-item");
                li3.setAttribute("class", "nav-item");
                li2.setAttribute("class", "nav-item");
                li8.setAttribute("class", "nav-item");

                myChart = drawChart(daily, myChart);
            });

            contentDiv.appendChild(graphDiv);

        } else {


            const time_series_error_div = document.createElement("div");
            const time_series_error = document.createElement("p");
            time_series_error.innerText = "Time series data is unavailable for " + children[1].textContent || children[1].innerText || "" + "!";
            time_series_error.style.fontSize = "30px";
            time_series_error.style.textAlign = "center";

            time_series_error_div.appendChild(time_series_error);
            graphDiv.appendChild(time_series_error_div);
            contentDiv.appendChild(graphDiv);
        }


        contentDiv.appendChild(document.createElement("br"));

        const lastDiv = document.createElement("div");
        //console.log(stockInfo);
        const p1 = document.createElement("p");
        p1.innerText = "Open: \t" + stockInfo["Global Quote"]["02. open"];

        const p2 = document.createElement("p");
        p2.innerText = "High: \t" + stockInfo["Global Quote"]["03. high"];

        const p3 = document.createElement("p");
        p3.innerText = "Low: \t" + stockInfo["Global Quote"]["04. low"];

        const p4 = document.createElement("p");
        p4.innerText = "Prev Close: \t" + stockInfo["Global Quote"]["08. previous close"];

        const p5 = document.createElement("p");
        p5.innerText = "Change: \t" + stockInfo["Global Quote"]["09. change"];

        const p6 = document.createElement("p");
        p6.innerText = "Change percent: \t" + stockInfo["Global Quote"]["10. change percent"];

        lastDiv.appendChild(p1);
        lastDiv.appendChild(p2);
        lastDiv.appendChild(p3);
        lastDiv.appendChild(p4);
        lastDiv.appendChild(p5);
        lastDiv.appendChild(p6);

        contentDiv.appendChild(lastDiv);
    });
}

populateWatchlist();