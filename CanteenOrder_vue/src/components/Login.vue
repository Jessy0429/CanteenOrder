<template>
  <div>
    <div class="background">
      <img src="../assets/background.jpg" class="image"/>
    </div>
    <div class="loginbody">
      <div>
        <el-card style="width: 400px">
          <el-tabs v-model="activeName" :stretch="true">
            <el-tab-pane label="登录" name="0">
              <el-form :model="signIn" status-icon :rules="rules" ref="signIn" label-width="100px">
                <el-form-item label="手机号" prop="user" label-width="80px">
                  <el-input v-model="signIn.user"></el-input>
                </el-form-item>
                <el-form-item label="密码" prop="password" label-width="80px">
                  <el-input type="password" v-model="signIn.password" autocomplete="off"></el-input>
                </el-form-item>
              </el-form>
              <el-button type="primary" @click="doLogin('signIn')">登录</el-button>
            </el-tab-pane>
            <el-tab-pane label="注册" name="1">
              <el-form :model="signUp" status-icon :rules="rules" ref="signUp" label-width="100px">
                <el-form-item label="手机号" prop="user">
                  <el-input v-model="signUp.user"></el-input>
                </el-form-item>
                <el-form-item label="密码" prop="password">
                  <el-input type="password" v-model="signUp.password" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="重复密码" prop="checkPass">
                  <el-input type="password" v-model="signUp.checkPass" autocomplete="off"></el-input>
                </el-form-item>
              </el-form>
              <el-button type="primary" @click="doSignup('signUp')">注册</el-button>
              <el-button type="primary" @click="clear('signUp')">清空</el-button>
            </el-tab-pane>
          </el-tabs>
        </el-card>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Login",
  // imgSrc:require('./src/loginbg.jpg'),
  props: {
    msg: String
  },
  data() {
    var validateUser = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入手机号'));
      }
      else callback();
    };
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'));
      }
      else if(this.activeName == 1){
        if (this.signUp.checkPass !== '') {
          this.$refs.signUp.validateField('checkPass');
        }
        callback();
      }
      else callback();
    };
    var validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'));
      } else if (value !== this.signUp.password) {
        callback(new Error('两次输入密码不一致!'));
      } else {
        callback();
      }
    };
    return {
      // username: '',
      // password: '',
      // error: {
      //   username: '',
      //   password: ''
      // },
      activeName: 0,
      userID: null,
      signIn: {
        user: '',
        password: '',
      },
      signUp: {
        user: '',
        password: '',
        checkPass: '',
      },
      rules: {
        user: [
          { validator: validateUser, trigger: 'blur' }
        ],
        password: [
          { validator: validatePass, trigger: 'blur' }
        ],
        checkPass: [
          { validator: validatePass2, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    doLogin(formName){
      this.$refs[formName].validate((valid) => {
        if(valid) {
          let _this = this;
          const url = "http://127.0.0.1:5000/api/login";
          this.axios.get(url, {params: {telnumber: this.signIn.user}})
          .then((res) => {
            console.log(res.data);
            if(this.signIn.password != res.data[3]){
              this.$message.error('密码错误');
              this.$refs[formName].resetFields();
            }
            else{
              this.$message.success('登录成功！');
              this.$refs[formName].resetFields();
              //  跳转到登录页
              this.$router.push({path: '/User', query: {userID: res.data[0], username: res.data[1]}});
            }
          })
          .catch((error) => {
            console.log(error);
          })
        }
        else return false;
      })
    },
    doSignup(formName){
      this.$refs[formName].validate((valid) => {
        if(valid) {
          const url = "http://127.0.0.1:5000/api/signup";
          var name = '用户' + this.signUp.user.substr(8,4);
          var user = {telnumber: this.signUp.user, password: this.signUp.password, username: name}
          this.axios.post(url, user)
            .then((res) => {
              console.log(res.data);
              if(res){
                this.$message.success('注册成功！');
                this.$refs[formName].resetFields();
                //  跳转到登录页
                this.$router.push({path: '/User', query: {userID: res.data[0], username: name}});
              }
            })
            .catch((error) => {
              console.log(error);
            })
        }
        else return false;
      })
    },
    clear(formName){
      this.$refs[formName].resetFields();
    }
  }
}
</script>
<style>
.loginbody{
  position: absolute;
  top: 50%;
  left: 50%;
  width: 100%;
  height: 100%;
  /*display: flex;*/
  /*justify-content: center;*/
  /*align-items: center;*/
  z-index: 1;
  margin: -200px 0 0 -200px;
  opacity: 80%;
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
.el-form-item__label{
  text-align: left;
}
</style>
