messagesModels = {
  // 取得訊息
  async getMessages() {
    const res = await fetch('/messages');
    const data = await res.json();
    return data;
  },
  //   新增訊息
  async postMessage() {
    const username = document.getElementById('username').value;
    const content = document.getElementById('content').value;
    const imageInput = document.getElementById('image');
    const formData = new FormData();

    formData.append('username', username);
    formData.append('content', content);
    if (imageInput.files.length > 0) {
      formData.append('image', imageInput.files[0]);
    }

    const res = await fetch('/messages', {
      method: 'POST',
      body: formData,
    });

    const result = await res.json();
    return result;
  },
};
messagesView = {
  renderMessage(data) {
    const messagesContent = document.getElementById('messagesContent');
    messagesContent.innerHTML = '';

    data.forEach((msg) => {
      const div = document.createElement('div');
      div.className = 'messages_content_msg';

      let html = `<div class="messages_content_msg_name">${msg.username || ''}</div>
          <div class="messages_content_msg_text">${msg.content || ''}</div>`;
      if (msg.image_url) {
        html += `<img src="${msg.image_url}" alt="image" class="msg-img">`;
      }
      div.innerHTML = html;
      messagesContent.appendChild(div);
    });
  },
};
messagesController = {
  init() {
    messagesController.fetchMessages();
    messagesController.formEvent();
  },
  // 取得訊息
  async fetchMessages() {
    const data = await messagesModels.getMessages();
    messagesView.renderMessage(data);
  },
  //   送出訊息
  async formEvent() {
    const form = document.getElementById('messageForm');

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const result = await messagesModels.postMessage();
      if (result.success) {
        form.reset();
        messagesController.fetchMessages();
      } else {
        alert('上傳失敗');
        console.log(`post message error : ${result.msg}`);
      }
    });
  },
};

// 初始化
messagesController.init();
