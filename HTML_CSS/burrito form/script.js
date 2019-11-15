function validateFirstName() {
    var str = document.getElementById("first_name").value;
    var digits = /[0-9]/g;
    var result  = str.match(digits);

    // document.getElementById("demo").innerHTML = result

    if (result == undefined || result.length == 0) {
        document.getElementById("demo").innerHTML = "valid name!";
    } else {
        document.getElementById("demo").innerHTML = "invalid!";
        alert("Invalid first name!")
    }
}

// function 

// document.addEventListener('DOMContentLoaded', function() {
//     var elems = document.querySelectorAll('.modal');
//     var instances = M.Modal.init(elems, options);
//   });

//   // Or with jQuery

//   $(document).ready(function(){
//     $('.modal').modal();
//   });
        


