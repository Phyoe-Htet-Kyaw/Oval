$(function(){
    $("#fileupload").change(function(event){
        var x = URL.createObjectURL(event.target.files[0]);
        console.log(x);
        $("#img-preview").css("backgroundImage", `url(${x})`);
    })
})

var ProfilePic = {
    main: function(event){
        event.preventDefault();
        var fd = new FormData();
        var files = $('#fileupload')[0].files;

        var upload_profie_picture_error = document.querySelector("#upload-profie-picture-error");
        upload_profie_picture_error.innerText = "";

        if(files.length > 0 ){
            fd.append('file',files[0]);
            var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            $.ajax({
                url: 'http://localhost:8000/uploading_profile_picture/',
                type: 'POST',
                data: fd,
                contentType: false,
                processData: false,
                headers: {
                    'X-CSRFToken': csrftoken
                },
                success: function(response){
                    console.log(response);
                    if(response.status == 1){
                        location.href = "http://localhost:8000/upload_cover_photo_view/";
                    }else if(response.status == 0){
                        general_error.innerText = response.message;
                    }
                },
                error: function(jqXHR, textStatus, errorThrown) {
                    console.log(textStatus, errorThrown);
                }
            })
        }
        else{
            upload_profie_picture_error.innerText = "Please choose profile picture!";
        }
    }
}

$("#upload-profie-picture-form").submit(ProfilePic.main);