<template>
  <div class="app-container">
    <el-row class="cont-row">
      <el-col :span="24">
        <aside>
          <span class="text-header">
            <b>Consultas Recurrentes</b>
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
                  :multiple="component.multiple"
                  @change="validateSelect(component.prop, $event,datacontrol[component.prop])"
                >
                  <span>
                    <el-option
                      v-for="item in datacontrol[component.prop]"
                      :key="item.value"
                      :label="item.option"
                      :value="item.value"
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
          ref="multipleTable"
          v-loading="loading"
          border
          fit
          highlight-current-row
          :data="tableData"
          @selection-change="handleSelectionChange"
        >
          <el-table-column type="selection" align="center" />
          <el-table-column
            v-for="column in tableColumns"
            :key="column.label"
            :label="column.label"
            :prop="column.prop"
            align="center"
            :width="column.width"
          >
            <template slot-scope="scope">
              {{ scope.row[column.prop] }}
            </template>
          </el-table-column>
        </el-table>
      </el-card>
      <el-card style="text-align: left; margin-top: 1%;">
        <el-form-item>
          <el-button type="success" class="btn-exec" @click="handleForm('modalform')">Ejecutar</el-button>
          <!-- <el-button @click="handleCancel()">Cancelar</el-button> -->
        </el-form-item>
      </el-card>
    </el-form>
  </div>
</template>

<script>
import { CONSTANTS } from './constants/constants'
import { getServicio } from '@/api/recurrentes/servicio'
import { getConsulta, getConsultaDetalle } from '@/api/recurrentes/consulta'
import { getEmpresa } from '@/api/recurrentes/empresa'
import { getPrueba } from '@/api/recurrentes/prueba'

export default {
  data() {
    return {
      model: {
        servicio: '',
        consulta: '',
        idempresa: '',
        ano: '',
        mes: ''
      },
      domcomponents: CONSTANTS.domItem,
      datacontrol: CONSTANTS.dataFormItem,
      rulesform: CONSTANTS.rulesFormItem,
      tableColumns: CONSTANTS.tableColumns,
      loading: false,
      multipleSelection: [],
      // tableData: CONSTANTS.tableData,
      tableData: [],
      x: ''
    }
  },
  created() {
    this.x = window.matchMedia('(max-width: 800px)')
    this.getAllServicios()
    this.getAnios()
    this.getMes()
    this.getPruebas()
  },
  methods: {
    handleSelectionChange(val) {
      // console.log(val)
      this.multipleSelection = val
    },
    validateSelect(action, param, component) {
      console.log('action >> ', action, ' >> param >> ', param)
      // console.log('componente >> ', component)
      // objCriterio permite obtener el idCriterio de la consulta para determinar la obligatoriedad del parametro empresa, cuando es 1 no es obligatorio dicho parametro
      const objCriterio = component.find(consulta => consulta.value === param)
      // console.log('criterio >> ', criterio)

      if (action === 'servicio') {
        this.model.consulta = ''
        this.model.idempresa = ''
        this.getConsultaServicio(param)
        this.getEmpresas(param)
      } if (action === 'consulta') {
        // console.log('criterio >> ', objCriterio.criterio)
        this.domcomponents[2].disabled = false
        this.rulesform.idempresa[0].required = true

        // Esta condicional se establece para deshabilitar la lista relacionada a la empresa y evitar la activacion de la regla de obligatoriedad
        if (objCriterio.criterio === 1) {
          this.domcomponents[2].disabled = true
          this.rulesform.idempresa[0].required = false
        }
        this.getDetalleCategoria(param)
      } else {
        return 0
      }
    },
    getAnios() {
      this.datacontrol.ano = []
      const today = new Date()
      const year = today.getFullYear()
      for (let index = 2013; index <= year; index++) {
        this.datacontrol.ano.unshift({ value: index, option: index })
      }
    },
    getMes() {
      this.datacontrol.mes = []
      const meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
      for (let index = 0; index < meses.length; index++) {
        this.datacontrol.mes.push({ value: index + 1, option: meses[index] })
      }
    },
    async getAllServicios() {
      await getServicio().then((response) => {
        // console.log('response servicio :>> ', response)
        this.datacontrol.servicio = response
      })
    },
    async getConsultaServicio(idservicio) {
      // console.log('idservicio :>> ', idservicio)
      await getConsulta(idservicio).then((response) => {
        // console.log('response consulta :>> ', response)
        this.datacontrol.consulta = response
      })
    },
    async getDetalleCategoria(idcategoria) {
      // console.log('idcategoria :>> ', idcategoria)
      await getConsultaDetalle(idcategoria).then((response) => {
        // console.log('response consultaDetalle :>> ', response)
        this.tableData = response
      })
    },
    async getEmpresas(idservicio) {
      // console.log('idservicio :>> ', idservicio)
      await getEmpresa(idservicio).then((response) => {
        // console.log('response empresas :>> ', response)
        this.datacontrol.idempresa = response
      })
    },
    async getPruebas() {
      // console.log('idservicio :>> ', idservicio)
      await getPrueba().then((response) => {
        console.log('response prueba :>> ', response)
        // this.datacontrol.idempresa = response
      })
    },
    async getShortexecution(iterator) {
      // console.log('getShortexecution -> ', iterator)
      const url = `${process.env.VUE_APP_BASE_API}/shortexecution?procedimiento=${iterator.procedimiento}&ano=${this.model.ano}&mes=${this.model.mes}&idempresa=${this.model.idempresa}&idconsulta=${iterator.id_detalle}`
      // console.log('URL :>> ', url)
      window.open(url, '_self') // Linea para llamar el servicio que genera el .CSV
    },
    async handleForm(formName) {
      // se activa cuando se presiona el boton ejecutar y valida las reglas
      this.$refs[formName].validate((valid) => {
        if (valid) {
          // console.log('model :>> ', this.model)

          if (this.multipleSelection.length) {
            let contador = 0
            for (const iterator of this.multipleSelection) { // Se recorre la cantidad de filas seleccionadas en la tabla
              setTimeout(this.getShortexecution, contador * 1000, iterator) // Se genera el .CSV por cada registro de la tabla
              contador += 1
            }
          } else {
            this.$message({
              message: 'Seleccione al menos un registro de la tabla',
              type: 'warning'
            })
          }
        } else {
          // console.log('error submit!!')
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
  .btn-exec {
    width: 15%;
  }
}

// Pantallas inferiores a 800px (mobile)
@media screen and (max-width: 800px) {
  .control-modal {
    width: 95%;
  }

  .btn-exec {
    width: 100%;
  }
}
</style>
