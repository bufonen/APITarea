async function agregarUsuario(e) {
    try {
        e.preventDefault();
        const nombre = document.getElementById("nombre").value;
        const email = document.getElementById("email").value;
        
        const response = await fetch('/usuarios/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                Nombre: nombre,
                Email: email
            })
        });

        if (!response.ok) {
            throw new Error('Error al crear usuario');
        }

        document.getElementById("addForm").reset();
        window.location.reload();
    } catch (error) {
        console.error('Error:', error);
        alert('Error al crear usuario');
    }
}

async function actualizarUsuario(id) {
    const nombre = document.getElementById(`nombre-${id}`).value;
    const email = document.getElementById(`email-${id}`).value;
    await fetch(`/usuarios/${id}`, {
        method: 'PUT',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({Nombre: nombre, Email: email})
    });
    window.location.reload();
}

async function eliminarUsuario(id) {
    await fetch(`/usuarios/${id}`, {method: 'DELETE'});
    window.location.reload();
}

//agregar el event listener cuando el DOM esté cargado
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById("addForm");
    if (form) {
        form.addEventListener("submit", agregarUsuario);
    }
});
