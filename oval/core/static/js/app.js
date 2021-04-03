var Auth = {
    registerSubmit: function(event){
        event.preventDefault();

        var username = document.querySelector("#username");
        var email = document.querySelector("#email");
        var password = document.querySelector("#password");
        var con_password = document.querySelector("#con-password");

        var username_error = document.querySelector("#username-error");
        var email_error = document.querySelector("#email-error");
        var password_error = document.querySelector("#password-error");
        var con_password_error = document.querySelector("#con-password-error");
        var general_error = document.querySelector("#general-error");

        username_error.innerText = "";
        email_error.innerText = "";
        password_error.innerText = "";
        con_password_error.innerText = "";
        general_error.innerText = "";

        if(username.value == ""){
            username_error.innerText = "Please enter your username!";
        }else{
            if(email.value == ""){
                email_error.innerText = "Please enter your email!";
            }else{
                if(password.value == ""){
                    password_error.innerText = "Please enter your password!";
                }else{
                    if(con_password.value == ""){
                        con_password_error.innerText = "Please enter your confirm password!";
                    }else{
                        if(password.value.length < 8){
                            password_error.innerText = "Please enter your password length more than 8!";
                        }else{
                            if(con_password.value.length < 8){
                                con_password_error.innerText = "Please enter your password length more than 8!";
                            }else{
                                if(password.value != con_password.value){
                                    password_error.innerText = "Password and Confirm Passoword didn't match!";
                                }else{
                                    var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
                                    $.ajax({
                                        url: 'http://localhost:8000/registering/',
                                        type: 'POST',
                                        data: {
                                            username: username.value,
                                            email: email.value,
                                            password: password.value,
                                        },
                                        headers: {
                                            'X-CSRFToken': csrftoken
                                        },
                                        success: function(response){
                                            console.log(response);
                                            if(response.status == 1){
                                                location.href = "http://localhost:8000/verify_email/";
                                            }else if(response.status == 0){
                                                general_error.innerText = response.message;
                                            }
                                        },
                                        error: function(jqXHR, textStatus, errorThrown) {
                                            console.log(textStatus, errorThrown);
                                        }
                                    })
                                }
                            }
                        }
                    }
                }
            }
        }
    },

    loginSubmit: function(event){
        event.preventDefault();

        var email = document.querySelector("#email");
        var password = document.querySelector("#password");

        var email_error = document.querySelector("#email-error");
        var password_error = document.querySelector("#password-error");
        var general_error = document.querySelector("#general-error");

        email_error.innerText = "";
        password_error.innerText = "";
        general_error.innerText = "";

        if(email.value == ""){
            email_error.innerText = "Please enter your email!";
        }else{
            if(password.value == ""){
                password_error.innerText = "Please enter your password!";
            }else{
                var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
                $.ajax({
                    url: 'http://localhost:8000/logining/',
                    type: 'POST',
                    data: {
                        email: email.value,
                        password: password.value,
                    },
                    headers: {
                        'X-CSRFToken': csrftoken
                    },
                    success: function(response){
                        console.log(response);
                        if(response.status == 1){
                            location.href = "http://localhost:8000";
                        }else if(response.status == 0){
                            general_error.innerText = response.message;
                        }
                    },
                    error: function(jqXHR, textStatus, errorThrown) {
                        console.log(textStatus, errorThrown);
                    }
                })
            }
        }
    }
}

if(document.querySelector("#register-form") != null){ document.querySelector("#register-form").addEventListener("submit", Auth.registerSubmit); }
if(document.querySelector("#login-form") != null){ document.querySelector("#login-form").addEventListener("submit", Auth.loginSubmit); }

