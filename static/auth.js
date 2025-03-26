function verifyRERA() {
    const reraID = document.getElementById("rera_id").value.trim();
    const statusElement = document.getElementById("authStatus");

    if (!reraID) {
        statusElement.style.color = "red";
        statusElement.innerHTML = "⚠ Please enter a RERA ID";
        return;
    }

    fetch("http://127.0.0.1:5000/verify_rera", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ rera_id: reraID })
    })
    .then(response => response.json())
    .then(data => {
        if (data.verified) {
            statusElement.style.color = "green";
            statusElement.innerHTML = "✅ RERA ID Verified";
        } else {
            statusElement.style.color = "red";
            statusElement.innerHTML = "❌ Invalid RERA ID";
        }
    })
    .catch(error => {
        console.error("Error verifying RERA ID:", error);
        statusElement.style.color = "red";
        statusElement.innerHTML = "⚠ Error checking RERA ID";
    });
}
