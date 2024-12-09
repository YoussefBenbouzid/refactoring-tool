// Selezione drop-area e files
const dropArea = document.getElementById('drop-area');
const fileInput = document.getElementById('files');

// Quando si verifica il drag (dragover)
dropArea.addEventListener('dragover', (event) => {
    event.preventDefault(); // Prevenzione comportamento di default
    dropArea.style.backgroundColor = '#F0F0F0'; // Cambio colore drop-area
});

// Quando il drag termina (dragleave)
dropArea.addEventListener('dragleave', () => {
    dropArea.style.backgroundColor = ''; // Ripristino colore drop-area
});

// Quando i file vengono rilasciati nell'area di drop (drop)
dropArea.addEventListener('drop', (event) => {
    event.preventDefault(); // Prevenzione comportamento di default
    dropArea.style.backgroundColor = ''; // Ripristino colore

    const files = event.dataTransfer.files; // Ottenimento file rilasciati
    if (files.length > 0) {
        fileInput.files = files; // Aggiunta file all'input
    }
});

// Gestione clic sull'input per selezionare file
fileInput.addEventListener('change', (event) => {
    const selectedFiles = event.target.files;
});

// Funzione per inviare file selezionati
function inviaFile() {
    const files = fileInput.files;
    if (files.length > 0) {
        console.log('File inviati:', files); // Per testare, da cancellare poi
        // Implementare logica per inviare file a server
    } else {
        alert('Seleziona almeno un file.');
    }
}

// Funzione per cancellare i file selezionati
function cancellaFile() {
    fileInput.value = '';
}

// Funzione per inviare lo snippet inserito nella textarea
function inviaSnippet() {
    var testo = document.getElementById('snippet').value;
}

// Funzione per cancellare lo snippet nella textarea
function cancellaSnippet() {
    document.getElementById('snippet').value = ''; 
}

// Funzione reset
function reset() {
    var domanda = confirm("Confermi di voler eliminare tutti i dati?");
        if (domanda === true) {
            cancellaFile();
            cancellaSnippet();
            // Implementare cancellazione output
        }
}