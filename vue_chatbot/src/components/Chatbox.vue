<template>
  <div class="chat-box">
    <div class="chatbox-container">
      <ul>
        <li v-for="(msg, idx) in messages" :key="idx" :class="msg.author">
          <p>
            <span>{{ msg.text }}</span>
          </p>
        </li>
      </ul>
    </div>
    <div class="chatinput-container">
      <b-form-input
        v-model="message"
        @keyup.enter="sendMessage"
        type="text"
      ></b-form-input>
      <b-button @click="sendMessage" variant="info">Send</b-button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Chatbox",
  data() {
    return {
      message: "",
      messages: [],
      loading: false,
    };
  },
  methods: {
    sendMessage() {
      this.loading = true;
      this.messages.push({
        text: this.message,
        author: "client",
      });

      axios({
        method: "post",
        url: "http://localhost:5000/chatbot",
        data: { text: this.message },
      }).then((res) => {
        this.messages.push({ text: res.data.text, author: "bot" });
      });

      // axios({
      //   method: "GET",
      //   url: "https://acobot-brainshop-ai-v1.p.rapidapi.com/get",
      //   headers: {
      //     "content-type": "application/octet-stream",
      //     "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
      //     "x-rapidapi-key":
      //       "2afc6d3e79mshae2be1d4810a177p196257jsnf07a6a459141",
      //     useQueryString: true,
      //   },
      //   params: {
      //     bid: "178",
      //     key: "sX5A2PcYZbsN5EY6",
      //     uid: "mashape",
      //     msg: this.message,
      //   },
      // })
      //   .then((res) => {
      //     this.messages.push({ text: res.data.cnt, author: "bot" });
      //   })
      //   .catch((error) => {
      //     console.log(error);
      // });
      this.message = "";
      this.loading = false;
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.chat-box {
  border: 1px solid black;
  border-radius: 8px;
  margin: 0 auto;
  width: 60%;
  padding: 5px;
}

ul {
  padding: 0;
}

.chat-box,
.chat-box li {
  display: flex;
  flex-direction: column;
  list-style-type: none;
}

.chatinput-container {
  display: flex;
  margin: 0 auto;
  width: 100%;
}

.btn {
  width: 135px;
}

.client span {
  background: rgb(3, 118, 194);
  border-radius: 4px;
  padding: 8px;
  float: left;
  color: white;
}

.bot span {
  background: lightcoral;
  border-radius: 4px;
  padding: 8px;
  float: right;
}
</style>
