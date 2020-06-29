var myTable = document.getElementsByTagName("form")[2];
var myClone = myTable.cloneNode(true);


function createTable() {
    currentDiv = document.getElementById("tableDiv");
    tableCopy = myClone.cloneNode(true);
    tableCopy.id = (document.getElementsByTagName("table").length + 1).toString() + 'form';


    currentDiv.appendChild(tableCopy);
    window.scrollTo(0, document.body.scrollHeight);
}


function topFunction() {
    window.scrollTo(0, 0);
}


function deleteTable() {
    currentDiv = document.getElementById("tableDiv");
    var indexTable = document.getElementsByTagName("table").length;
    var lastTable = document.getElementsByTagName("table")[indexTable - 1];

    lastTable.parentNode.removeChild(lastTable);
}


function CSVExportMaster() {
    //TO IMPLEMENT
    alert('Error');
}