$(function () {
    loadProfileAjax();

    setInterval(function () {
        profileAjax()

    }, 10000)

});

function loadProfileAjax() {

    $.ajax
    ({
        type: "GET",
        url: "http://127.0.0.1:8000/profile/",
        dataType: 'json',
        headers: {
            "Authorization": "Bearer " + localStorage.token
        },
        success: function (data, status) {
            $("#profile").html("$ " + data['profileData'])
        }
    })
    ;
}

$.ajax(
    {
       type: "POST",
        url: "register/",
        data: JSON.stringify({
            username: username,
            password: password,
            email: email

        }),
        crossDomain: false,
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    }).done(function (data) {
    if (data.result === 1) {
        alert("registered successfully");
        $(location).attr('href', "dashboard");

    } else {
        alert("duplicate username!");
        $("#register-error").textContent = "duplicate username !";
    }

});