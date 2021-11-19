function search(choice, input) {

    fetch(`https://openlibrary.org/search.json?${choice}=${input}&limit=20`)
    .then(data => data.json())
    .then(data => {
            console.log(data)
            let images
            
            for (const doc of data.docs) {
                    let coverKey = doc.cover_edition_key;
                    let url =`https://openlibrary.org/${doc.key}`
                    let img = 
                    `<a rel="noopener noreferrer" target="_blank" href=${url}>
                    <img src='http://covers.openlibrary.org/b/OLID/${coverKey}-M.jpg'>
                    </a>`
                    images += img;
            }
            show.innerHTML = images

    }) 

}