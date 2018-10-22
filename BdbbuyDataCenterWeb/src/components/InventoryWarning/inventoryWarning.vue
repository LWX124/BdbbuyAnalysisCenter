<template>
  <div id="main" style="margin-left: 3%;margin-right: 3%;margin-top: 20px">
    <div class="row" >
      <p :hidden="pageType!='count'" style="margin-left: 0px;width: 400px">
        <label >输入库存最低数量：</label>
        <input type="text" class="normal" v-model="countInfo"/>
        <label >件</label>
        <Button v-on:click="getData">
          刷新
        </Button>
        <small></small>
      </p>


    </div>
    <br>

    <Table  :data="tableData" :columns="tableColumns" stripe :loading="tableLoading"></Table>
    <div style="margin: 20px;overflow: hidden">
      <div style="float: right;">
        <Page ref="pages" :total="totalCount" :current="pageCurrent" @on-change="changePage"
              :page-size="pageSize" show-sizer :page-size-opts="page_size_opts" show-total></Page>
      </div>
    </div>

  </div>
</template>

<script>
  import {serverBaseURL} from '../../globalConfig'

  export default {
    name: 'inventoryWarning',
    data() {
      return {
        page_size_opts: [20, 40, 50, 100],
        pageSize: 20,
        tableData: [],
        tableColumns: [],
        totalCount: 0,
        allProductList: [],
        pageType: 'count',
        countInfo: 5,
        pageCurrent: 1,
        tableLoading: false

      }

    },
    mounted: function () {
      // 页面加载
      console.log('这里是库存预警页面')
      this.setTableColumn()
      this.getData()
      this.pageType = this.$route.query.type
    },

    methods: {

      getData:function () {
        this.tableData = []
        this.pageCurrent = 1
        this.tableLoading = true
        let url = serverBaseURL + 'product/getWarnigProduct'
        if (this.pageType == 'count') {
          url = url + '?lowCount=' + this.countInfo
        }
        this.$http.get(url).then(function (response) {
          var status = response.status;
          this.tableLoading = false
          if (status == 200) {
            var result = response.body;
            this.allProductList = result['data']['order_list']
            this.totalCount = result['data']['totalCount']
            this.changePage(1)
          }
        }, function (response) {
          console.log("发生错误")
          var str = response.body.message
          this.tableLoading = false
          this.$Message.success(str)
        });
      },

      setTableColumn:function () {
        this.tableColumns = [
          {
            title: 'id',
            key: 'product_id',
            width: 100,
            align: 'center',
          },
          {
            title: '中文名',
            key: 'name',
            width: 200,
            align: 'center',
          },
          {
            title: '库存数量',
            key: 'product_qty',
            width: 100,
            align: 'center',
          },
          {
            title: 'SKU',
            key: 'sku',
            width: 150,
            align: 'center',
          },
          {
            title: '售价',
            key: 'price',
            width: 150,
            align: 'center',
          },
          {
            title: '保质期',
            key: 'quality_date',
            width: 200,
            align: 'center',
          },
          ]
      },

      changePage:function (index) {
        var startPosition = 0
        var endPosition = this.allProductList.length
        if (this.allProductList.length > this.pageSize) {
          startPosition = this.pageSize * (index - 1)
          endPosition = this.pageSize * index
        }
        this.tableData = this.allProductList.slice(startPosition, endPosition)
      }

    }

  }
</script>

<style scoped>
  label {
    /*width: 25%;*/
    display: inline-block;
    padding: 0 5px;
    vertical-align: middle;
    font-style: normal;
    color: black;
    margin-left: 0px;
  }


  input[type="text"] {
    height: 30px;
    line-height: 20px;
    border-radius: 5px;
    padding: 5px 5px;
    vertical-align: middle;
    color: #666;
  }

</style>
