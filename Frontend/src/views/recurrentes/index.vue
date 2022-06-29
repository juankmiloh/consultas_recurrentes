<template>
  <div class="app-container">
    <el-row class="cont-row">
      <el-col :span="24">
        <aside>
          <span class="text-header">
            <b>Consultas recurrentes</b>
          </span>
        </aside>
      </el-col>
    </el-row>
    <el-form
      ref="modalform"
      :model="model"
      :rules="rulesform"
      label-width="160px"
      :label-position="x.matches ? 'top' : 'top'"
      class="demo-ruleForm"
    >
      <el-card class="box-card">
        <el-row :gutter="20">
          <el-col v-for="component in domcomponents" :key="component.prop" :span="8" :xs="24" style="border: 0px solid;">
            <el-form-item :prop="component.prop">
              <span v-if="component.type === 'select'">
                <el-select
                  v-model="model[component.prop]"
                  filterable
                  :placeholder="component.placeholder"
                  class="control-modal"
                  clearable
                  :disabled="component.disabled"
                >
                  <span>
                    <el-option
                      v-for="item in datacontrol[component.prop]"
                      :key="item.id"
                      :label="item.nombre"
                      :value="item.id"
                    />
                  </span>
                </el-select>
              </span>
            </el-form-item>
          </el-col>
        </el-row>
      </el-card>
      <el-card style="margin-top: 1%;">
        <el-table
          :data="tableData"
          style="width: 100%"
        >
          <el-table-column
            prop="date"
            label="Fecha"
            width="180"
          />
          <el-table-column
            prop="name"
            label="Nombre"
            width="180"
          />
          <el-table-column
            prop="address"
            label="Dirección"
          />
        </el-table>
      </el-card>
      <el-card style="text-align: left; margin-top: 1%;">
        <el-form-item>
          <el-button type="success" style="width: 15%;" @click="handleForm('modalform')">Ejecutar</el-button>
          <!-- <el-button @click="handleCancel()">Cancelar</el-button> -->
        </el-form-item>
      </el-card>
    </el-form>
  </div>
</template>

<script>
import { CONSTANTS } from './constants/constants'

export default {
  data() {
    return {
      model: CONSTANTS.formItem,
      domcomponents: CONSTANTS.domItem,
      datacontrol: CONSTANTS.dataFormItem,
      rulesform: CONSTANTS.rulesFormItem,
      x: '',
      tableData: [{
        date: '2016-05-03',
        name: 'Tom',
        address: 'No. 189, Grove St, Los Angeles'
      }, {
        date: '2016-05-02',
        name: 'Tom',
        address: 'No. 189, Grove St, Los Angeles'
      }, {
        date: '2016-05-04',
        name: 'Tom',
        address: 'No. 189, Grove St, Los Angeles'
      }, {
        date: '2016-05-01',
        name: 'Tom',
        address: 'No. 189, Grove St, Los Angeles'
      }]
    }
  },
  created() {
    this.x = window.matchMedia('(max-width: 800px)')
  },
  methods: {
    async handleForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          console.log('MODELO -> ', this.model)
        } else {
          console.log('error submit!!')
        }
      })
    },
    handleCancel() {
      this.$refs['modalform'].resetFields()
    }
  }
}
</script>

<style>
.cont-row {
  text-align: center;
}
.text-header {
  color: black;
  font-size: xx-large;
}
</style>

<style lang="scss" scoped>

// Pantallas superiores a 800px (PC)
@media screen and (min-width: 800px) {
  .control-modal {
    width: 100%;
  }
}

// Pantallas inferiores a 800px (mobile)
@media screen and (max-width: 800px) {
  .control-modal {
    width: 95%;
  }
}
</style>
