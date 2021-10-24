<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  components:{

  },
  data() {
    return{
    }
  },
  mounted(){
    this.getMessage();
  },
  methods:{
    getMessage() {
      // 使用 axios 向 flask 发送请求
      const url = "http://127.0.0.1:5000/api/ping";
      this.axios.get(url)
        .then((res) => {
          console.log(res.data);
        })
        .catch((error) => {
          console.log(error);
        })
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  position: fixed;
  display: flex;
  width: 100%;
  height: 100%;
}
</style>
