$(function () {
    creditAjax();
    homesAjax();

    setInterval(function () {
        creditAjax();
        homesAjax();

    }, 10000)

});

function creditAjax() {

    $.ajax
    ({
        type: "GET",
        url: "http://127.0.0.1:8000/get-credit/",
        dataType: 'json',
        headers: {
            "Authorization": "Bearer " + localStorage.token
        },
        success: function (data, status) {
            $("#credit").html("$ " + data['credit-amount'])
        }
    })
    ;
}

function homesAjax() {

    $.ajax
    ({
        type: "GET",
        url: "http://127.0.0.1:8000/get-homes/",
        dataType: 'json',
        headers: {
            "Authorization": "Bearer " + localStorage.token
        },
        success: function (data, status) {
            $("#homes").html(data['homes-count'])
        }
    })
    ;
}