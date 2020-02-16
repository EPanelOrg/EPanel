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
            $("#pName").html("$ " + data['name'])
            $("#uName").html("$ " + data['user'])
            $("#pLastName").html("$ " + data['lastName'])
            $("#pBirhDate").html("$ " + data['BDate'])
            $("#pcredit").html("$ " + data['credit'])
            $("#pEmail").html("$ " + data['email'])
            $("#pCitizenNo").html("$ " + data['CitizenshipNo'])
        }
    })
    ;
}
function sentProfileAjax() {

    $.ajax
    ({
        type: "POST",
        url: "http://127.0.0.1:8000/profile/",
        data: JSON.stringify({
                    uName : uName
                    Name : Name
                    LastName :LastName
                    BDate : BDate
                    PhoneNumber : PhoneNumber
                    EmailAddress : EmailAddress
                    CitizenshipNo : CitizenshipNo
                    UserName: UserName,
                    password: password,

                }),
//        crossDomain: false, //???
        headers: {
            "Authorization": "Bearer " + localStorage.token
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        success: function (data, status) {
            $("#profile").html("$ " + data['profileData'])
        }
    }).done(function (data) {
          if (data.result === 1) {
              alert("edit successfully");
              $(location).attr('href', "dashboard"); //????

          } else {
              alert("duplicate username!");
              $("#register-error").textContent = "duplicate username !";
          }

      });