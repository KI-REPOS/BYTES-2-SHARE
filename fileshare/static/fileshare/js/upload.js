document.getElementById('upload-form').addEventListener('submit', function(e) {
    let fileInput = document.getElementById('fileInput');
    if (!fileInput.files.length) {
        alert("Please choose a file first.");
        e.preventDefault();
        return;
    }

    let progressBar = document.getElementById('progress-bar');
    let xhr = new XMLHttpRequest();
    let formData = new FormData(this);

    xhr.upload.addEventListener('progress', function(e) {
        if (e.lengthComputable) {
            let percent = Math.round((e.loaded / e.total) * 100);
            progressBar.style.width = percent + "%";
            progressBar.textContent = percent + "%";
        }
    });

    xhr.open('POST', window.location.href, true);
    xhr.setRequestHeader('X-CSRFToken', document.querySelector('[name=csrfmiddlewaretoken]').value);
    xhr.send(formData);

    e.preventDefault();
});
