document.addEventListener("DOMContentLoaded", function () {
    fetch('/api/activities')
        .then(response => response.json())
        .then(data => {
            let activities = data.activities;
            let activitiesContainer = document.getElementById("activities-container");


            for (let day in activities) {
                activities[day].array.forEach(activity => {
                    // Crea un nuevo div para cada tarjeta de actividad
                    let cardItem = document.createElement("div");
                    cardItem.classList.add('card-item', 'card-${day}'); //Item asignado al dia que pertenece

                    // Crea el contenedor para el título de la actividad
                    let activityTitle = document.createElement('div');
                    activityTitle.classList.add('activity-title', 'pt-4');
                    let title = document.createElement('h5');
                    title.textContent = activity.title;
                    activityTitle.appendChild(title); // Agregamos el h5 dentro de activity-title

                    // Crea el contenedor para el cuerpo de la actividad
                    let cardBody = document.createElement('div');
                    cardBody.classList.add('card-body');
                    let description = document.createElement('p');
                    description.textContent = activity.description;
                    cardBody.appendChild(description); // Agregamos el p  dentro del cuerpo

                    // Agrega el título y el cuerpo a la tarjeta
                    cardItem.appendChild(activityTitle);
                    cardItem.appendChild(cardBody);

                    // Agrega la tarjeta completa al contenedor principal
                    //activitiesContainer.appendChild(cardItem);
                    window.alert("hOLS");

                });
            }
        })
});
