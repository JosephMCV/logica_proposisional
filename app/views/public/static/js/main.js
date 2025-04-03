let counter = 0;

function getButton(counter) {
    if (counter > 2) {
        return `
            <button type="button" class="button_close col-7" onclick="removeFieldGroup(${counter})">
                <span class="X_close"></span>
                <span class="Y_close"></span>
                <div class="close"></div>
            </button>
        `;
    } else {
        return `<div class="col-7"></div>`;
    }
}

function addFieldGroup() {
    counter++;

    const container = document.getElementById("fieldsContainer");

    // container.innerHTML = `
        
    //     ${getButton(counter)}
    // `;

    container.appendChild(fieldGroup);
}

function removeFieldGroup(id) {
    const fieldGroup = document.querySelector(`.fields[data-id='${id}']`);
    if (fieldGroup) {
        fieldGroup.remove();
    }
}

addFieldGroup();
addFieldGroup();

function getInputValue(field_name) {
    const input = document.getElementById(field_name);
    return input ? input.value : "";  // Si no existe, retorna una cadena vacía
}

function submitData() {
    const formData = {
        variable_type: getInputValue("variable_type"),
        v1_name: getInputValue("v1_name"),
        v2_name: getInputValue("v2_name"),
        value_type: getInputValue("value_type"),
        val1_content: parseInt(getInputValue("val1_content")) || 0,
        val2_content: parseInt(getInputValue("val2_content")) || 0,
        restrictions: {}  // 🔥 Corregido para coincidir con FastAPI
    };

    for (let index = 1; index <= counter; index++) {
        formData.restrictions[`rest_name_${index}`] = getInputValue(`rest_name_${index}`);
        formData.restrictions[`rest_1_${index}`] = parseInt(getInputValue(`rest_1_${index}`)) || 0;  
        formData.restrictions[`rest_2_${index}`] = parseInt(getInputValue(`rest_2_${index}`)) || 0;  
        formData.restrictions[`rest_type_${index}`] = getInputValue(`rest_type_${index}`);
        formData.restrictions[`disp_${index}`] = parseInt(getInputValue(`disp_${index}`)) || 0;
    }

    fetch("http://localhost:8000/form-data", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => console.log("Éxito:", data))
    .catch(error => console.error("Error:", error));
}


document.addEventListener("DOMContentLoaded", function() {
    console.log("DOM completamente cargado y listo 🚀");
});
