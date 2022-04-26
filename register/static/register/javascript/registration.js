$("#registration_form").submit(async (event) => {
    var data = {};
    var informations = {};
    var school = {1: 'Trường Đại học Công nghệ Thông tin - UIT',
                    2: 'Trường Đại học Khoa học Xã hội và Nhân văn - HCMUSSH',
                    3: 'Trường Đại học Khoa học Tự nhiên - HCMUS',
                    4: 'Trường Đại học Bách khoa - HCMUT',
                    5: 'Trường Đại học Quốc tế - HCMIU'
                };  

    let registration_form =  document.getElementById('registration_form');
    let formData = new FormData(registration_form);
    
    formData.forEach((value, key) => {
        if (key.includes('school')) {
            informations[key] = school[value];
        } else {
            informations[key] = value;
        }
    });
    data["informations"] = informations;

    fetch('https://us-central1-ucpc-348205.cloudfunctions.net/export_2_sheet', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => console.log(data.message))
    // event.preventDefault();
});