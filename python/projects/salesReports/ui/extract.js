
function getJSON(){
    var getJSONButton = document.getElementById("getJSONButton");
    if (getJSONButton.value === "0"){
        // console.log("add count");
        getJSONButton.value = "1";
    } 
    else{
        // console.log("return");
        return;
    }
    const request = new Request('/data.json');
    // const url = request.url;
    // const method = request.method;
    // const credentials = request.credentials;
    
    fetch(request)
        .then(response => {
            if (response.status === 200) {
                console.log('got json', response);
                return response.json();
            }   else {
                throw new Error('Something went wrong on api server!');
            }
        })
        .then(response => {
            
            
            // var row1 = table1.insertRow();
            // var row2 = table1.insertRow();
            // var cell1 = row1.insertCell();
            // var cell2 = row1.insertCell();
            // var cell3 = row1.insertCell();
            // var cell4 = row2.insertCell();
            // var cell5 = row2.insertCell();
            // var cell6 = row2.insertCell();
            // cell1.innerHTML = response.SalesReport[0].Year;
            // cell2.innerHTML = response.SalesReport[1].Year;
            // cell3.innerHTML = response.SalesReport[2].Year;
            // cell4.innerHTML = response.SalesReport[0].Sales;
            // cell5.innerHTML = response.SalesReport[1].Sales;
            // cell6.innerHTML = response.SalesReport[2].Sales;

            response.SalesReport.forEach(element => {
                console.log([element.Year, element.Sales]);
                console.log(element);
                var arr = [element.Year, element.Sales];
                var arrLength = arr.length;

                // big/horizontal
                // Year|	2017|  2018| 2019
                // sales|	$	|$	|$

    //     <tr id="row1">
                //     <th>Year</th>
        // </tr>
            // <tr id="row2">
                //     <th>Sales</th>
        // </tr>
                // ['Year', 'Sales'].forEach( rowElement => {
                //     var row = document.getElementById("horizontalRow"+rowElement);
                //     var cell = row.insertCell();
                //     cell.innerHTML = element[rowElement];
                // })
                // var tablebigHorizontal = document.getElementById("tablebigHorizontal");
                // var horizontalRowYear = document.getElementById("horizontalRowYear");
                // var horizontalRowSales = document.getElementById("horizontalRowSales");
                // var cell1 = horizontalRowYear.insertCell();
                // var cell2 = horizontalRowSales.insertCell();
                // cell1.innerHTML = (arr[0]);
                // cell2.innerHTML = (arr[1]);

                // arr.forEach(Arrelement => {
                //     var cell = row.insertCell();
                //     cell.innerHTML = Arrelement;
                // });
                for (var i = 0; i < arrLength; i++) {
                    let row = tablebigHorizontal.rows[i];
                    var cell = row.insertCell();
                    cell.innerHTML = arr[i];
                }

                // small/vertical
                // <tr id="row1"></tr>
                    // <th>Year</th>
                    // <th>Sales</th>
                // </tr>

                // Year | Sales
                // 2017 | $
                // 2018 | $
                var tableSmallVertical = document.getElementById("tableSmallVertical");
                var row = tableSmallVertical.insertRow();
                arr.forEach(Arrelement => {
                    var cell = row.insertCell();
                    cell.innerHTML = Arrelement;
                });


                // var cell1 = row1.insertCell();
                // var cell2 = row1.insertCell();
                // cell1.innerHTML = (arr[0]);
                // cell2.innerHTML = (arr[1]);
                // tr.push('<tr><td>' + element.Year + '</td></tr>')
                // tr.push('<td><tr>' + element.Sales + '</tr></td>')
                // cell.innerHTML = element.Year;
                // cell2.innerHTML = element.Year;
                // cell3.innerHTML = element.Year;
            });

            // response.SalesReport.forEach(element => {
            //     // tr.push('<tr><td>' + element.Year + '</td></tr>')
            //     // tr.push('<td><tr>' + element.Sales + '</tr></td>')
            //     cell.innerHTML = element.Sales;
            //     // cell2.innerHTML = element.Sales;
            //     // cell3.innerHTML = element.Sales;
            // });
            
            
            console.log((response.SalesReport[0].Year))
           
            // jsonFile = JSON.parse(response)
            // alert(obj[0].Year);
            // alert(obj[0].Sales);
            // alert(obj[1].Year);
            // alert(obj[1].Sales);
            // alert(obj[2].Year);
            // alert(obj[2].Sales);
            console.log('debug');
            console.debug(response);
            resizeDisplay();
            window.addEventListener('resize', resizeDisplay);

            // ...
        })
        .catch(error => {
            console.log('error catch');
            console.error(error);
        });
        console.log('outside fetch');

    //   request.json().then(function(response) {
    //     do something with the data sent in the request
    //     alert(response[0].Year);
    //     alert(response[0].Sales);
    //     alert(response[1].Year);
    //     alert(response[1].Sales);
    //     alert(response[2].Year);
    //     alert(response[2].Sales);
    //     catch
    //   });
    // var response = JSON.parse(data)();
        
}

function toggleDisplay() {
    var x = document.getElementById("table1DIV");
    if (x.style.display === "none") {
        x.style.display = "block";
    }
    else{
        x.style.display = "none";
    }
    var y = document.getElementById("table2DIV");
    if (y.style.display === "none") {
        y.style.display = "block";
    }
    else{
        y.style.display = "none";
    }
}

function resizeDisplay() {
    var x = document.getElementById("table1DIV");
    var y = document.getElementById("table2DIV");
    if (document.documentElement.clientWidth < 673) {
        x.style.display = "none";
        y.style.display = "block";
    }
    else{
        y.style.display = "none";
        x.style.display = "block";
    }
}