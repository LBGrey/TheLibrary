var show = document.getElementById("show")
var myForm = document.getElementById("myForm")
myForm.onsubmit = (e) => {
        e.preventDefault();

        let data = new FormData(myForm);

        let input = data.get("input");

        let choice = data.get("choice");

        choice ? search("author", input) : search("title", input)

}

function search(choice, input) {

        fetch(`https://openlibrary.org/search.json?${choice}=${input}&limit=28`)
        .then(data => data.json())
        .then(data => {
                console.log(data)
                let images = ""
                for (const doc of data.docs) {
                        let coverKey = doc.cover_edition_key;
                        let img = 
                        `<button onclick="create_book( '${doc.title}', '${doc.author_name[0]}', '${doc.subject && doc.subject[0]}' )">
                        <img src='http://covers.openlibrary.org/b/OLID/${coverKey}-M.jpg'>
                        </button>`
                        images += img;
                }
                show.innerHTML = images
        }) 

}

function create_book(title, author, genre) {
        console.log(title, author, genre)
        let data = {
        title, author, genre
        }
        let form = new FormData()
        form.append('title', title)
        form.append('author', author)
        form.append('genre', genre)
        console.log(data, form)


fetch('http://localhost:5000/create_book', { method:"POST", body:form })
        .then(console.log ('good'))
        .catch(console.log('error'))


        window.location.pathname = ('/show/id')
}


// var searchForm = document.getElementById("searchForm")
// searchForm.onsubmit = (e) => {
//     e.preventDefault()
//     var form = new FormData(myForm)
    
//     fetch('http://localhost:5000/search_books', { method:"POST", body:form})
//         .then(res => res.json())
//         .then(res => create_list(res))
// }


// function create_list(dataarray){
//     var results = document.getElementById("results")
//     results.innerHTML = ""
//     for (const data in dataarray){
//         results.innerHTML += `
//         <div style="display:flex; height: 25px;">
//             <p style="font-size: 25px; width: 300px;">${data.author}</p>
//             <p style="font-size: 25px; width: 500px;">${data.title}</p>
//             <p style="font-size: 15px; width: 50px; margin-top: -3px; margin-left: 0px">{{ ${ data.read} | replace (1, 'Been Read') | replace ('None', 'Not Read') }}</p>
//             <p style="margin-right:0px; display:flex">
//             <div style="margin-right: 0px; display:flex; width: 200px; margin-left:-30px; justify-content: right">
//                 <form action='/show/${books.id}'>
//                     <input type="submit" class="show solid" value="Details">
//                 </form>
//                 <form action='/book/${data.id}/edit'>
//                     <input type="submit" class="show solid" value="Edit">
//                 </form><form action="/delete_book" method='POST'>
//                     <input type="hidden" name="book_id" value="${data.id}">
//                     <input type="submit" class="show solid" value="Delete">
//                 </form>
//             </div>
//             </p>
//         </div>
//         `
//     }
// }
// var searchForm2 = document.getElementById("searchForm2")
// searchForm2.onsubmit = (e) => {
//     e.preventDefault()
//     var form2 = new FormData(myForm2)
    
//     fetch('http://localhost:5000/search_wishlist', { method:"POST", body:form2})
//         .then(res => res.json())
//         .then(res => create_list2(res))
// }


// function create_list2(dataarray){
//     var results2 = document.getElementById("results2")
//     results2.innerHTML = ""
//     for (const data in dataarray){
//         results2.innerHTML += `
//         <div style="display:flex; height: 25px;">
//             <p style="font-size: 25px; width: 300px;">${data.author}</p>
//             <p style="font-size: 25px; width: 500px;">${data.title}</p>
//             <p style="font-size: 15px; width: 50px; margin-top: -3px; margin-left: 0px">{{ ${ data.read} | replace (1, 'Been Read') | replace ('None', 'Not Read') }}</p>
//             <p style="margin-right:0px; display:flex">
//             <div style="margin-right: 0px; display:flex; width: 200px; margin-left:-30px; justify-content: right">
//                 <form action='/show/${books.id}'>
//                     <input type="submit" class="show solid" value="Details">
//                 </form>
//                 <form action='/book/${data.id}/edit'>
//                     <input type="submit" class="show solid" value="Edit">
//                 </form><form action="/delete_book" method='POST'>
//                     <input type="hidden" name="book_id" value="${data.id}">
//                     <input type="submit" class="show solid" value="Delete">
//                 </form>
//             </div>
//             </p>
//         </div>
//         `
//     }
// }
// var searchForm = document.getElementById("searchForm")
// searchForm.onsubmit = (e) => {
//     e.preventDefault()
//     var form = new FormData(myForm)
    
//     fetch('http://localhost:5000/search_books', { method:"POST", body:form})
//         .then(res => res.json())
//         .then(res => create_list(res))
// }


// function create_list(dataarray){
//     var results = document.getElementById("results")
//     results.innerHTML = ""
//     for (const data in dataarray){
//         results.innerHTML += `
//         <div style="display:flex; height: 25px;">
//             <p style="font-size: 25px; width: 300px;">${data.author}</p>
//             <p style="font-size: 25px; width: 500px;">${data.title}</p>
//             <p style="font-size: 15px; width: 50px; margin-top: -3px; margin-left: 0px">{{ ${ data.read} | replace (1, 'Been Read') | replace ('None', 'Not Read') }}</p>
//             <p style="margin-right:0px; display:flex">
//             <div style="margin-right: 0px; display:flex; width: 200px; margin-left:-30px; justify-content: right">
//                 <form action='/show/${books.id}'>
//                     <input type="submit" class="show solid" value="Details">
//                 </form>
//                 <form action='/book/${data.id}/edit'>
//                     <input type="submit" class="show solid" value="Edit">
//                 </form><form action="/delete_book" method='POST'>
//                     <input type="hidden" name="book_id" value="${data.id}">
//                     <input type="submit" class="show solid" value="Delete">
//                 </form>
//             </div>
//             </p>
//         </div>
//         `
//     }
// }






// var mysearch = document.getElementById("list")
// function search_books(title, author) {
//     let data = {
//         title, author
//     }
//     let form = 
// }