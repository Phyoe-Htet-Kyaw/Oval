$(function(){
    $("#fileupload").change(function(event){
        var x = URL.createObjectURL(event.target.files[0]);
        console.log(x);
        $("#img-preview").css("backgroundImage", `url(${x})`);
    })
})

var CoverPhoto = {
    main: function(event){
        event.preventDefault();
        var fd = new FormData();
        var files = $('#fileupload')[0].files;

        var upload_cover_photo_error = document.querySelector("#upload-cover-photo-error");
        upload_cover_photo_error.innerText = "";

        if(files.length > 0 ){
            fd.append('file',files[0]);
            var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            $.ajax({
                url: 'http://localhost:8000/uploading_cover_photo/',
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
                        location.href = "http://localhost:8000/";
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
            upload_cover_photo_error.innerText = "Please choose profile picture!";
        }
    }
}

$("#upload-cover-photo-form").submit(CoverPhoto.main);