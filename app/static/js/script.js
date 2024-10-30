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
                        cardItem.setAttribute("data-day", day);

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

            // Hide all activities cards at first
            const allCardsItems = document.querySelector(".card-item");

            if (allCardsItems) {
                allCardsItems.forEach(card => card.style.display = "none");
            }

            // Event listener
            const daysList = document.querySelectorAll(".days-list li");
            daysList.forEach(dayItem => {
                dayItem.addEventListener("click", function () {
                    const selectedDay = dayItem.getAttribute("data-day");

                    // Oculta todas las tarjetas primero
                    allCards.forEach(card => card.style.display = "none");

                    // Muestra las tarjetas correspondientes al día seleccionado
                    const dayCards = document.querySelectorAll(`.card-item[data-day="${selectedDay}"]`);
                    dayCards.forEach(card => card.style.display = "block");
                });
            });
        })
        .catch(error => {
            console.error('Hubo un problema con la solicitud Fetch:', error);
        });
});