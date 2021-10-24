<template>
  <el-container direction="vertical" style="position:absolute;left:0;right:0;top:0;bottom:0;overflow:hidden;">
    <el-header height="100px">
      <span>周邹揪，喜欢您来:D</span>
      <i class="el-icon-food"></i>
    </el-header>
    <el-container height="100%" direction="horizontal">
      <el-aside>
        <el-menu class="el-menu-vertical-demo"
                 @select="handleSelect"
                  default-active="0">
          <el-menu-item class="el-submenu" index="0">
            <i class="el-icon-tableware"></i>
            <span>首页</span>
          </el-menu-item>
          <el-menu-item class="el-submenu" index="1">
            <i class="el-icon-s-claim"></i>
            <span>我的订单</span>
          </el-menu-item>
          <el-menu-item class="el-submenu" index="2">
            <i class="el-icon-user"></i>
            <span>个人中心</span>
          </el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  name: "app_user",
  data(){
    return {
      clickType: NaN,
      clickPath: undefined,
    }
  },
  methods:{
    handleSelect(key, keyPath) {
      this.clickType = 'updateClickType';
      this.clickPath = keyPath;
      // this.$store.commit('updateClickType', keyPath);
      if(keyPath[0] == '0') {
        this.clickType = 'showMainPage';
        this.$router.push({name:'usermain'});
      }
      else if(keyPath[0] == '1') {
        this.clickType = 'showOrdersPage';
        this.$router.push({name:'userorders'});
      }
      else if(keyPath[0] == '2') {
        this.clickType = 'showUserPage';
        this.$router.push({name:'userinfo'});
      }
      // if(keyPath[0] === "5" || keyPath[0] === "8") {
      //   this.$store.commit('showMainGraph', true);
      // }
      // else {
      //   this.$store.commit('showMainGraph', false);
      console.log(this.clickType, this.clickPath)
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
  background-color: #66CCCC;
  color: #ffffff;
  text-align: center;
  line-height: 100px;
  font-family: 'Hiragino Sans GB';
  font-size: 30px;

}
.el-aside{
  text-align: center;
  width: 200px;
  font-family: 'Hiragino Sans GB';
  font-size: 20px;
}
.el-menu-item{
  font-size: 15px;
  /*height: 200px;*/
  text-align: center;
}
</style>
