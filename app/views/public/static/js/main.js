let counter = 0;

const letras = [];
let letra = 'p'.charCodeAt(0);

while (String.fromCharCode(letra) !== 'o') {
    letras.push(String.fromCharCode(letra));
    letra = letra === 'z'.charCodeAt(0) ? 'a'.charCodeAt(0) : letra + 1;
}

letras.push('o');

function toggleNegacion(button) {
    let h4 = button.nextElementSibling;
    if (h4.textContent.startsWith("¬")) {
        h4.textContent = h4.textContent.slice(1);
    } else {
        h4.textContent = "¬" + h4.textContent;
    }
}

function addFieldGroup() {
    const container = document.getElementById("fieldsContainer");

    // Quitar botón de borrar del anterior último (si existe)
    const lastField = container.lastElementChild;
    if (lastField) {
        const btn = lastField.querySelector(".button_close");
        if (btn) btn.remove();
    }

    const fieldGroup = document.createElement("div");
    fieldGroup.className = "field";
    fieldGroup.dataset.id = counter;

    const letraActual = letras[counter];

    fieldGroup.innerHTML = `
        <div style="margin-bottom: 6px; width: 30%; display: flex; gap:10px; justify-content:center;">
            <button onclick="toggleNegacion(this)">
                <span>Negar</span>
            </button>
            <h4 id="textoH4">${letraActual}</h4>
        </div>
        <div class="input-box">
            <input required placeholder="Ingrese el valor" class="input" name="${letraActual}" id="${letraActual}" type="text">
        </div>
        <div style="width: 30%;">
            <button type="button" class="button_close col-7" onclick="removeFieldGroup(${counter})">
                <span class="X_close"></span>
                <span class="Y_close"></span>
                <div class="close"></div>
            </button>
        </div>
    `;

    container.appendChild(fieldGroup);
    counter++;
}

function removeFieldGroup(id) {
    const container = document.getElementById("fieldsContainer");
    const fieldGroup = container.querySelector(`.field[data-id='${id}']`);
    if (fieldGroup) {
        fieldGroup.remove();
    }

    // Aplicar botón de eliminar al nuevo último (si hay al menos 1)
    const allFields = container.querySelectorAll(".field");
    const last = allFields[allFields.length - 1];
    if (last) {
        const lastId = last.dataset.id;
        const btnDiv = document.createElement("div");
        btnDiv.style.width = "30%";
        btnDiv.innerHTML = `
            <button type="button" class="button_close col-7" onclick="removeFieldGroup(${lastId})">
                <span class="X_close"></span>
                <span class="Y_close"></span>
                <div class="close"></div>
            </button>
        `;
        last.appendChild(btnDiv);
    }
}

function getInputValue(field_name) {
    const input = document.getElementById(field_name);
    return input ? input.value : "";
}

function recolectarValores() {
    const campos = document.querySelectorAll("#fieldsContainer .field");
    const resultado = {};

    campos.forEach(field => {
        const h4 = field.querySelector("h4");
        const input = field.querySelector("input");
        if (!h4 || !input) return;

        let clave = h4.textContent.trim();
        resultado[clave] = input.value;
    });

    return resultado;
}

function submitData() {
    const textarea = document.getElementById("text");
    const expressions = recolectarValores();

    // Validación: mínimo 2 expresiones
    if (Object.keys(expressions).length < 2) {
        alert("Debes ingresar al menos dos expresiones.");
        return;
    }

    const request = {
        main_text: textarea.value,
        expressions_dict: expressions
    };

    // Enviar usando fetch
    fetch("http://localhost:8000/form-data", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(request)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Error en la respuesta del servidor");
        }
        return response.json(); // o .text() si esperás texto
    })
    .then(data => {
        alert("Respuesta del servidor: " + JSON.stringify(data));
    })
    .catch(error => {
        console.error("Error al enviar los datos:", error);
        alert("Hubo un error al enviar los datos. Revisa la consola para más detalles.");
    });
}

document.addEventListener("DOMContentLoaded", function () {
    console.log("DOM completamente cargado y listo 🚀");
    addFieldGroup(); // arranca con al menos uno
});
