$(function () {
    loadProfileAjax();

    $("#submit").click(sentProfileAjax)



});

function loadProfileAjax() {

    $.ajax
    ({
        type: "GET",
        url: "http://127.0.0.1:8000/profile-api/",
        dataType: 'json',
        headers: {
            "Authorization": "Bearer " + "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgxODgwMTgwLCJqdGkiOiI5Yjg2MDNiYzQ0Mjc0OTM0YjQzM2Y0NDFmMjc4YmUyYSIsInVzZXJfaWQiOjF9.p5F8fZvDKOCtq5Kf7ULWM6cXhr-jrhkJVWN6LnPWvL8" //localStorage.token
        },
        success: function (data, status) {
            $("#pName").html(data['profileData']['name'])
            $("#pLastName").html(data['profileData']['lastName'])
            $("#pBirhDate").html(data['profileData']['BDate'])
            $("#pcredit").html(data['profileData']['credit'])
            $("#pEmail").html(data['profileData']['email'])
            $("#pCitizenNo").html(data['profileData']['CitizenshipNo'])
        }
    })
    ;
}

function sentProfileAjax() {
    var Name;
    var LastName;
    var BDate;
    var EmailAddress;
    var CitizenshipNo;
    var credit

    Name =  $("#Name").val().toString();
    LastName =  $("#LastName").val().toString();
    BDate =  $("#BDate").val().toString();
    EmailAddress =  $("#EmailAddress").val().toString();
    CitizenshipNo =  $("#CitizenshipNo").val().toString();
    credit =  $("#credit").val().toString();

    $.ajax
    ({
        type: "PUT",
        url: "http://127.0.0.1:8000/profile-api/",
        data: JSON.stringify({
                    name : Name,
                    lastName :LastName,
                    BDate : BDate,
                    email : EmailAddress,
                    CitizenshipNo : CitizenshipNo
                    credit = credit
                }),
//        crossDomain: false, //???
        headers: {
            "Authorization": "Bearer " + "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgxODgwMTgwLCJqdGkiOiI5Yjg2MDNiYzQ0Mjc0OTM0YjQzM2Y0NDFmMjc4YmUyYSIsInVzZXJfaWQiOjF9.p5F8fZvDKOCtq5Kf7ULWM6cXhr-jrhkJVWN6LnPWvL8",
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        success: function(result) {
                        alert("profile updated!");
      }
     });
}


