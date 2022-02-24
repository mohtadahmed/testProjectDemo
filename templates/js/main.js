// function fileSubmit() {
//         let photo = document.getElementById("image-file").files[0];
//         let formData = new FormData();

//         formData.append("photo", photo);
//         fetch("/upload/image", { method: "POST", body: formData });
//       }



// async function fileSubmit() {
//     let formData = new FormData();           
//     formData.append("file", fileupload.files[0]);
//     await fetch('/upload/image', {
//       method: "POST", 
//       body: formData
//     });    
//     alert('The file has been uploaded successfully.');
// }