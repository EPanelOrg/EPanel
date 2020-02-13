$(function () {
    creditAjax();
    homesAjax();

    setInterval(function () {
        creditAjax()
        homesAjax()

    }, 10000)

});

function creditAjax() {

    $.ajax
    ({
        type: "GET",
        url: "http://127.0.0.1:8000/get-credit/",
        dataType: 'json',
        headers: {
            "Authorization": "Bearer " + " eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgxNTM5ODAzLCJqdGkiOiI4MGUzZWI3OWVjYmQ0NWU1ODU3YWZjZTQ1YzgxMjdkNSIsInVzZXJfaWQiOjF9.nNQP3iaHaqH2NXzCfAbt11LjC796F59K-zt3laR2wLg"
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
            "Authorization": "Bearer " + " eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgxNTM5ODAzLCJqdGkiOiI4MGUzZWI3OWVjYmQ0NWU1ODU3YWZjZTQ1YzgxMjdkNSIsInVzZXJfaWQiOjF9.nNQP3iaHaqH2NXzCfAbt11LjC796F59K-zt3laR2wLg"
        },
        success: function (data, status) {
            $("#homes").html(data['homes-count'])
        }
    })
    ;
}