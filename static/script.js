let voiceEnabled = true;

function appendMessage(sender, message) {
  const chatBox = document.getElementById('chat-box');
  const msg = document.createElement('div');
  msg.className = sender === 'You' ? 'user-message' : 'bot-message';
  msg.innerHTML = `<strong>${sender}:</strong> ${message}`;
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function sendMessage() {
  const input = document.getElementById('user-input');
  const message = input.value.trim();
  if (!message) return;
  appendMessage('You', message);
  input.value = '';

  fetch('/ask', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message })
  })
    .then(res => res.json())
    .then(data => {
      appendMessage('VISTA', data.reply);
      if (voiceEnabled) speak(data.reply);
    });
}

function speak(text) {
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.voice = speechSynthesis.getVoices()[0];
  speechSynthesis.speak(utterance);
}

function startListening() {
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = 'en-US';
  recognition.start();
  recognition.onresult = function (event) {
    document.getElementById('user-input').value = event.results[0][0].transcript;
    sendMessage();
  };
}

function toggleVoice() {
  voiceEnabled = !voiceEnabled;
  alert('Voice: ' + (voiceEnabled ? 'ON' : 'OFF'));
}

function toggleTheme() {
  document.body.classList.toggle('dark-mode');
}

function exportCode() {
  const chat = document.getElementById('chat-box').innerText;
  const blob = new Blob([chat], { type: 'text/plain' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'vista_convo.txt';
  a.click();
}

function clearChat() {
  document.getElementById('chat-box').innerHTML = '';
}
