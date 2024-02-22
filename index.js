const slides = [];


function getBlockHtml(title, description, imageUrl) {
    return `<div class="block">
            <div class="block-image">
                <img src="${imageUrl}"/>
            </div>
            <div class="block-content">
                <div class="block-title">
                    <h2>
                        ${title}
                    </h2>
                </div>
                <div class="block-description">
                    <p>${description}</p>
                </div>
            </div>
        </div>`
}

const main = () => {
    fetch(' http://127.0.0.1:5000/')
        .then((response) => {
            return response.json();
        })
        .then((data) => {

            const centerBlock = document.getElementById("center")
            console.log(centerBlock)
            let newContent = ""
            data.forEach((item) => {
                console.log(item)
                newContent = newContent+getBlockHtml(item.title,item.description,item.photo)
                centerBlock.innerHTML = newContent
            })
            console.log(data);
        });
    console.log("sadfsf")
}

main()
