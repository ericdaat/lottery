function makeRequest(request_type, url, json_data) {
    $.ajax({
        type: request_type,
        url: url,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        data: JSON.stringify(json_data),
        success: function (data) {
           console.log("success");
        },
        error: function () {
           console.log("error");
        }
    });
}

function draw() {
    makeRequest(
        "POST",
        "/api/draw",
        {}
    )
    setTimeout(location.reload.bind(location), 200);
}


function reset() {
    makeRequest(
        "POST",
        "/api/reset",
        {}
    )
    setTimeout(location.reload.bind(location), 200);
}
