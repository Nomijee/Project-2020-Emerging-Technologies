let URL = "http://127.0.0.1:5000/predict";

async function getArrangementRecords() {
    let speed = document.getElementById("search_field").value;

    await fetch(URL, {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({'speed': speed})
  })
        .then(response => response.json())
        .then(recordsJSON => {
            let powerGenerationData = "<tr class='arrangement_record'>"
                + "<td>" + recordsJSON['speed'] + "</td>"
                + "<td>" + recordsJSON['power'] + "</td>"
                + "</tr>";
            $("table tbody").append(powerGenerationData);
        });

}
