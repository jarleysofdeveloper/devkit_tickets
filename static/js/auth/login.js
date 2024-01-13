$(document).ready(()=>{
    $("#submitLogin").click(()=>{
        const user = $("#username").val();
        const password = $("#password").val();

        if(user === "" || password === "" ){
            console.log("los datos estan vacios");
        }else{
            try {
                $.ajax({
                    type: "POST",
                    url: "http://192.168.18.5:5000/login",
                    data: {username: user, password: password},
                    success: function (response) {
                        console.log(response);
                    }
                });
            } catch (error) {
                console.log(error);
            }
        }

    });
});