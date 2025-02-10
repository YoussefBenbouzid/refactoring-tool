// Funzione per validare URL ed estrarre owner e repo
function validaEdEstrai(url_repository) {
    const githubRepoRegex = /^https?:\/\/github\.com\/([\w-]+)\/([\w-]+)(\/.*)?$/;
    const match = url_repository.match(githubRepoRegex);

    if (match) {
        return {
            valido: true,
            owner: match[1],
            repo: match[2]
        };
    } else {
        return { valido: false };
    }
}

// Funzione per inviare dati dell'URL del repository inserito nella textarea
function inviaDatiUrl() {
    var url_repository = document.getElementById('url_repository').value.trim();

    // Verifica validità dell'URL del repository ed estrazione di owner e repo
    const risultato = validaEdEstrai(url_repository);

    if (!risultato.valido) {
        alert("Inserisci un URL valido di un repository GitHub.");
        return;
    }

    // Invio di owner e repo estratti dall'URL del repository
    fetch('http://127.0.0.1:8000/repository', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
            "owner": risultato.owner, 
            "repo": risultato.repo 
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('risposta').value = data.risposta;
    });
}

// Funzione per cancellare l'URL del repository inserito nella textarea
function cancellaUrl() {
    document.getElementById('url_repository').value = '';
}

// Funzione per inviare snippet inseriti nella textarea
function inviaSnippet() {
    var codice = document.getElementById('snippet').value;

    fetch('http://127.0.0.1:8000/snippet', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ "codice": codice })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('risposta').value = data.risposta;
    });
}

// Funzione per cancellare snippet inseriti nella textarea
function cancellaSnippet() {
    document.getElementById('snippet').value = '';
}

// Selezione drop-area e file
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
    event.preventDefault(); // Prevenzione del comportamento di default
    dropArea.style.backgroundColor = ''; // Ripristino colore

    const files = event.dataTransfer.files; // Ottenimento dei file rilasciati
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
        // Implementare logica per inviare file a server
        // Implementare logica per inviare file a server
        // Implementare logica per inviare file a server
    } else {
        alert('Seleziona almeno un file.');
    }
}

// Funzione per cancellare file selezionati
function cancellaFile() {
    fileInput.value = '';
}

// Funzione per avviare la valutazione
function valuta() {
    fetch('http://127.0.0.1:8000/valuta', {
        method: 'POST'
    })
}

// Funzione reset per cancellare file, snippet e output e svuotare le cartelle
function reset() {
    var domanda = confirm("Confermi di voler eliminare tutti i dati?");
        if (domanda === true) {
            fetch('http://127.0.0.1:8000/reset', {
                method: 'POST'
            })
            cancellaFile();
            cancellaSnippet();
            cancellaUrl();
            document.getElementById('output').value = ''
        }
}