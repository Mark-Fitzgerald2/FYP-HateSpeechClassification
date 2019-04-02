var data =
    {
        "hate": "-",
        "percentage": "-%"
    }

var textOutput = document.getElementById('textOutput')
textOutput.innerHTML = data["hate"];
var textProb = document.getElementById('textProb')
textProb.innerHTML = data["percentage"];

var textOutput = document.getElementById('twitterIdOutput');
textOutput.innerHTML = data["hate"];
var textProb = document.getElementById('IDProb');
textProb.innerHTML = data["percentage"];

classifyText = null;
classifyTwitterHandle = null;

var pieData = [360];
var labels = ["Waiting to classify"];
var colorArray1 = ["#F7464A", "#46BFBD", "#FDB45C", "#949FB1", "#4D5360"];
var hoverArray1 = ["#FF5A5E", "#5AD3D1", "#FFC870", "#A8B3C5", "#616774"];
var colorArray2 = ["#0066ff", "#9933ff", "#66ff66", "#ff9933", "#00ffff"];
var hoverArray2 = ["#6699ff", "#9966ff", "#99ff99", "#ff9966", "#ccffff"];
var ctxP = document.getElementById("pieChart").getContext('2d');
var dataset = {
    labels: labels,
    datasets: [{
        data: pieData,
        backgroundColor: colorArray1,
        hoverBackgroundColor: hoverArray1
    }]
};
var myPieChartText = new Chart(ctxP, {
    type: 'pie',
    data: dataset,
    options: {
        responsive: true
    }
});

ctxP = document.getElementById("pieChartTwitterAcc").getContext('2d');

dataset = {
    labels: labels,
    datasets: [{
        data: pieData,
        backgroundColor: colorArray2,
        hoverBackgroundColor: hoverArray2
    }]
};

var myPieChartTwitterAcc = new Chart(ctxP, {
    type: 'pie',
    data: dataset,
    options: {
        responsive: true
    }
});
//jquery
$(function() {

    function classT(){
        $(document).ready(function () {
            var text = $.trim($("#textToClassify").val());
            text = removeHTML(text);
            if (text != "") {
                $.blockUI({
                    css: {
                        border: 'none',
                        padding: '15px',
                        backgroundColor: '#000',
                        '-webkit-border-radius': '10px',
                        '-moz-border-radius': '10px',
                        opacity: .5,
                        color: '#fff'
                    }
                });
                postData('http://134.209.27.230/classifyText', {"text": text})
                    .then(data => removeMapping(data))
                    .catch(error => alertError(error));
            } else {
                var data =
                    {
                        "hate": "-",
                        "percentage": "-%"
                    }

                var textOutput = document.getElementById('textOutput')
                textOutput.innerHTML = data["hate"];
                var textProb = document.getElementById('textProb')
                textProb.innerHTML = data["percentage"];
                setupPieChart([360],["Waiting to classify"]);
                alert("Please enter a message to classify.");
            }
        });
    }
    function classTH() {
        $(document).ready(function () {
            var twitterId = $.trim($("#userId").val());
            twitterId = removeHTML(twitterId);
            var numTweets = $("#numTweets").find(":selected").text();
            if (twitterId != "" && numTweets != "Choose") {
                $.blockUI({
                    css: {
                        border: 'none',
                        padding: '15px',
                        backgroundColor: '#000',
                        '-webkit-border-radius': '10px',
                        '-moz-border-radius': '10px',
                        opacity: .5,
                        color: '#fff'
                    }
                });
                numTweets = parseInt(numTweets)
                postData('http://134.209.27.230/classifyTwitterAcc', {"twitterId": twitterId,"numTweets": numTweets})
                    .then(data => updateTwitterIdResults(data))
                    .catch(error => alertError(error));
            } else {
                var data =
                    {
                        "hate": "-",
                        "percentage": "-%"
                    }

                var textOutput = document.getElementById('twitterIdOutput');
                textOutput.innerHTML = data["hate"];
                var textProb = document.getElementById('IDProb');
                textProb.innerHTML = data["percentage"];
                setupPieChart([360],["Waiting to classify"]);
                alert("Please make sure that both fields are filled in.");
            }
        });
    }
    function removeHTML(text){
        var map = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#039;'
        };

        return text.replace(/[&<>"']/g, function(m) { return map[m]; });
    }
    function removeMapping(data){
        words = data["labels"];
        for(i=0;i<words.length;i++){
            words[i] = convertMapping(words[i]);
        }
        data["labels"] = words;
        updateTextResults(data);
    }
    function convertMapping(text){
        /*var map = {
            '&amp;': '&',
            '&lt;': '<',
            '&gt;': '>',
            '&quot;': '"',
            '&#039;': "'"
        };*/
        return text.replace(/&#039;/g,"'").replace(/&amp;/g,"&").replace(/&lt;/g,"<").replace(/&gt;/g,">").replace(/&quot;/g,'"');
        //return text.replace(/[&<>"']/g, function(m) { return map[m]; });
    }
    classifyText = classT;
    classifyTwitterHandle = classTH;
});

function postData(url = '', data = {}) {
    // Default options are marked with *
    return fetch(url, {
        method: "POST", // *GET, POST, PUT, DELETE, etc.
        mode: "cors", // no-cors, cors, *same-origin
        cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
        credentials: "same-origin", // include, *same-origin, omit
        headers: {
            "Content-Type": "application/json",
            // "Content-Type": "application/x-www-form-urlencoded",
        },
        redirect: "follow", // manual, *follow, error
        referrer: "no-referrer", // no-referrer, *client
        body: JSON.stringify(data), // body data type must match "Content-Type" header
    })
        .then(response => response.json()); // parses response to JSON
}

function updateTextResults(data) {
    $.unblockUI();
    var textOutput = document.getElementById('textOutput');
    textOutput.innerHTML = data["pred"];
    var textProb = document.getElementById('textProb');
    textProb.innerHTML = data["prob"];
    relocateTextRes();
    if(data["data"].length == 0) {
        setupPieChart([1], ["No words associated with hate"], "text");
    } else {
        setupPieChart(data["data"], data["labels"], "text");
    }
}

function updateTwitterIdResults(data) {
    $.unblockUI();
    var textOutput = document.getElementById('twitterIdOutput');
    textOutput.innerHTML = data["pred"];
    var textProb = document.getElementById('IDProb');
    textProb.innerHTML = data["prob"];
    relocateTHRes();
    setupPieChart(data["data"], data["labels"], "twitterAcc");
}

function alertError(error) {
    $.unblockUI();
    alert("An unexpected error with the server has occurred. Please try again. If the issue persists, please contact the developer.");
    console.log(error);
}

function relocateTHRes() {
    location.href = "#twitterHandleResults";
}

function relocateTextRes() {
    location.href = "#textResults";
}

function setupPieChart(data, labels, type){
    if(data != undefined && labels != undefined) {
        var pie;
        var color;
        var hover;
        if(type == "text"){
            pie = window.myPieChartText;
            color = window.colorArray1;
            hover = window.hoverArray1;
        } else {
            pie = window.myPieChartTwitterAcc;
            color = window.colorArray2;
            hover = window.hoverArray2;
        }
        var dataset = {
            labels: labels,
            datasets: [{
                data: data,
                backgroundColor: color,
                hoverBackgroundColor: hover
            }]
        };
        pie.data = dataset;
        pie.update();
    }
}