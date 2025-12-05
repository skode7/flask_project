const chatDiv = document.getElementById("chatDiv");
const submitBtn = document.getElementById("submit-btn");
const span = document.createElement("span");
const msgDiv = document.getElementById("messages")

async function fetchData (input) {
    const url = "http://127.0.0.1:5000/ask/" + input
    const response = await fetch(url)
    return await response.json()
}

async function showMessage(message) {
    span.textContent = message["reply"]
    msgDiv.append(span)

}

submitBtn.addEventListener("click", async (evt) => {
    const inputValue = document.getElementById("txtarea").value;
    const data = await fetchData(inputValue)
    evt.preventDefault()
    await showMessage(data)

})