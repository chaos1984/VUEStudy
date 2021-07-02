<template >
  <div class="block" style="margin-top: 20px">
    <el-timeline>
      <el-timeline-item v-for="(activity, index) in activities" :key="index">
        <el-card style="width: 90%">
          <h3>{{ activity.title }}</h3>
          <p>{{ activity.content }}</p>
          <p>{{ activity.timestamp }}</p>
          <!-- <el-row>
            <el-button
              type="primary"
              icon="el-icon-edit"
              circle
              size="mini"
              @click="dialogFormVisible = true"
            ></el-button>
            <el-button
              type="danger"
              icon="el-icon-delete"
              circle
              size="mini"
            ></el-button>
          </el-row> -->
        </el-card>
      </el-timeline-item>
    </el-timeline>
    <!-- form input -->
    <el-divider/>
    <div style="margin-left: 20px " width="50%">
  <el-select
    v-model="title"
    multiple
    filterable
    allow-create
    default-first-option
    placeholder="Choose tags for your article">
    <el-option
      v-for="item in options"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
      <div style="margin: 20px 0"></div>
      <el-input
        type="textarea"
        :rows="10"
        placeholder="Content"
        v-model="content"
      >
      </el-input>

      <el-row :gutter="1" style="margin-top: 20px">
        <el-button
          type="primary"
          icon="el-icon-plus"
          circle
          size="mini"
          @click="addItem"
        ></el-button>
        <el-button
          type="danger"
          icon="el-icon-minus"
          circle
          size="mini"
          @click="delItem"
        ></el-button>
      </el-row>
    </div>
  </div>
</template>


<script>
export default {
  props: {
    getdata: {},
  },
  data() {
    return {
      title: "",
      content: "",
      dialogFormVisible: false,
      loading: true,
      reverse: true,
      state: false,
      flag: false,
      form: {},
      options: [{
          value: 'A surface update',
          label: 'A surface update'
        }, {
          value: 'Cover Hinge update',
          label: 'Cover Hinge update'
        }, {
          value: 'Cushion Change',
          label: 'Cushion Change'
        }],
      activities: [ ],
    };
  },

   mounted() {
    this.activities = JSON.parse(this.getdata.Log);
  
  },
  methods: {
    addItem() {
      console.log('this.getdata')
      
      var myDate = new Date();
      // var mytime=myDate.toLocaleTimeString();     //获取当前时间
      // 获取日期与时间
      
      this.activities.push({title:this.title.join(" and "),
        content: this.content,
        timestamp: myDate.toLocaleString(),
      });
      
    },
    delItem() {
      this.activities.pop({});
    },
    editlog(content) {
      this.dialogFormVisible = true;
      console.log(content);
    },
  },
};
</script>