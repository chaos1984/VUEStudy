<template>
<v-card>
<v-table width="500" height="300" bgcolor="green" cellspacing="1" >
      <tr bgcolor="white">
          <td>1</td>
          <td>2</td>
          <td>3</td>
          <td>4</td>
      </tr>
      <tr bgcolor="white">
          <td>5</td>
           <td>6</td>
           <td>7</td>
           <td>8</td>
       </tr>
       <tr bgcolor="white">
           <td></td>
           <td></td>
           <td></td>
           <td></td>
       </tr>
       <tr bgcolor="white">
           <td></td>
           <td></td>
           <td></td>
           <td></td>
       </tr>
   </v-table>
</v-card> 
</template>

<script>
    import {mapState} from 'vuex';
    export default {
      data: () => ({
        
      }),
      computed:{
      ...mapState({
        CurrentForm : state => state.form,
        })
      },
    }
 
</script>