const socket = io();

socket.on("event", (data) => {
    const list = document.getElementById("events");
    const item = document.createElement("li");
    item.innerText = `${data.timestamp} | ${data.event_type} | ${data.value}`;
    list.prepend(item);
});

