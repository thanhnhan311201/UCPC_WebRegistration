// function showInpuBox(selectElement, other_popUp) {
//     selectElement.addEventListener('change', (event) => {
//         if (event.target.value == 6) {
//             if (other_popUp.style.display == 'none') {
//                 other_popUp.style.display = 'block';
//                 }
//         } else {
//             other_popUp.style.display = 'none';
//         }
//     });
// }

// const school_name1 = document.querySelector('.school_name1');
// const school_name2 = document.querySelector('.school_name2');
// const school_name3 = document.querySelector('.school_name3');
// const popUp1 = document.getElementById("popUp_1");
// const popUp2 = document.getElementById("popUp_2");
// const popUp3 = document.getElementById("popUp_3");

// showInpuBox(school_name1, popUp1)
// showInpuBox(school_name2, popUp2)
// showInpuBox(school_name3, popUp3)

// $("#registration_form").submit(async (event) => {
//     // var data = {};
//     // var informations = {};
//     // var school = {1: 'Trường Đại học Công nghệ Thông tin - UIT',
//     //                 2: 'Trường Đại học Khoa học Xã hội và Nhân văn - HCMUSSH',
//     //                 3: 'Trường Đại học Khoa học Tự nhiên - HCMUS',
//     //                 4: 'Trường Đại học Bách khoa - HCMUT',
//     //                 5: 'Trường Đại học Quốc tế - HCMIU'
//     //             };  

//     let registration_form =  document.getElementById('registration_form');
//     let formData = new FormData(registration_form);
    
//     if (formData.get('school2') == 6) {
//         value = document.getElementById("other_school1").value;
//         formData.set('school1', value);
//     }
//     if (formData.get('school2') == 6) {
//         value = document.getElementById("other_school2").value;
//         formData.set('school2', value);
//     }
//     if (formData.get('school3') == 6) {
//         value = document.getElementById("other_school3").value;
//         formData.set('school3', value);
//     }

//     $.ajax({
//         type: "POST",
//         url: "http://localhost:8000",
//         // contentType: 'multipart/form-data',
//         contentType: false,
//         enctype: 'multipart/form-data',
//         processData: false,
//         cache: false,
//         data: formData,
//         success: (data) => {    
//             console.log(data);
//         }
//     })

//     // formData.forEach((value, key) => {
//     //     if (key.includes('school')) {
//     //         if (value == 6) {
//     //             value = document.getElementById("other_" + key).value;
//     //             informations[key] = value;
//     //         } else {
//     //             informations[key] = school[value];
//     //         }
//     //     } else {
//     //         informations[key] = value;
//     //     }
//     // });

//     // data["informations"] = informations;

//     // fetch('https://us-central1-ucpc-348205.cloudfunctions.net/export_2_sheet', {
//     //     method: 'POST',
//     //     headers: {
//     //         'Content-Type': 'application/json',
//     //     },
//     //     body: JSON.stringify(data),
//     //     })
//     //     .then(response => response.json())
//     //     .then(data => console.log(data.message))
// });