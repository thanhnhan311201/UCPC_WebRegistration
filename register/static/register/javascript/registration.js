const form = document.querySelector('#registration_form');
const TeamRegex = /\b\S*[AĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴA-Z]+\S*\b/;
const NumberRegex = /^([0-9]{10}|[0-9]{11})$/;
const CMNDandCCCD = /^([0-9]{9}|[0-9]{12})$/;
const NameRegex = /^([a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂẾưăạảấầẩẫậắằẳẵặẹẻẽềềểếỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ]{1,}\s{0,}){2,7}$/;
const PasswordRegex = /^(?=.{6,})(?=.*[a-z]+)(?=.*\d+)(?=.*[A-Z]+)[ -~]*$/;
const EmailRegex = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;


let team = form.elements.namedItem("team");
let member1 = form.elements.namedItem("member1");
let cmnd1 = form.elements.namedItem("cmnd1");
let phone1 = form.elements.namedItem("phone1");
let member2 = form.elements.namedItem("member2");
let cmnd2 = form.elements.namedItem("cmnd2");
let phone2 = form.elements.namedItem("phone2");
let member3 = form.elements.namedItem("member3");
let cmnd3 = form.elements.namedItem("cmnd3");
let phone3 = form.elements.namedItem("phone3");
let email = form.elements.namedItem("email");
let password = form.elements.namedItem("password");

team.addEventListener('input', validate);
member1.addEventListener('input', validate);
cmnd1.addEventListener('input', validate);
phone1.addEventListener('input', validate);
member2.addEventListener('input', validate);
cmnd2.addEventListener('input', validate);
phone2.addEventListener('input', validate);
member3.addEventListener('input', validate);
cmnd3.addEventListener('input', validate);
phone3.addEventListener('input', validate);
email.addEventListener('input', validate);
password.addEventListener('input', validate);

function validate (e) {
    if (e.target.name == "team") {
        if (TeamRegex.test(e.target.value)) {
            e.target.classList.add('valid');
            e.target.classList.remove('invalid');
        } else {
            e.target.classList.add('invalid');
            e.target.classList.remove('valid');
        }
    }

    if (e.target.name == "member1") {
        if (NameRegex.test(e.target.value)) {
            e.target.classList.add('valid');
            e.target.classList.remove('invalid');
        } else {
            e.target.classList.add('invalid');
            e.target.classList.remove('valid');
        }
    }

    if (e.target.name == "member2") {
        if (NameRegex.test(e.target.value)) {
            e.target.classList.add('valid');
            e.target.classList.remove('invalid');
        } else {
            e.target.classList.add('invalid');
            e.target.classList.remove('valid');
        }
    }

    if (e.target.name == "member3") {
        if (NameRegex.test(e.target.value)) {
            e.target.classList.add('valid');
            e.target.classList.remove('invalid');
        } else {
            e.target.classList.add('invalid');
            e.target.classList.remove('valid');
        }
    }

    if (e.target.name == "cmnd1") {
        if (CMNDandCCCD.test(e.target.value)) {
            e.target.classList.add('valid');
            e.target.classList.remove('invalid');
        } else {
            e.target.classList.add('invalid');
            e.target.classList.remove('valid');
        }
    }

    if (e.target.name == "cmnd2") {
        if (CMNDandCCCD.test(e.target.value)) {
            e.target.classList.add('valid');
            e.target.classList.remove('invalid');
        } else {
            e.target.classList.add('invalid');
            e.target.classList.remove('valid');
        }
    }

    if (e.target.name == "cmnd3") {
        if (CMNDandCCCD.test(e.target.value)) {
            e.target.classList.add('valid');
            e.target.classList.remove('invalid');
        } else {
            e.target.classList.add('invalid');
            e.target.classList.remove('valid');
        }
    }

    if (e.target.name == "phone1") {
        if (NumberRegex.test(e.target.value)) {
            e.target.classList.add('valid');
            e.target.classList.remove('invalid');
        } else {
            e.target.classList.add('invalid');
            e.target.classList.remove('valid');
        }
    }

    if (e.target.name == "phone2") {
        if (NumberRegex.test(e.target.value)) {
            e.target.classList.add('valid');
            e.target.classList.remove('invalid');
        } else {
            e.target.classList.add('invalid');
            e.target.classList.remove('valid');
        }
    }

    if (e.target.name == "phone3") {
        if (NumberRegex.test(e.target.value)) {
            e.target.classList.add('valid');
            e.target.classList.remove('invalid');
        } else {
            e.target.classList.add('invalid');
            e.target.classList.remove('valid');
        }
    }

    if (e.target.name == "email") {
        if (EmailRegex.test(e.target.value)) {
            e.target.classList.add('valid');
            e.target.classList.remove('invalid');
        } else {
            e.target.classList.add('invalid');
            e.target.classList.remove('valid');
        }
    }

    if (e.target.name == "password") {
        if (PasswordRegex.test(e.target.value)) {
            e.target.classList.add('valid');
            e.target.classList.remove('invalid');
        } else {
            e.target.classList.add('invalid');
            e.target.classList.remove('valid');
        }
    }
}

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