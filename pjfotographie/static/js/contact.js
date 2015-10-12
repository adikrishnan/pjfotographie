function validateField(field, regex){
    var pattern = new RegExp(regex);
    if (!pattern.test($("#"+field).val())) {
        return false;
    } else {
        return true;
    };
}

function displayMessage(message){
    $("#notify").removeClass("uk-hidden");
    $("#notify").text(message);
}

function enableSubmit(){
    $("#notify").addClass("uk-hidden");
    $("#notify").text("");
    valid_name = validateField("name", "^[a-zA-Z. ]+$");
    valid_phone = validateField("phone", "^[0-9]{10}$");
    valid_email = validateField("email", "^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$");
    if (valid_name && valid_phone && valid_email) {
        $("#submit").prop("disabled", false);
    };
}

$(document).ready(function(){
    $("#submit").prop("disabled", true)
    $("#name").focusout(function(){
        valid_name = validateField("name", "^[a-zA-Z. ]+$");
        if (!valid_name) {
            displayMessage("Invalid characters in the name field. You can only use A to Z and .");
        } else {
            enableSubmit();
        }
    });
    $("#phone").focusout(function(){
        valid_phone = validateField("phone", "^[0-9]{10}$");
        if (!valid_phone) {
            displayMessage("Please enter 10 digit phone number.");
        } else {
            enableSubmit();
        }
    });
    $("#email").focusout(function(){
        valid_email = validateField("email", "^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$");
        if (!valid_email) {
            displayMessage("Invalid email address. Your email must be of the form abc@xyz.com");
        } else {
            enableSubmit();
        }
    });
});