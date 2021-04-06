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
})