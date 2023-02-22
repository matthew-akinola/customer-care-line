const button = document.getElementById('location');
button.addEventListener("click", () =>{
    if(navigator.geolocation){ //if browser supports geolocation api
        //geolocation.getCurrentPostion method is used to get current postion of the user
        //it takes three params success, error, options.
        //callback function will call else error callback will call
        navigator.geolocation.getCurrentPosition(onSuccess);

    }else{
        button.innerText = "Your browser not support";
    }
})

function onSuccess(postion){
    let {latitude, longitude} = postion.coords;
    fetch(`https://api.opencagedata.com/geocode/v1/json?q=${latitude}+${longitude}&key=642f10acdb4c45f59a7c69e02e1de305`)
    //https://api.opencagedata.com/geocode/v1/json?q=LAT+LNG&key=642f10acdb4c45f59a7c69e02e1de305
    .then(response => (response.json()).then(result =>{

        let allDetails = result.results[0].components;
        let {city,country} = allDetails;
        button.innerText = `${city}, ${country}`;
        console.log(city, country)
        window.location.href = `helpline?city=${city}&country=${country}`
        // $.ajax({
        //     type: "GET",
        //     url: '/helpline',
        //     data: {
        //          "city":city,
        //           "country":country
        //         },
        //     success: function (data) {
        //         // any process in data
        //         window.location.href = `/helpline?city=${city}&country=${country}`
        //     },
        //     failure: function () {
        //         alert("failure");
        //     }
        // });
    }))
        
  
}
