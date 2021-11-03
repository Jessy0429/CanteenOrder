<template>
  <div>
    <div class="background">
      <img src="../assets/background_app.jpg" class="image"/>
    </div>
    <el-container direction="vertical" style="position:absolute;left:0;right:0;top:0;bottom:0;overflow:hidden;">
      <el-header height="100px">
        <span>{{this.username}}，喜欢您来:D</span>
        <i class="el-icon-food"></i>
      </el-header>
      <el-container height="100%" direction="horizontal">
        <el-aside>
          <el-menu class="el-menu-vertical-demo"
                   @select="handleSelect"
                   default-active="0">
<!--                   background-color="rgba(0,0,0,0)"-->

            <el-menu-item class="el-submenu" index="0">
              <i class="el-icon-tableware" style="font-size: 30px"></i>
              <span>首页</span>
            </el-menu-item>
            <el-menu-item class="el-submenu" index="1" height="250px">
              <i class="el-icon-s-claim" style="font-size: 30px"></i>
              <span>我的订单</span>
            </el-menu-item>
            <el-menu-item class="el-submenu" index="2" height="250px">
              <i class="el-icon-user" style="font-size: 30px"></i>
              <span>个人中心</span>
            </el-menu-item>
          </el-menu>
        </el-aside>
        <el-main>
          <router-view @childEvent="changeName"></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "app_user",
  data(){
    return {
      clickType: NaN,
      clickPath: undefined,
      userID: this.$route.query.userID,
      username: this.$route.query.username,
    }
  },
  methods:{
    handleSelect(key, keyPath) {
      this.clickType = 'updateClickType';
      this.clickPath = keyPath;
      // this.$store.commit('updateClickType', keyPath);
      if(keyPath[0] == '0') {
        this.clickType = 'showMainPage';
        this.$router.push({path:'/usermain', query:{userID: this.userID}});
      }
      else if(keyPath[0] == '1') {
        this.clickType = 'showOrdersPage';
        this.$router.push({path:'/userorders', query:{userID: this.userID}});
      }
      else if(keyPath[0] == '2') {
        this.clickType = 'showUserPage';
        console.log(this.userID);
        this.$router.push({path:'/userinfo', query:{userID: this.userID}});
      }
      // if(keyPath[0] === "5" || keyPath[0] === "8") {
      //   this.$store.commit('showMainGraph', true);
      // }
      // else {
      //   this.$store.commit('showMainGraph', false);
      console.log(this.clickType, this.clickPath)
      },
    changeName(name){
      console.log(name);
      if (name.username != this.username) this.username = name.username;
    }
  }
}
</script>

<style scoped>
.el-container{
  padding: 0px;
  margin: 0px;
  height: 100%;
}
.el-header{
  background-color: rgba(239, 120, 80, 0.99);
  color: #ffffff;
  text-align: center;
  line-height: 100px;
  font-family: 'Hiragino Sans GB';
  font-size: 30px;
}
.el-aside{
  text-align: center;
  width: 750px;
  font-family: 'Hiragino Sans GB';
  font-size: 20px;
}
.el-main{
  padding-left: 0;
}
.el-menu{
  background-color: rgba(255, 255, 255, 0.5);
}
.el-menu-item{
  font-size: 25px;
  height: 250px;
  text-align: center;
  line-height: 250px;
  font-family: "Microsoft JhengHei";
}
.el-menu-item.is-active {
  color: #ee7951;
}
.el-menu-item:focus, .el-menu-item:hover {
  outline: 0;
  background-color: #fae3db;
}
.background{
  width:100%;
  height:100%;  /**宽高100%是为了图片铺满屏幕 */
  z-index:-1;
  position: absolute;
}
.image{
  height: 100%;
  width: 100%;
  opacity: 20%;
}
</style>
