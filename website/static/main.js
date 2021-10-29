function deleteEntry(noteId){
    fetch('/deleteEntry', {
        method:'POST',
        body: JSON.stringify({noteId:noteId}),
    }).then((_res) => {
        window.location.href="/account";
    });
}
// function updateEntry(noteId){
//     fetch('/updateEntry', {
//         method:'POST',
//         body: JSON.stringify({noteId:noteId}),
//     })
    
// }