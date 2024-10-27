document.addEventListener("DOMContentLoaded", function () {
    fetch('/api/activities')
        .then(response => {
            if (!response.ok) {
                throw new Error('Response was not ok!');
            }
            return response.json();
        })
        .then(data => {
            let activities = data.activities;
            let activitiesContainer = document.getElementById("activities-container");

            // Itera sobre las actividades
            for (let day in activities) {
                // Verifica si activities[day] es un array
                if (Array.isArray(activities[day])) {
                    activities[day].forEach(activity => {
                        console.log(`Procesando actividad: ${activity.title}`); // Muestra la actividad que se está procesando

                        // Crea un nuevo div para cada tarjeta de actividad
                        let cardItem = document.createElement("div");
                        cardItem.classList.add('card-item', `card-${day}`); // Usar comillas invertidas para interpolación

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
                        cardBody.appendChild(description); // Agregamos el p dentro del cuerpo

                        // Agrega el título y el cuerpo a la tarjeta
                        cardItem.appendChild(activityTitle);
                        cardItem.appendChild(cardBody);

                        // Agrega la tarjeta completa al contenedor principal
                        activitiesContainer.appendChild(cardItem);
                    });
                } else {
                    console.warn(`No se encontró un array para el día: ${day}`);
                    console.log(`Contenido de activities[${day}]:`, activities[day]); // Muestra qué hay en activities[day]
                }
            }
        })
        .catch(error => {
            console.error('Hubo un problema con la solicitud Fetch:', error);
        });
});