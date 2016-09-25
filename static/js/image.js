$("#upload-form").on("submit", function(e) {
    e.preventDefault();

    var formData = new FormData(this)

    $.ajax({

        type: "POST",
        url: $(this).attr("action"),
        data: formData,
        cache:false,
        contentType: false,
        processData: false,
        success: function(image_path) {
            console.log("success");
            updateImage(image_path);
        },
        error: function(error) {
            console.log("error");
            console.log(error);
        }

    });
});

function updateImage(image_path) {
    $("#uploaded-image").attr("src", image_path);
}
