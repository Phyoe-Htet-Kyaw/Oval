var Verify = {
    process: function(event){
        event.preventDefault();
        var verify_code = document.querySelector("#verify_code");
        var verify_code_error = document.querySelector("#verify-code-error");

        verify_code_error.innerText = "";

        if(verify_code.value == ""){
            verify_code_error.innerText = "Please enter verify code!";
        }else{
            var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            $.ajax({
                url: 'http://localhost:8000/verifying/',
                type: 'POST',
                data: {
                    code: verify_code.value,
                },
                headers: {
                    'X-CSRFToken': csrftoken
                },
                success: function(response){
                    console.log(response);
                    if(response.status == 1){
                        location.href = "http://localhost:8000/upload_profile_picture/";
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

$("#verify-form").submit(Verify.process);