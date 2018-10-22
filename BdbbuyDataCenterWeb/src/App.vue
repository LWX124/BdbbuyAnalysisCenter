
<template>
  <div id="app">
    <!--<img src="./assets/logo.png">-->
    <Menu mode="horizontal" :active-name="menuActiveName"  @on-select="gotoPage">
      <MenuItem name="saleData">
        <Icon type="ios-stats" />
        销售统计
      </MenuItem>
      <MenuItem name="inventoryWarning">
        <Icon type="ios-warning" />
        库存预警
      </MenuItem>

    </Menu>
    <router-view/>
  </div>
</template>

<script>

  export default {
    name: 'App',
    data() {
      return {
        menuActiveName: 'saleData',
      }

    },

    mounted: function () {
      // 页面加载
      this.menuActiveName = this.$route.path.replace('/', '')
    },

    methods: {
      gotoPage:function (name) {
        this.$router.push({path: name})
      }
    }
  }
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #f5f7f9;
  margin-top: 10px;
}


</style>
