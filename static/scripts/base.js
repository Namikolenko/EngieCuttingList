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
    //TO IMPLEMENT
    alert('Error');
}


function checkDia(obj) {
    var diameter = obj.value;
    var flag = obj.parentNode.parentNode.getElementsByTagName("div")[10].getElementsByTagName("input")[0].checked;

    var compAselect = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[19].childNodes[0];
    var compBselect = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[20].childNodes[0];
    //alert(obj);
    //alert(obj.parentNode);
    //alert(obj.parentNode.parentNode.parentNode.parentNode.getElementsByTagName("div")[0]);
    //alert(obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[11].childNodes[0].textContent);
    //alert(obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[29].childNodes[0]);
    obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[19].childNodes[0].style.borderColor = "blue";
    var compAvar1 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[27].childNodes[0];
    var compBvar1 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[28].childNodes[0];

    var compAvar2 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[31].childNodes[0];
    var compBvar2 = obj.parentNode.parentNode.parentNode.getElementsByTagName("div")[32].childNodes[0];

    var length = compAselect.options.length;
    for (k = length - 1; k > 0; k--) {
        compAselect.options[k] = null;
    }
    length = compBselect.options.length;
    for (k = length - 1; k > 0; k--) {
        compBselect.options[k] = null;
    }
    length = compAvar1.options.length;
    for (k = length - 1; k > 0; k--) {
        compAvar1.options[k] = null;
    }
    length = compBvar1.options.length;
    for (k = length - 1; k > 0; k--) {
        compBvar1.options[k] = null;
    }
    length = compAvar2.options.length;
    for (k = length - 1; k > 0; k--) {
        compAvar2.options[k] = null;
    }
    length = compBvar2.options.length;
    for (k = length - 1; k > 0; k--) {
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

    if (obj.value !== ""){
        if (isFinite(obj.value)){
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
                    if (response["valid"]){
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
                                //alert(key + " " + value);
                                //alert(JSON.stringify(value));
                            });
                            //alert(namesarr);
                            //alert(arrRec);

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

                            var length = compAselect.options.length;
                            for (k = length - 1; k > 0; k--) {
                                compAselect.options[k] = null;
                            }

                            var lengthB = compBselect.options.length;
                            for (k = lengthB - 1; k > 0; k--) {
                                compBselect.options[k] = null;
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

                                if (!obj.parentNode.getElementsByTagName('input')[1].checked) {
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

                                if (!obj.parentNode.getElementsByTagName('input')[1].checked) {
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
                                /*if (partRight !== "") {
                                    myOption = document.createElement("option");
                                    var myOption2 = document.createElement("option");
                                    myOption.text = 'T <= ' + partRight;
                                    myOption2.text = 'T <= ' + partRight;
                                    compAselect.add(myOption);
                                    compBselect.add(myOption2);
                                    var myOptionrev = document.createElement("option");
                                    var myOption2rev = document.createElement("option");
                                    myOptionrev.text = 'T > ' + partRight;
                                    myOption2rev.text = 'T > ' + partRight;
                                    compAselect.add(myOptionrev);
                                    compBselect.add(myOption2rev);
                                }*/
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
                                            } else {

                                            }
                                        }
                                    });
                                });
                                if (somearr.length !== 0) {
                                    //alert(names[el] + " " + el);
                                    dict[namesarr[el]] = somearr;
                                }
                            }

                            length = compAselect.options.length;
                            for (k = length - 1; k > 0; k--) {
                                compAselect.options[k] = null;
                            }

                            lengthB = compBselect.options.length;
                            for (k = lengthB - 1; k > 0; k--) {
                                compBselect.options[k] = null;
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
                    } else {
                        obj.style.borderColor = "red";
                    }
                }
            });
        }
    }
}