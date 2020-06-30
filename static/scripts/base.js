var myTable = document.getElementsByTagName("form")[2];
var myClone = myTable.cloneNode(true);

var TReducersIncome = false;
var ReducersIncome = false;
var CapsInside = [];
var arrRec = [];
var dict = {};

document.getElementById('date').value = new Date().toLocaleString();  //                                       INITIALIZE DATE NOW
document.getElementById('date').value = document.getElementById('date').value.slice(0, 10);


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
    const element = document.createElement('a');

    var separator = ';'; //--------------------------------------------------------------SWITCH BETWEEN ';' AND ',' TO DEFINE THE OUTPUT-----------------------------
    var nameDoc = document.getElementById('document');

    var line = "Document" + separator + "Revision" + separator + "ISO" + separator + "Project Number" + separator + "Date" + separator + "Name" + separator + "Component" + separator + "Batch Number" + separator + "Charge Number" + separator + "Spool" + separator + "Weld" + separator + "Wall Thickness" + separator + "BBE" + separator + "Diameter" + separator + "Calculated Length" + separator + "Comments" + "\n";

    for (var i = 0; i < document.getElementsByTagName("table").length; i++) {
        var compA = document.getElementsByTagName("table")[i].rows[0].cells[0].getElementsByTagName("div")[19].childNodes[0].value;
        var compB = document.getElementsByTagName("table")[i].rows[0].cells[0].getElementsByTagName("div")[20].childNodes[0].value;
        var isoN = document.getElementById('iso').value;
        var batchN = document.getElementsByTagName("table")[i].rows[0].cells[0].getElementsByTagName("div")[21].childNodes[0].value;
        var chargeN = document.getElementsByTagName("table")[i].rows[0].cells[0].getElementsByTagName("div")[22].childNodes[0].value;
        var spool = document.getElementsByTagName("table")[i].rows[0].cells[0].getElementsByTagName("div")[14].childNodes[0].value;

        var weldA = document.getElementsByTagName("table")[i].rows[0].cells[0].getElementsByTagName("div")[18].childNodes[0].value;
        var weldB = document.getElementsByTagName("table")[i].rows[0].cells[0].getElementsByTagName("div")[18].childNodes[0].value;
        var wallTh = document.getElementsByTagName("table")[i].rows[0].cells[0].getElementsByTagName("div")[15].childNodes[0].value;
        var BBEa = document.getElementsByTagName("table")[i].rows[0].cells[0].getElementsByTagName("div")[34].childNodes[0].value;
        var BBEb = document.getElementsByTagName("table")[i].rows[0].cells[0].getElementsByTagName("div")[35].childNodes[0].value;
        var diameter = document.getElementsByTagName("table")[i].rows[0].cells[0].getElementsByTagName("div")[16].childNodes[0].value;
        var rezLength = document.getElementsByTagName("table")[0].rows[0].cells[0].getElementsByTagName("div")[36].childNodes[1].value;
        var comments = document.getElementsByTagName("table")[i].rows[0].cells[0].getElementsByTagName("div")[23].childNodes[0].value;

        line += nameDoc.value + separator + document.getElementById('revision').value + separator + isoN + separator + document.getElementById('projectnr').value + separator + document.getElementById('date').value + separator + document.getElementById('name').value + separator + compA + separator + batchN + separator + chargeN + separator + spool + separator + weldA + separator + wallTh + separator + BBEa + separator + diameter + separator + rezLength + separator + comments + "\n";
        line += nameDoc.value + separator + document.getElementById('revision').value + separator + isoN + separator + document.getElementById('projectnr').value + separator + document.getElementById('date').value + separator + document.getElementById('name').value + separator + compB + separator + batchN + separator + chargeN + separator + spool + separator + weldB + separator + wallTh + separator + BBEb + separator + diameter + separator + rezLength + separator + comments + "\n";
    }

    if (nameDoc.value === "") {
        alert('The document field is empty, enter and try again');
    } else {
        var fullnameDoc = nameDoc.value + '.csv';

        element.setAttribute('href', 'data:text/plain;charset=utf-8,' + line);
        element.setAttribute('download', fullnameDoc);

        element.style.display = 'none';
        document.body.appendChild(element);
        element.click();
        document.body.removeChild(element);
    }
}


function checkDia(obj) {
    var diameter = obj.value;
    var flag = obj.parentNode.parentNode.getElementsByTagName("div")[11].getElementsByTagName("input")[0].checked;

    var compAselect = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[19].childNodes[0];
    var compBselect = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[20].childNodes[0];

    var compAvar1 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[27].childNodes[0];
    var compBvar1 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[28].childNodes[0];

    var compAvar2 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[31].childNodes[0];
    var compBvar2 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[32].childNodes[0];

    var length = compAselect.options.length;
    for (k = length - 1; k >= 0; k--) {
        compAselect.options[k] = null;
    }
    length = compBselect.options.length;
    for (k = length - 1; k >= 0; k--) {
        compBselect.options[k] = null;
    }
    length = compAvar1.options.length;
    for (k = length - 1; k >= 0; k--) {
        compAvar1.options[k] = null;
    }
    length = compBvar1.options.length;
    for (k = length - 1; k >= 0; k--) {
        compBvar1.options[k] = null;
    }
    length = compAvar2.options.length;
    for (k = length - 1; k >= 0; k--) {
        compAvar2.options[k] = null;
    }
    length = compBvar2.options.length;
    for (k = length - 1; k >= 0; k--) {
        compBvar2.options[k] = null;
    }

    compAselect.disabled = true;
    compBselect.disabled = true;
    compAvar1.disabled = true;
    compAvar2.disabled = true;
    compBvar1.disabled = true;
    compBvar2.disabled = true;

    compAselect.style.borderColor = "black";
    compBselect.style.borderColor = "black";
    compAvar1.style.borderColor = "black";
    compAvar2.style.borderColor = "black";
    compBvar1.style.borderColor = "black";
    compBvar2.style.borderColor = "black";

    if (obj.value !== "") {
        if (isFinite(obj.value)) {
            $.ajax({
                type: 'GET',
                url: "/checkDia",
                data: {
                    diameter: diameter,
                    flag: flag
                },
                success: function (response) {
                    CapsInside = [];
                    TReducersIncome = false;
                    ReducersIncome = false;
                    if (response["valid"]) {
                        let tmpArr = [];
                        dict = {};
                        arrRec = [];
                        compAselect.disabled = false;
                        compBselect.disabled = false;
                        compAselect.style.borderColor = "blue";
                        compBselect.style.borderColor = "blue";

                        obj.style.borderColor = "blue";

                        if (flag) {
                            Object.keys(response).forEach(function (key) {
                                arrRec.push(key);

                            });
                            arrRec.shift();
                            arrRec.pop();

                            let names = JSON.parse(response["names"]);
                            let namesarr = [];
                            Object.keys(names).forEach(function (key) { // Здесь key = "wallthickness"; value = 3
                                var value = names[key];
                                namesarr.push(value);
                            });

                            TReducersIncome = JSON.parse(response["data5"]);
                            ReducersIncome = JSON.parse(response["data4"]);
                            Angle90Income = JSON.parse(response["data1"]);
                            Angle180Income = JSON.parse(response["data2"]);
                            TPieceIncome = JSON.parse(response["data3"]);
                            CapsToHZ = JSON.parse(response["data10"]);


                            //alert("2");
                            for (let el in arrRec) {
                                let somearr = [];
                                let receive = JSON.parse(response[arrRec[el]]);

                                if (el > 4) {
                                    Object.keys(receive).forEach(function (key) {
                                        var value = receive[key];
                                        //alert(JSON.stringify(value));
                                        Object.keys(value).forEach(function (key) { // Здесь key = "wallthickness"; value = 3
                                            if (el > 4 && el < 9) {
                                                var val = value[key];
                                                if (val !== null && val !== "None")
                                                    somearr.push(key);
                                            }
                                        });
                                    });
                                }
                                if (somearr.length !== 0) {
                                    //alert(names[el] + " " + el);
                                    dict[namesarr[el]] = somearr;
                                }
                            }

                            Object.keys(dict).forEach(function (key) {
                                var myOption = document.createElement("option");
                                myOption.text = convertNameOfFlanges(key);
                                compAselect.add(myOption);
                            });

                            Object.keys(dict).forEach(function (key) {
                                var myOption = document.createElement("option");
                                myOption.text = convertNameOfFlanges(key);
                                compBselect.add(myOption);
                            });

                            if (TReducersIncome) {
                                myOption = document.createElement("option");
                                var myOption2 = document.createElement("option");

                                if (!flag) {
                                    myOption.text = convertNameOfFlanges('TReducer');
                                    myOption2.text = convertNameOfFlanges('TReducer');
                                } else {
                                    myOption.text = convertNameOfFlanges('TReducerPieceDIN');
                                    myOption2.text = convertNameOfFlanges('TReducerPieceDIN');
                                }

                                compAselect.add(myOption);
                                compBselect.add(myOption2);
                            }

                            if (ReducersIncome) {
                                myOption = document.createElement("option");
                                var myOption2 = document.createElement("option");

                                if (!flag) {
                                    myOption.text = convertNameOfFlanges('Reducer');
                                    myOption2.text = convertNameOfFlanges('Reducer');
                                } else {
                                    myOption.text = 'ReducerDIN';
                                    myOption2.text = 'ReducerDIN';
                                }

                                compAselect.add(myOption);
                                compBselect.add(myOption2);
                            }

                            if (Angle90Income) {
                                myOption = document.createElement("option");
                                var myOption2 = document.createElement("option");
                                myOption.text = 'Angle90';
                                myOption2.text = 'Angle90';
                                compAselect.add(myOption);
                                compBselect.add(myOption2);
                            }

                            if (Angle180Income) {
                                myOption = document.createElement("option");
                                var myOption2 = document.createElement("option");
                                myOption.text = 'Angle180';
                                myOption2.text = 'Angle180';
                                compAselect.add(myOption);
                                compBselect.add(myOption2);
                            }

                            if (TPieceIncome) {
                                myOption = document.createElement("option");
                                var myOption2 = document.createElement("option");
                                myOption.text = 'TPieceDIN';
                                myOption2.text = 'TPieceDIN';
                                compAselect.add(myOption);
                                compBselect.add(myOption2);
                            }

                            //alert(JSON.stringify(CapsToHZ));
                            if (JSON.stringify(CapsToHZ) !== "[]") {
                                CapsToHZ = CapsToHZ[0];
                                var partLeft = CapsToHZ["pipe_diam"];
                                var partRight = CapsToHZ["TValueinterval"];
                                CapsInside.push(partLeft);
                                if (partRight !== null && partRight !== "null") {
                                    CapsInside.push(partRight)
                                }
                                myOption = document.createElement("option");
                                var myOption2 = document.createElement("option");
                                myOption.text = 'Caps';
                                myOption2.text = 'Caps';
                                compAselect.add(myOption);
                                compBselect.add(myOption2);
                            }

                            var myOptions = document.createElement("option");
                            myOptions.text = "SPECIAL";
                            var myOptionss = document.createElement("option");
                            myOptionss.text = "SPECIAL";
                            compAselect.add(myOptionss);
                            compBselect.add(myOptions);
                            //-----------------------------------------------------------------------------------------------
                        } else {
                            Object.keys(response).forEach(function (key) {
                                arrRec.push(key);
                            });
                            arrRec.shift();
                            arrRec.pop();

                            let names = JSON.parse(response["names"]);
                            let namesarr = [];
                            Object.keys(names).forEach(function (key) { // Здесь key = "wallthickness"; value = 3
                                var value = names[key];
                                namesarr.push(value);
                                //alert(key + " " + value);
                                //alert(JSON.stringify(value));
                            });
                            //alert(namesarr);
                            //alert(arrRec);

                            TReducersIncome = JSON.parse(response["data11"]);
                            ReducersIncome = JSON.parse(response["data12"]);

                            //alert("2");
                            for (let el in arrRec) {
                                let somearr = [];
                                let receive = JSON.parse(response[arrRec[el]]);

                                Object.keys(receive).forEach(function (key) {
                                    var value = receive[key];
                                    //alert(JSON.stringify(value));
                                    Object.keys(value).forEach(function (key) { // Здесь key = "wallthickness"; value = 3
                                        if (el < 4) {
                                            var val = value[key];
                                            if (val !== null && val !== "None")
                                                somearr.push(val);
                                        } else {
                                            if (el < 8) {
                                                var val = value[key];
                                                if (val !== null && val !== "None")
                                                    somearr.push(key)
                                            }
                                        }
                                    });
                                });
                                if (somearr.length !== 0) {
                                    //alert(names[el] + " " + el);
                                    dict[namesarr[el]] = somearr;
                                }
                            }

                            Object.keys(dict).forEach(function (key) {
                                var myOption = document.createElement("option");
                                myOption.text = convertNameOfFlanges(key);
                                compAselect.add(myOption);
                            });

                            Object.keys(dict).forEach(function (key) {
                                var myOption = document.createElement("option");
                                myOption.text = convertNameOfFlanges(key);
                                compBselect.add(myOption);
                            });

                            if (TReducersIncome) {
                                myOption = document.createElement("option");
                                var myOption2 = document.createElement("option");
                                myOption.text = convertNameOfFlanges('TReducer');
                                myOption2.text = convertNameOfFlanges('TReducer');
                                compAselect.add(myOption);
                                compBselect.add(myOption2);
                            }

                            if (ReducersIncome) {
                                myOption = document.createElement("option");
                                var myOption2 = document.createElement("option");
                                myOption.text = 'Reducer';
                                myOption2.text = 'Reducer';
                                compAselect.add(myOption);
                                compBselect.add(myOption2);
                            }

                            var myOptions = document.createElement("option");
                            myOptions.text = "SPECIAL";
                            var myOptionss = document.createElement("option");
                            myOptionss.text = "SPECIAL";
                            compAselect.add(myOptionss);
                            compBselect.add(myOptions);
                        }
                        getDictA(compAselect);
                        getDictB(compBselect);
                    } else {
                        obj.style.borderColor = "red";
                    }
                }
            });
        }
    }
}


function getDictA(obj) {
    var compAselect = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[19].childNodes[0];
    var compBselect = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[20].childNodes[0];

    var compAvar1 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[27].childNodes[0];
    var compBvar1 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[28].childNodes[0];

    var compAvar2 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[31].childNodes[0];
    var compBvar2 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[32].childNodes[0];

    var specialA = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[26].childNodes[0];

    length = compAvar1.options.length;
    for (k = length - 1; k >= 0; k--) {
        compAvar1.options[k] = null;
    }
    length = compAvar2.options.length;
    for (k = length - 1; k >= 0; k--) {
        compAvar2.options[k] = null;
    }

    compAvar1.disabled = false;
    compAvar2.disabled = true;

    compAvar1.style.borderColor = "blue";
    compAvar2.style.borderColor = "black";
    specialA.style.borderColor = "violet";

    if (obj.value === "SPECIAL") {
        specialA.readOnly = false;
        specialA.style.borderColor = "blue";
    } else {
        specialA.value = "";
        specialA.readOnly = true;
    }

    //--------------------------------------------

    var compSelected = convertNameOfFlanges(obj.options[obj.selectedIndex].text);
    if (compSelected === "TReducer" || compSelected === "Reducer" || compSelected === "TReducerPieceDIN" || compSelected === "ReducerDIN") {
        compAvar1.disabled = false;
        compAvar1.style.borderColor = "blue";
        var someOption = document.createElement("option");
        someOption.text = "Big";
        compAvar1.add(someOption);
        var someOption2 = document.createElement("option");
        someOption2.text = "Small";
        compAvar1.add(someOption2);
    }

    //alert(CapsInside.length + " " + CapsInside[0] + " " + CapsInside[1]);
    if (compSelected === "Caps") {
        if (CapsInside.length === 1) {
        } else {
            compAvar1.disabled = false;
            compAvar1.style.borderColor = "blue";
            myOption = document.createElement("option");
            var myOption2 = document.createElement("option");
            myOption.text = 'T <= ' + CapsInside[1];
            myOption2.text = 'T > ' + CapsInside[1];
            compAvar1.add(myOption);
            compAvar1.add(myOption2);
        }
    }

    Object.keys(dict).forEach(function (key) {
        if (key === compSelected) {
            var value = dict[key];
            for (el in value) {
                var myOption = document.createElement("option");
                myOption.text = convertFlange(value[el]);
                compAvar1.add(myOption);
            }
        }
    });

    if (compAselect.value === "Angle90" || compAselect.value === "Angle180" || compAselect.value === "TPieceDIN" || compAselect.value === convertNameOfFlanges("TPiece")) {
        compAvar1.disabled = true;
        compAvar1.style.borderColor = "black";
    }

    if (compAselect.value === "TEE EQUAL") {
        length = compAvar1.options.length;
        for (k = length - 1; k >= 0; k--) {
            compAvar1.options[k] = null;
        }
    }

    getVar2A(compAvar1);
}

function getDictB(obj) {
    var compAselect = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[20].childNodes[0];
    var compBselect = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[20].childNodes[0];

    var compAvar1 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[28].childNodes[0];
    var compBvar1 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[28].childNodes[0];

    var compAvar2 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[32].childNodes[0];
    var compBvar2 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[32].childNodes[0];

    var specialA = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[29].childNodes[0];

    length = compAvar1.options.length;
    for (k = length - 1; k >= 0; k--) {
        compAvar1.options[k] = null;
    }
    length = compAvar2.options.length;
    for (k = length - 1; k >= 0; k--) {
        compAvar2.options[k] = null;
    }

    compAvar1.disabled = false;
    compAvar2.disabled = true;

    compAvar1.style.borderColor = "blue";
    compAvar2.style.borderColor = "black";
    specialA.style.borderColor = "violet";

    if (obj.value === "SPECIAL") {
        specialA.readOnly = false;
        specialA.style.borderColor = "blue";
    } else {
        specialA.value = "";
        specialA.readOnly = true;
    }

    //--------------------------------------------

    var compSelected = convertNameOfFlanges(obj.options[obj.selectedIndex].text);
    if (compSelected === "TReducer" || compSelected === "Reducer" || compSelected === "TReducerPieceDIN" || compSelected === "ReducerDIN") {
        compAvar1.disabled = false;
        compAvar1.style.borderColor = "blue";
        var someOption = document.createElement("option");
        someOption.text = "Big";
        compAvar1.add(someOption);
        var someOption2 = document.createElement("option");
        someOption2.text = "Small";
        compAvar1.add(someOption2);
    }

    //alert(CapsInside.length + " " + CapsInside[0] + " " + CapsInside[1]);
    if (compSelected === "Caps") {
        if (CapsInside.length === 1) {
        } else {
            compAvar1.disabled = false;
            compAvar1.style.borderColor = "blue";
            myOption = document.createElement("option");
            var myOption2 = document.createElement("option");
            myOption.text = 'T <= ' + CapsInside[1];
            myOption2.text = 'T > ' + CapsInside[1];
            compAvar1.add(myOption);
            compAvar1.add(myOption2);
        }
    }

    Object.keys(dict).forEach(function (key) {
        if (key === compSelected) {
            var value = dict[key];
            for (el in value) {
                var myOption = document.createElement("option");
                myOption.text = convertFlange(value[el]);
                compAvar1.add(myOption);
            }
        }
    });

    if (compAselect.value === "Angle90" || compAselect.value === "Angle180" || compAselect.value === "TPieceDIN" || compAselect.value === convertNameOfFlanges("TPiece")) {
        compAvar1.disabled = true;
        compAvar1.style.borderColor = "black";
    }

    if (compAselect.value === "TEE EQUAL") {
        length = compAvar1.options.length;
        for (k = length - 1; k >= 0; k--) {
            compAvar1.options[k] = null;
        }
    }

    getVar2B(compAvar1);
}

function getVar2A(obj) {
    var diameter = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[16].childNodes[0].value;

    var compAselect = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[19].childNodes[0];
    var compBselect = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[20].childNodes[0];

    var compAvar1 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[27].childNodes[0];
    var compBvar1 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[28].childNodes[0];

    var compAvar2 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[31].childNodes[0];
    var compBvar2 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[32].childNodes[0];

    var specialA = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[26].childNodes[0];

    length = compAvar2.options.length;
    for (k = length - 1; k >= 0; k--) {
        compAvar2.options[k] = null;
    }

    if (obj.value === "Big" || obj.value === "Small") {
        nameForAjax = convertNameOfFlanges(compAselect.options[compAselect.selectedIndex].text);

        $.ajax({
            type: 'GET',
            url: "/checkDiaTwo",
            data: {
                diameter: diameter,
                type: nameForAjax,
                parameter: obj.value
            },
            success: function (response) {
                if (response["valid"]) {
                    var receive = JSON.parse(response["data"]);
                    Object.keys(receive).forEach(function (key) {
                        var value = receive[key];
                        Object.keys(value).forEach(function (key) {
                            var tmp = value[key];
                            var myOption = document.createElement("option");
                            myOption.text = tmp;
                            if (tmp !== null) {
                                compAvar2.disabled = false;
                                compAvar2.style.borderColor = "blue";
                                compAvar2.add(myOption);
                            }
                        });
                    });
                }
            }
        });
    }

    if (compAselect.value === "Weldolet") {
        $.ajax({
            type: 'GET',
            url: "/checkDiaTwo",
            data: {
                diameter: diameter,
                type: "Weldolet",
                parameter: obj.value
            },
            success: function (response) {
                if (response["valid"]) {
                    var receive = JSON.parse(response["data"]);
                    Object.keys(receive).forEach(function (key) {
                        var value = receive[key];
                        Object.keys(value).forEach(function (key) {
                            var tmp = value[key];
                            var myOption = document.createElement("option");
                            let somestr = key;
                            myOption.text = convertWeldolet(somestr);
                            if (tmp !== null) {
                                compAvar2.disabled = false;
                                compAvar2.style.borderColor = "blue";
                                compAvar2.add(myOption);
                            }
                        });
                    });
                }
            }
        });
    }
}


function getVar2B(obj) {
    var diameter = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[16].childNodes[0].value;

    var compAselect = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[20].childNodes[0];
    var compBselect = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[20].childNodes[0];

    var compAvar1 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[27].childNodes[0];
    var compBvar1 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[28].childNodes[0];

    var compAvar2 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[32].childNodes[0];
    var compBvar2 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[32].childNodes[0];

    var specialA = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[29].childNodes[0];

    length = compAvar2.options.length;
    for (k = length - 1; k >= 0; k--) {
        compAvar2.options[k] = null;
    }

    if (obj.value === "Big" || obj.value === "Small") {
        nameForAjax = convertNameOfFlanges(compAselect.options[compAselect.selectedIndex].text);

        $.ajax({
            type: 'GET',
            url: "/checkDiaTwo",
            data: {
                diameter: diameter,
                type: nameForAjax,
                parameter: obj.value
            },
            success: function (response) {
                if (response["valid"]) {
                    var receive = JSON.parse(response["data"]);
                    Object.keys(receive).forEach(function (key) {
                        var value = receive[key];
                        Object.keys(value).forEach(function (key) {
                            var tmp = value[key];
                            var myOption = document.createElement("option");
                            myOption.text = tmp;
                            if (tmp !== null) {
                                compAvar2.disabled = false;
                                compAvar2.style.borderColor = "blue";
                                compAvar2.add(myOption);
                            }
                        });
                    });
                }
            }
        });
    }

    if (compAselect.value === "Weldolet") {
        $.ajax({
            type: 'GET',
            url: "/checkDiaTwo",
            data: {
                diameter: diameter,
                type: "Weldolet",
                parameter: obj.value
            },
            success: function (response) {
                if (response["valid"]) {
                    var receive = JSON.parse(response["data"]);
                    Object.keys(receive).forEach(function (key) {
                        var value = receive[key];
                        Object.keys(value).forEach(function (key) {
                            var tmp = value[key];
                            var myOption = document.createElement("option");
                            let somestr = key;
                            myOption.text = convertWeldolet(somestr);
                            if (tmp !== null) {
                                compAvar2.disabled = false;
                                compAvar2.style.borderColor = "blue";
                                compAvar2.add(myOption);
                            }
                        });
                    });
                }
            }
        });
    }
}


function calculate(obj) {
    var diameter = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[16].childNodes[0].value;
    var length = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[17].childNodes[0].value;
    var weld = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[18].childNodes[0].value;

    var compAselect = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[19].childNodes[0];
    var compBselect = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[20].childNodes[0];

    var compAvar1 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[27].childNodes[0];
    var compBvar1 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[28].childNodes[0];

    var compAvar2 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[31].childNodes[0];
    var compBvar2 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[32].childNodes[0];

    var specialA = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[26].childNodes[0];
    var specialB = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[29].childNodes[0];

    var rez = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[36].childNodes[1];

    $.ajax({
        type: 'GET',
        url: "/calculate",
        data: {
            compAname: convertNameOfFlanges(compAselect.value),
            compAprops: compAvar2.value,
            weld: weld, //--------
            compAvar: compAvar1.value,
            compBname: convertNameOfFlanges(compBselect.value),
            compBprops: compBvar2.value,
            compBvar: compBvar1.value,
            diameter: diameter,
            length: length,
            compAinput: specialA.value,
            compBinput: specialB.value
        },
        success: function (response) {
            //alert(1);
            if (response['valid'] === false) {
                alert(response['reason']);
                rez.value = 'error ocured';
            } else {
                rez.value = response["instance"];
            }

        }
    });
}

function convertFlange(somestr) {
    if (somestr === 'PN212')
        somestr = 'PN2.5';
    return somestr;
}

function convertWeldolet(somestr) {
    if (somestr === 'weldolet_diam1')
        somestr = '3/8 inches';
    if (somestr === 'weldolet_diam2')
        somestr = '1/2 inches';
    if (somestr === 'weldolet_diam3')
        somestr = '3/4 inches';
    if (somestr === 'weldolet_diam4')
        somestr = '1 inches';
    if (somestr === 'weldolet_diam5')
        somestr = '1-1/2 inches';
    if (somestr === 'weldolet_diam6')
        somestr = '2 inches';
    if (somestr === 'weldolet_diam7')
        somestr = '3 inches';
    if (somestr === 'weldolet_diam8')
        somestr = '4 inches';
    if (somestr === 'weldolet_diam9')
        somestr = '6 inches';
    if (somestr === 'weldolet_diam10')
        somestr = '8 inches';
    if (somestr === 'weldolet_diam11')
        somestr = '10 inches';
    if (somestr === 'weldolet_diam12')
        somestr = '12 inches';
    if (somestr === 'weldolet_diam13')
        somestr = '14 inches';
    if (somestr === 'weldolet_diam14')
        somestr = '16 inches';
    if (somestr === 'weldolet_diam15')
        somestr = '18 inches';
    if (somestr === 'weldolet_diam16')
        somestr = '20 inches';
    if (somestr === 'weldolet_diam17')
        somestr = '24 inches';
    return somestr;
}

function checkLength(obj) {
    if (isFinite(obj.value)) {
        obj.style.borderColor = "blue";
    } else {
        obj.style.borderColor = "red";
    }
}


function convertNameOfFlanges(somestr) {
    if (somestr === 'TPiece') {
        return 'TEE EQUAL'
    }
    if (somestr === 'WeldingNeckFlangASAASTM') {
        return 'FLANGE Weldingneck'
    }
    if (somestr === 'WeldingBend') {
        return 'ELBOW'
    }
    if (somestr === 'InsertFlang') {
        return 'FLANGE Insert'
    }
    if (somestr === 'TReducer') {
        return 'TEE REDUCING'
    }

    if (somestr === 'TEE EQUAL') {
        return 'TPiece'
    }
    if (somestr === 'FLANGE Weldingneck') {
        return 'WeldingNeckFlangASAASTM'
    }
    if (somestr === 'ELBOW') {
        return 'WeldingBend'
    }
    if (somestr === 'FLANGE Insert') {
        return 'InsertFlang'
    }
    if (somestr === 'TEE REDUCING') {
        return 'TReducer'
    }
    return somestr;
}