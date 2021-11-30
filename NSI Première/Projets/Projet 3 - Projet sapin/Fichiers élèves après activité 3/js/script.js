function Bouton_clic() {
    console.log("Bouton " + event.target.value + " cliqué !");
    var request = new XMLHttpRequest(); // Initialisation
    request.open("GET", "/" + event.target.value);
    request.send();
}

/*
function Bouton_ascendant() {
    console.log("Bouton ascendant cliqué !");
    var request = new XMLHttpRequest(); // Initialisation
    request.open("GET", "/Ascendant"); // Création de la requête GET
    request.send(); // Envoi de la requête GET au serveur
}


function Bouton_descendant() {
    console.log("Bouton descendant cliqué !");
    var request = new XMLHttpRequest(); // Initialisation
    request.open("GET", "/Descendant"); // Création de la requête GET
    request.send(); //Envoi de la requête GET au serveur
}

function Bouton_alterne() {
    console.log("Bouton alterné cliqué !");
    var request = new XMLHttpRequest(); // Initialisation
    request.open("GET", "/Alterné"); // Création de la requête GET
    request.send(); //Envoi de la requête GET au serveur
}

function Bouton_aleatoire() {
    console.log("Bouton aléatoire cliqué !");
    var request = new XMLHttpRequest(); // Initialisation
    request.open("GET", "/Aléatoire"); // Création de la requête GET
    request.send(); //Envoi de la requête GET au serveur
}
*/