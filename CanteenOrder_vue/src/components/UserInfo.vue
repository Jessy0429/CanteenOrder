<template>
  <div>
    <el-collapse v-model="activeNames">
      <el-collapse-item>
        <template slot="title">
          <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png" :size="60"></el-avatar>
          <span style="margin-left: 20px">{{this.UserName}}</span>
        </template>
        <el-descriptions :column="2" class="margin-top">
          <el-descriptions-item label="用户名" :labelStyle="{'line-height': '50px'}" :contentStyle="{'line-height': '50px'}">
            <span style="margin-right: 10px">{{this.UserName}}</span>
            <el-button size="mini" @click="dialogVisible = true; dialogID = 0">修改</el-button>
          </el-descriptions-item>
          <el-descriptions-item label="手机号" :labelStyle="{'line-height': '50px'}" :contentStyle="{'line-height': '50px'}">
            <span style="margin-right: 10px">{{this.TelNumber}}    </span>
            <el-button size="mini" @click="dialogVisible = true; dialogID = 1">修改</el-button>
          </el-descriptions-item>
          <el-descriptions-item label="密码" :labelStyle="{'line-height': '50px'}" :contentStyle="{'line-height': '50px'}">
            <el-button size="mini" @click="dialogVisible = true; dialogID = 2">修改密码</el-button>
          </el-descriptions-item>
        </el-descriptions>
      </el-collapse-item>
      <el-collapse-item>
        <template slot="title">
          <i class="el-icon-s-home" size="50px"></i>
          <span style="margin-left: 20px">我的收货信息</span>
          <el-button icon="el-icon-plus" circle size="mini" @click="dialogVisible = true; dialogID = 3"></el-button>
        </template>
        <div v-for="(DeliveredInfo, index) in this.DeliveredInfos">
          <el-descriptions :title="DeliveredInfo.Consignee + ' ' + DeliveredInfo.Telephone" :colon="false">
            <template slot="extra">
              <el-switch v-model="DeliveredInfo.isdefault" active-text="设为默认" @change="changeDefault(index)"></el-switch>
            </template>
            <el-descriptions-item content-style="width: 100%">
              <el-row>
                <el-col :span="12" style="line-height: 40px"><span>{{DeliveredInfo.Address}}</span></el-col>
                <el-col :span="12" style="text-align: right"><el-button icon="el-icon-edit" circle align="right" @click="dialogVisible = true; dialogID = 3; edit_index = index"></el-button></el-col>
              </el-row>
            </el-descriptions-item>
          </el-descriptions>
        </div>
      </el-collapse-item>
    </el-collapse>
    <div>
      <el-dialog :visible.sync="dialogVisible" :append-to-body="true">
        <template slot="title">
          <span v-if="dialogID == 2">修改密码</span>
          <span v-else-if="dialogID == 1">修改手机号</span>
          <span v-else-if="dialogID == 0">修改用户名</span>
          <span v-else-if="dialogID == 3 && edit_index != null">修改收货信息</span>
          <span v-else-if="dialogID == 3 && edit_index == null">新增收货信息</span>
        </template>
        <el-row type="flex" justify="center" align="middle" v-if="dialogID == 0">
          <el-col :span="6" style="text-align:center">用户名</el-col>
          <el-col :span="18"><el-input  :placeholder="this.UserName" v-model="edit_UserName" @keydown.enter.native="updateInfo"></el-input></el-col>
        </el-row>
        <el-row type="flex" justify="center" align="middle" v-else-if="dialogID == 1">
          <el-col :span="6" style="text-align:center">手机号</el-col>
          <el-col :span="18"><el-input  :placeholder="this.TelNumber" v-model="edit_TelNumber" @keydown.enter.native="updateInfo"></el-input></el-col>
        </el-row>
        <div v-else-if="dialogID == 2">
          <el-row type="flex" justify="center" align="middle" style="margin: 10px">
            <el-col :span="6" style="text-align:center">原密码</el-col>
            <el-col :span="18"><el-input  placeholder="请输入原始密码" v-model="input_PW"></el-input></el-col>
          </el-row>
          <el-row type="flex" justify="center" align="middle" style="margin: 10px">
            <el-col :span="6" style="text-align:center">新密码</el-col>
            <el-col :span="18"><el-input  placeholder="请输入更改后的密码" v-model="edit_PassWord"></el-input></el-col>
          </el-row>
          <el-row type="flex" justify="center" align="middle">
            <el-col :span="6" style="text-align:center; color:#f00;" v-if="!this.checkPW">*密码错误</el-col>
          </el-row>
        </div>
        <div v-else-if="dialogID == 3">
          <el-row type="flex" justify="center" align="middle" style="margin: 10px">
            <el-col :span="6" style="text-align:center">收货姓名</el-col>
            <el-col :span="18">
              <el-input  :placeholder="this.edit_index != null ? this.DeliveredInfos[this.edit_index].Consignee : '请输入收货人姓名'" v-model="edit_Consignee"></el-input>
            </el-col>
          </el-row>
          <el-row type="flex" justify="center" align="middle" style="margin: 10px">
            <el-col :span="6" style="text-align:center">手机号码</el-col>
            <el-col :span="18"><el-input  :placeholder="this.edit_index != null ? this.DeliveredInfos[this.edit_index].Telephone: '请输入收货手机号'" v-model="edit_Telephone"></el-input></el-col>
          </el-row>
          <el-row type="flex" justify="center" align="middle" style="margin: 10px">
            <el-col :span="6" style="text-align:center">收货地址</el-col>
            <el-col :span="18"><el-input  :placeholder="this.edit_index != null ? this.DeliveredInfos[this.edit_index].Address: '请输入收货地址'" v-model="edit_Address"></el-input></el-col>
          </el-row>
        </div>
        <span slot="footer" class="dialog-footer">
          <el-button @click="updateInfo">确 定</el-button>
          <el-button @click="dialogVisible = false">取 消</el-button>
        </span>

      </el-dialog>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserInfo",
  data(){
    return{
      dialogVisible: false,
      dialogID: undefined,
      activeNames: ['1'],
      UserName: '',
      UserID: null,
      TelNumber: '',
      PassWord: '',
      edit_UserName: '',
      edit_TelNumber: '',
      input_PW: '',
      edit_PassWord: '',
      checkPW: true,
      edit_index: null,
      edit_Consignee: '',
      edit_Telephone: '',
      edit_Address: '',
      DeliveredInfos:[]
    }
  },
  mounted() {
    this.getData();
  },
  methods: {
    updateInfo(){
      let update = {}
      if (this.dialogID === 0){
        this.UserName = this.edit_UserName;
        this.edit_UserName = '';
        this.dialogVisible = false;
        update = {username: this.UserName}
      }
      else if(this.dialogID === 1){
        this.TelNumber = this.edit_TelNumber;
        this.edit_TelNumber = '';
        this.dialogVisible = false;
        update = {telnumber: this.TelNumber}
      }
      else if(this.dialogID === 2){
        this.checkPW = (this.input_PW === this.PassWord);
        if(this.checkPW) {
          this.PassWord = this.edit_PassWord;
          this.edit_PassWord = '';
          this.dialogVisible = false;
          update = {password: this.PassWord}
        }
        this.edit_PassWord = '';
        this.input_PW = '';
      }
      else if(this.dialogID === 3){
        if (this.edit_index != null) {
          update = {deliveredID: this.DeliveredInfos[this.edit_index].DeliveredID};
          let key = '';
          let value = '';
          if (this.edit_Consignee) {
            key = 'consignee';
            value = this.edit_Consignee;
            update[key] = value;
            this.DeliveredInfos[this.edit_index].Consignee = this.edit_Consignee;

          }
          if (this.edit_Telephone) {
            key = 'telephone';
            value = this.edit_Telephone;
            update[key] = value;
            this.DeliveredInfos[this.edit_index].Telephone = this.edit_Telephone;
          }
          if (this.edit_Address) {
            key = 'address';
            value = this.edit_Address;
            update[key] = value;
            this.DeliveredInfos[this.edit_index].Address = this.edit_Address;
          }
        }
        else update = {consignee: this.edit_Consignee, telephone: this.edit_Telephone, address: this.edit_Address};
        this.dialogVisible = false;
      }

      if(this.edit_index != null) {
        if(this.dialogID != 3){
          const url = "http://127.0.0.1:5000/api/updateUserInfo"
          this.axios.put(url, update)
            .then((res) => {console.log(res);})
            .catch((error) => {
              console.log(error);
            })
        }
        else{
          const url = "http://127.0.0.1:5000/api/updateDeliveredInfo"
          this.axios.put(url, update)
            .then((res) => {console.log(res);})
            .catch((error) => {
              console.log(error);
            })
        }
      }
      else{
        const url = "http://127.0.0.1:5000/api/insertDeliveredInfo"
        this.axios.post(url, update)
          .then((res) => {
            console.log(res);
            this.DeliveredInfos.push({deliveredID: res.data, Consignee: this.edit_Consignee, Telephone: this.edit_Telephone, Address: this.edit_Address, isdefault: false})
          })
          .catch((error) => {
            console.log(error);
          })
      }
      this.edit_index = null;
    },
    changeDefault(index){
      for (let i = 0;i < this.DeliveredInfos.length; i++){
        if (i != index) this.DeliveredInfos[i].isdefault = false;
      }
    },
    getData(){
      // 使用 axios 向 flask 发送请求
      const url_ui = "http://127.0.0.1:5000/api/getUserInfo";
      // console.log(undefined.data)
      this.axios.get(url_ui)
        .then((res) => {
          console.log(res.data);
          this.UserID = res.data[0];
          this.UserName = res.data[1];
          this.TelNumber = res.data[2];
          this.PassWord = res.data[3];
        })
        .catch((error) => {
          console.log(error);
        })
        .then(
          ()=>{
            const url_di = "http://127.0.0.1:5000/api/getDeliveredInfo"
            this.axios.get(url_di)
              .then((res) => {
                console.log(res.data);
                for (let i = 0; i < res.data.length; i++){
                  this.DeliveredInfos.push({DeliveredID: res.data[i][0], Consignee: res.data[i][2], Telephone: res.data[i][3], Address: res.data[i][4], isdefault: (i > 0 ? false : true)})
                }
              })
              .catch((error) => {
                console.log(error);
              })
          }
      )
    }
  }
}
</script>

<style scoped>
.el-collapse /deep/ .el-collapse-item__header{
  height: 80px;
  font-size: 25px;
  color: #62a8f0;
}
</style>
