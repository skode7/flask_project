const chatDiv = document.getElementById("chatDiv");
const submitBtn = document.getElementById("submit-btn");
const span = document.createElement("span");
const msgDiv = document.getElementById("messages")

async function fetchData (input) {
    try {
        const url = "http://127.0.0.1:5000/ask/" + input
        const response = await fetch(url)
        return await response.json()
    }
    catch (error){
        return {"error": error}
    }
}

async function showMessage(message) {
    span.className = "message"
    if ("reply" in message) {
        span.textContent = message["reply"]
    }
    else {
        span.textContent = message["error"]
    }
    msgDiv.append(span)
}

submitBtn.addEventListener("click", async (evt) => {
    let userInput = document.getElementById("txtarea");
    const value = userInput.value;
    const msgSpan = document.createElement("span")

    userInput.value = "";
    msgSpan.className = "message user"
    msgSpan.textContent = value;
    msgDiv.append(msgSpan)
    evt.preventDefault()

    const data = await fetchData(value);
    await showMessage(data)

})