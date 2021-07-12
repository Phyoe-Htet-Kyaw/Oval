$(function(){
    $("#profile-fileupload").change(function(event){
        var x = URL.createObjectURL(event.target.files[0]);
        console.log(x);
        $("#profile-preview").css({"backgroundImage": `url(${x})`, "border": "none"});
    })

    $("#cover-fileupload").change(function(event){
        var x = URL.createObjectURL(event.target.files[0]);
        console.log(x);
        $("#cover-preview").css({"backgroundImage": `url(${x})`, "border": "none"});
    })

    $("#university_update #country").change(function(){
        var template = "";
        var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        $.ajax({
            url: 'http://localhost:8000/api/get_city_list/',
            type: 'POST',
            data: {
                country_id: $(this).val(),
            },
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function(response){
                if(response.status == 1){
                    response.data.forEach(function(item){
                        template += `<option value="${item[0]}">${item[1]}</option>`;
                    })
                    $("#university_update #city").html(template);
                }else if(response.status == 0){
                    console.log(response.message);
                }
            },
            error: function(jqXHR, textStatus, errorThrown) {
                console.log(textStatus, errorThrown);
            }
        })
    })

    $("#university_update").submit(function(event){
        event.preventDefault();

        var name = $("#university_update #name").val();
        var email = $("#university_update #email").val();
        var phone = $("#university_update #phone").val();
        var uni = $("#university_update #uni").val();
        var address = $("#university_update #address").val();
        var country = $("#university_update #country").val();
        var city = $("#university_update #city").val();
        var map = $("#university_update #map").val();
        var about = $("#university_update .about").val();

        var profile_file = $('#university_update #profile-fileupload')[0].files;
        var cover_file = $('#university_update #cover-fileupload')[0].files;

        if(profile_file.length == 0 ){
            profile_file[0] = "";
        }

        if(cover_file.length == 0 ){
            cover_file[0] = "";
        }

        if(country == "null"){
            country = "";
        }

        if(city == null){
            city = "";
        }

        console.log(country, city);

        var fd = new FormData();
        fd.append('profile',profile_file[0]);
        fd.append('cover',cover_file[0]);
        fd.append('name',name);
        fd.append('email',email);
        fd.append('phone',phone);
        fd.append('address',address);
        fd.append('country',country);
        fd.append('city',city);
        fd.append('map',map);
        fd.append('about',about);
        fd.append('uni',atob(uni));

        var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        $.ajax({
            url: 'http://localhost:8000/university_update_process/',
            type: 'POST',
            data: fd,
            contentType: false,
            processData: false,
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function(response){
                if(response.status == 1){
                    location.href = `http://localhost:8000/university_detail/${uni}/`
                }else if(response.status == 0){
                    console.log(response.message)
                }
            },
            error: function(jqXHR, textStatus, errorThrown) {
                console.log(textStatus, errorThrown);
            }
        })
    })
})