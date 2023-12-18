let username;

document.getElementById("submit Button").onclick = function(){

    username = document.getElementById("NewUser").value;
    document.getElementById("Founder Name").innerHTML = username;
}