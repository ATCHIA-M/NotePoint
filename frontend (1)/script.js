console.log("JS is working");
async function cleanNotes() {
    const text = document.getElementById("inputText").value;
    const mode = document.getElementById("mode").value;

    console.log("Button clicked"); // ✅ debug

    const response = await fetch("http://localhost:5000/clean", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text, mode: mode })
    });

    console.log("Response:", response); // ✅ debug

    const data = await response.json();
    console.log("Data:", data); // ✅ debug

    document.getElementById("output").innerHTML = data.cleaned;
}
function changeTheme(theme) {
    document.body.className = theme;
}

function copyText() {
    const text = document.getElementById("output").innerText;
    navigator.clipboard.writeText(text);
    alert("Copied!");
}
let currentTheme = 0;

function toggleTheme() {
    const themes = ["", "dark", "pastel"];
    currentTheme = (currentTheme + 1) % themes.length;

    document.body.className = themes[currentTheme];
}