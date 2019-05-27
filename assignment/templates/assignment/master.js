var _URL = window.URL || window.webkitURL;

function isSupportedBrowser() {
    return window.File && window.FileReader && window.FileList && window.Image;
}

function getSelectedFile() {
    var fileInput = document.getElementById("filePicker");
    var fileIsSelected = fileInput && fileInput.files && fileInput.files[0];
    if (fileIsSelected)
        return fileInput.files[0];
    else
        return false;

}
function isGoodImage(file) {
    var deferred = jQuery.Deferred();
    var image = new Image();

    image.onload = function() {
        // Check if image is bad/invalid
        if (this.width + this.height === 0) {
            this.onerror();
            return;
        }

        // Check the image resolution
        if (this.width >= 400 && this.height >= 400) {
            deferred.resolve(true);
        } else {
            alert("The image resolution is too low.");
            deferred.resolve(false);
        }
    };

    image.onerror = function() {
        alert("Invalid image. Please select an image file.");
        deferred.resolve(false);
    }

    image.src = _URL.createObjectURL(file);

    return deferred.promise();
}


$("#form").submit(function(event) {
    var form = this;

    if (isSupportedBrowser()) {
        event.preventDefault(); //Stop the submit for now

        var file = getSelectedFile();
        if (!file) {
            alert("Please select an image file.");
            return;
        }

        isGoodImage(file).then(function(isGood) {
            if (isGood)
                form.submit();
        });
    }
});
