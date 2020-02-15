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
//            $("#pName").html("$ " + data['profileData'])
//            $("#pLastName").html("$ " + data['profileData'])
//            $("#pBirhDate").html("$ " + data['profileData'])
//            $("#pGender").html("$ " + data['profileData'])
//            $("#pPhoenNum").html("$ " + data['profileData'])
//            $("#pEmail").html("$ " + data['profileData'])
//            $("#pCitizenNo").html("$ " + data['profileData'])
//            $("#profile").html("$ " + data['profileData'])

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
                    Name : Name
                    LastName :LastName
                    BDate : BDate
//                    Gender
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