ClassicEditor
        .create( document.querySelector( '#editor' ) )
        .catch( error => {
            console.error( error );
        } );

function registerSubmit(event){
    event.preventDefault();

    var username = document.querySelector("#username");
    var email = document.querySelector("#email");
    var password = document.querySelector("#password");
    var con_password = document.querySelector("#con-password");

    var username_error = document.querySelector("#username-error");
    var email_error = document.querySelector("#email-error");
    var password_error = document.querySelector("#password-error");
    var con_password_error = document.querySelector("#con-password-error");

    username_error.innerText = "";
    email_error.innerText = "";
    password_error.innerText = "";
    con_password_error.innerText = "";

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
                                        if(response == 1){
                                            location.href = "http://localhost:8000";
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
}

document.querySelector("#register-form").addEventListener("submit", registerSubmit)