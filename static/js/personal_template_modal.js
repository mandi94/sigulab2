/**
 * Funciones validadoras del primer paso
 */

const requiredFieldMessage = 'Este campo es requerido'
const badYear1 = "No puede ser previa a la fecha de inicio o posterior a la fecha actual."

const current_year = (new Date).getFullYear()








/*
COLOCA EN INPUTS TODOS TUS CAMPOS
*/






const inputs = [
    'nombre_add', 'apellido_add', 'ci_add', 'email_add', 'email_alt_add', 'telefono_add',
    'pagina_web_add', 'categoria_add', 'cargo_add', 'fecha_ingreso_add', 'fecha_salida_add',
    'estatus_add', 'operador_add', 'celular_add', 'persona_contacto', 'contacto_emergencia_add', 'fecha_nacimiento_add',
    'direccion_add', 'gremio_add', 'fecha_ingreso_usb_add', 'fecha_ingreso_ulab_add',
    'fecha_ingreso_admin_publica_add', 'condicion_add', 'ubicacion_add', 'dependencia_add', 'rol_add',
    'fecha_inicio_1_add', 'fecha_final_1_add', 'cargo_hist_1_add', 'dependencia_hist_1_add', 'organizacion_1_add',
    'fecha_inicio_2_add', 'fecha_final_2_add', 'cargo_hist_2_add', 'dependencia_hist_2_add', 'organizacion_2_add',
    'fecha_inicio_3_add', 'fecha_final_3_add', 'cargo_hist_3_add', 'dependencia_hist_3_add', 'organizacion_3_add',
    'fecha_inicio_4_add', 'fecha_final_4_add', 'cargo_hist_4_add', 'dependencia_hist_4_add', 'organizacion_4_add',
    'fecha_inicio_5_add', 'fecha_final_5_add', 'cargo_hist_5_add', 'dependencia_hist_5_add', 'organizacion_5_add',
    // Competencias
    'competencia1_nombre', 'competencia2_nombre', 'competencia3_nombre', 'competencia4_nombre', 'competencia5_nombre',
    'competencia6_nombre', 'competencia7_nombre', 'competencia8_nombre', 'competencia9_nombre', 'competencia10_nombre',
    // Trabajos dirigidos
    'trabajo1_titulo_trabajo', 'trabajo1_anio', 'trabajo1_institucion', 'trabajo1_nivel',
    'trabajo2_titulo_trabajo', 'trabajo2_anio', 'trabajo2_institucion', 'trabajo2_nivel',
    'trabajo3_titulo_trabajo', 'trabajo3_anio', 'trabajo3_institucion', 'trabajo3_nivel',
    'trabajo4_titulo_trabajo', 'trabajo4_anio', 'trabajo4_institucion', 'trabajo4_nivel',
    'trabajo5_titulo_trabajo', 'trabajo5_anio', 'trabajo5_institucion', 'trabajo5_nivel',
]

const inputSelectorsAll = inputs.map(i => `[name="${i}"]`).join(',') +
    ", .pop-field";

// Funciones que validan toda la pagina 1 del formulario 
function validaPaginaWeb () {
    const $this = $('[name="pagina_web_add"]')
    if ($this.val() === '') {
        $this.popover('hide');
        return true;
    }
    if (!($this.val().match(/^((https?|ftp|smtp):\/\/)?(www.)?[a-z0-9]+\.[a-z]+(\/[a-zA-Z0-9#]+\/?)*$/))) {
        $this.attr('data-content', "Formato incorrecto de pagina web. Ejemplo: hola.com");
        $this.popover('show');
        $this.addClass('input-error');
        $this.attr("data-valido", "false");
        return false;
    }
    else {
        $this.removeClass('input-error');
        $this.popover('hide');
        $this.attr("data-valido", "true");
        return true;
    }
}

function validaEmailAlternativo () {
    const $this = $('[name="email_alt_add"]')
    if ($this.val() === '') {
        $this.popover('hide');
        return true;
    }
    if (!($this.val().match(/^(([^<>()\[\]\.,;:\s@\"]+(\.[^<>()\[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/))){
        $this.attr("data-content", "El correo no tiene el formato correcto. Ejemplo: hola_mundo@dominio.com");
        console.log($this.popover('show'));
        $this.addClass('input-error');
        $this.attr("data-valido", "false");
        return false;
    }
    else {
        $this.removeClass('input-error');
        $this.attr("data-valido", "true");
        $this.popover('hide');
        return true;
    }
}

function validaOperador () {
    const $this = $('[name="operador_add"]')
    if (!$this.val()) {
        $this.attr('data-content', requiredFieldMessage);
        $this.popover('show');
        $this.addClass('input-error');
        $this.attr("data-valido", "false");
        return false;
    }
    else {
        $this.removeClass('input-error');
        $this.attr("data-valido", "true");
        $this.popover('hide');
        return true;
    }
}

function validaCelular () {
    const $this = $('[name="celular_add"]')
    const val = $this.val().replace(/-/g, '')
    if (val === '') {
        $this.attr('data-content', requiredFieldMessage);
        $this.popover('show');
        $this.addClass('input-error');
        $this.attr("data-valido", "false");
        return false;
    }
    if (!(val.match(/^\d{7}$/gm))) { // Extension de 1 a 4 digitos
        $this.attr('data-content', 'El número de celular tiene el formato incorrecto. Ejemplo 1234567');
        $this.popover('show');
        $this.addClass('input-error');
        $this.attr("data-valido", "false");
        return false;
    }
    else {
        $this.removeClass('input-error');
        $this.attr("data-valido", "true");
        $this.popover('hide');
        return true;
    }
}

function validaDireccionHab () {
    const $this = $('[name="direccion_add"]')
    if ($this.val() === '') {
        $this.attr("data-content", requiredFieldMessage);
        $this.popover('show');
        $this.addClass('input-error');
        return false;
    }
    else {
        $this.removeClass('input-error');
        $this.popover('hide');
        return true;
    }
}

function validaTelefonoResidencial (){
    const $this = $('[name="telefono_add"]')
    const val = $this.val().replace(/[()-]/g, '')
    if (val === '') {
        $this.attr("data-content", requiredFieldMessage);
        $this.addClass('input-error');
        $this.attr("data-valido", "false");
        $this.popover('show')
        return false;
    }
    if (!(val.match(/^\d{11}$/gm))){
        $this.attr("data-content", "El teléfono tiene el formato incorrecto. Ejemplo: 02121234567");
        $this.addClass('input-error');
        $this.attr("data-valido", "false");
        $this.popover('show');
        return false;
    }
    else {
        $this.removeClass('input-error');
        $this.attr("data-valido", "true");
        $this.popover('hide');
        return true;
    }
}

function validaPersonaContacto () {
    const $this = $('[name="persona_contacto"]')
    if ($this.val() === '') {
        $this.attr("data-content", requiredFieldMessage);
        $this.popover('show');
        $this.addClass('input-error');
        return false;
    }
    else {
        $this.removeClass('input-error');
        $this.popover('hide');
        return true;
    }

}

function validaContactoEmergencia () {
    const $this = $('[name="contacto_emergencia_add"]')
    const val = $this.val().replace(/[()-]/g, '')
    if (val === '') {
        $this.attr("data-content", requiredFieldMessage);
        $this.addClass('input-error');
        $this.attr("data-valido", "false");
        $this.popover('show');
        return false;
    }
    if (!val.match(/\d{11}$/)) { 
        $this.attr("data-content", 'El contacto de emergencia debe tener solo números. Ejemplo: 02121234567');
        $this.popover('show');
        $this.addClass('input-error');
        return false;
    }
    else {
        $this.removeClass('input-error');
        $this.popover('hide');
        return true;
    }
}

function validaFechaNac(){
    const $this = $('[name="fecha_nacimiento_add"]');
    if ($this.val() === ""){
        $this.attr("data-content", requiredFieldMessage);
        $this.addClass('input-error');
        $this.attr("data-valido", 'false');
        $this.popover('show');
        return false;
    }
    else{
        $this.removeClass('input-error');
        $this.popover('hide');
        return true;
    }
}

const validadoresPrimerPaso = [
    validaPaginaWeb,
    validaEmailAlternativo,
    validaOperador,
    validaCelular,
    validaDireccionHab,
    validaTelefonoResidencial,
    validaPersonaContacto,
    validaContactoEmergencia,
    validaFechaNac
]

// Funciones que validan la segunda pagina 
function validaEstatus(){
    const $this = $('[name="estatus_add"]')
    if ($this.val() === null){
        $this.attr("data-content", requiredFieldMessage);
        $this.addClass('input-error');
        $this.attr("data-valido", 'false');
        $this.popover('show');
        return false
    }
    else {
        $this.removeClass('input-error');
        $this.popover('hide');
        return true;
    }
}

function validaCategoria(){
    const $this = $('[name="categoria_add"]')
    if ($this.val() === null){
        $this.attr("data-content", requiredFieldMessage);
        $this.addClass('input-error');
        $this.attr("data-valido", 'false');
        $this.popover('show');
        return false
    }
    else {
        $this.removeClass('input-error');
        $this.popover('hide');
        return true;
    }
}

function validaCondicion(){
    const $this = $('[name="condicion_add"]')
    if ($this.val() === null){
        $this.attr("data-content", requiredFieldMessage);
        $this.addClass('input-error');
        $this.attr("data-valido", 'false');
        $this.popover('show');
        return false
    }
    else {
        $this.removeClass('input-error');
        $this.popover('hide');
        return true;
    }
}

function validaFechaIngreso(){
    const $this = $('[name="fecha_ingreso_add"]');
    if ($this.val() === ""){
        $this.attr("data-content", requiredFieldMessage);
        $this.addClass('input-error');
        $this.attr("data-valido", 'false');
        $this.popover('show');
        return false;
    }
    else if (!moment(voltearFecha($this.val())).isSameOrBefore(moment().format("YYYY-MM-DD"))){
        $this.attr("data-content", 'La fecha de ingreso tiene que ser antes de la fecha de hoy u hoy');
        $this.addClass('input-error');
        $this.attr("data-valido", 'false');
        $this.popover('show');
        return false;
    }
    else{
        $this.removeClass('input-error');
        $this.popover('hide');
        return true;
    }
}

// Funcion que se encarga de voltear la fecha y se muestre en el formato pedido
function voltearFecha(fecha){
    if (fecha !== ""){
        var dia = fecha.substr(0,2);
        var mes = fecha.substr(3,2);
        var anio = fecha.substr(6,10);
    
        var fecha = anio + "-" + mes + "-" + dia;
        
        return fecha;
    }
    else {
        return "";
    }
}

function validaFechaSalida(){
    const $this = $('[name="fecha_salida_add"]');
    const fecha_inicio = voltearFecha($('[name="fecha_ingreso_add"]').val());
    const fecha_final = voltearFecha($this.val());

    if (fecha_inicio !== "" && fecha_final !== "" && !moment(fecha_inicio).isSameOrBefore(fecha_final)){
        $this.attr("data-content", "La fecha de egreso tiene que ser despues que la fecha de ingreso o igual a esta.");
        $this.addClass('input-error');
        $this.attr("data-valido", 'false');
        $this.popover('show');
        return false
    }
    else{
        $this.removeClass('input-error');
        $this.popover('hide');
        return true;
    }
}

function validaFechaIngresoUSB(){
    const $this = $('[name="fecha_ingreso_usb_add"]');
    const fecha_ingreso_ulab = voltearFecha($('[name="fecha_ingreso_ulab_add"]').val());
    const fecha_ingreso_usb = voltearFecha($this.val());

    if ($this.val() === "" && $('[name="categoria_add"]').val() !== 'Fijo'){
        $this.attr("data-content", requiredFieldMessage);
        $this.addClass('input-error');
        $this.attr("data-valido", 'false');
        $this.popover('show');
        return false
    }
    else if (fecha_ingreso_ulab !== "" && !(moment(fecha_ingreso_usb).isBefore(fecha_ingreso_ulab) || moment(fecha_ingreso_usb).isSame(fecha_ingreso_ulab))){
        $this.attr("data-content", "La fecha de ingreso al USB tiene que ser antes de la fecha de ingreso al ULAB");
        $this.addClass('input-error');
        $this.popover('show');
        return false;
    }
    else{
        $this.removeClass('input-error');
        $this.popover('hide');
        return true;
    }
}

function validaFechaIngresoUlab(){
    const $this = $('[name="fecha_ingreso_ulab_add"]');
    const fecha_inicio = voltearFecha($('[name="fecha_ingreso_add"]').val());
    const fecha_ingreso_ulab = voltearFecha($this.val());

    if ($this.val() === "" && $('[name="categoria_add"]').val() !== 'Fijo'){
        $this.attr("data-content", requiredFieldMessage);
        $this.addClass('input-error');
        $this.attr("data-valido", 'false');
        $this.popover('show');
        return false;
    }
    else if (fecha_inicio !== "" && !(moment(fecha_ingreso_ulab).isBefore(fecha_inicio) || moment(fecha_ingreso_ulab).isSame(fecha_inicio))) {
        $this.attr("data-content", "La fecha de ingreso al ULAB tiene que ser antes que la fecha de ingreso");
        $this.addClass('input-error');
        $this.popover('show');
        return false;
    }
    else{
        $this.removeClass('input-error');
        $this.popover('hide');
        return true;
    }
}

function validaFechaIngresoAdminPubl(){
    const $this = $('[name="fecha_ingreso_admin_publica_add"]');
    const fecha_ingreso_usb = voltearFecha($('[name="fecha_ingreso_usb_add"]').val());
    const fecha_ingreso_admin_pub = voltearFecha($this.val());

    if ($this.val() === "" && $('[name="categoria_add"]').val() !== 'Fijo'){
        $this.attr("data-content", requiredFieldMessage);
        $this.addClass('input-error');
        $this.attr("data-valido", 'false');
        $this.popover('show');
        return false;
    }
    else if (fecha_ingreso_usb !== "" && !(moment(fecha_ingreso_admin_pub).isBefore(fecha_ingreso_usb) || moment(fecha_ingreso_admin_pub).isSame(fecha_ingreso_usb))){
        $this.attr("data-content", "La fecha de ingreso a la administración pública debe ser antes de la fecha de ingreso a la USB");
        $this.addClass('input-error');
        $this.popover('show');
        return false;
    }
    else{
        $this.removeClass('input-error');
        $this.popover('hide');
        return true;
    }
}

const validadoresSegundoPasoFijo = [
    validaEstatus,
    validaCategoria,
    validaCondicion,
    validaFechaIngresoUSB,
    validaFechaIngresoUlab,
    validaFechaIngresoAdminPubl
]

const validadoresSegundoPaso = [
    validaEstatus,
    validaCategoria,
    validaCondicion,
    validaFechaIngreso,
    validaFechaSalida
]

// Funciones para validar la tercera parte del formulario

function validarCargo(){
    const $this = $('[name="cargo_add"]');
    if ($this.val() === ''){
        $this.attr("data-content", requiredFieldMessage);
        $this.addClass('input-error');
        $this.attr("data-valido", "false");
        $this.popover('show');
        return false;
    } 
    else {
        $this.removeClass('input-error');
        $this.popover('hide');
        return true;
    }
}

function validarGremio(){
    const $this = $('[name="gremio_add"]');
    if ($this.val() === null){
        $this.attr("data-content", requiredFieldMessage);
        $this.addClass('input-error');
        $this.attr("data-valido", "false");
        $this.popover('show');
        return false;
    }
    else {
        $this.removeClass('input-error');
        $this.popover('hide');
        return true;
    }
}

function validarUbicacion(){
    const $this = $('[name="ubicacion_add"]');
    if ($this.val() === null){
        $this.attr("data-content", requiredFieldMessage);
        $this.addClass('input-error');
        $this.attr("data-valido", "false");
        $this.popover('show');
        return false;
    }
    else {
        $this.removeClass('input-error');
        $this.popover('hide');
        return true;
    }
}

function validarRol(){
    const $this = $('[name="rol_add"]');
    if ($this.val() === null){
        $this.attr("data-content", requiredFieldMessage);
        $this.addClass('input-error');
        $this.attr("data-valido", "false");
        $this.popover('show');
        return false;
    }
    else {
        $this.removeClass('input-error');
        $this.popover('hide');
        return true;
    }
}

const validadoresTercerPaso = [
    validarCargo,
    validarGremio,
    validarUbicacion,
    validarRol
]

// Funciones para validar los campos de historial de trabajo

function validaTrabajo1() {
    // Campos del formulario de un trabajo
    const $fechIn= $('[name="fecha_inicio_1_add"]');
    const $fechFin = $('[name="fecha_final_1_add');
    const $depen = $('[name="dependencia_hist_1_add"]');
    const $org = $('[name="organizacion_1_add"]');
    const $cargo = $('[name="cargo_hist_1_add"]');
    var arreglo = [$fechIn, $fechFin, $depen, $org, $cargo]
    var validacion = true;
    //Si uno de los campos de un trabajo esta lleno entonces los
    // demás también son requeridos
    for (var i=0; i<arreglo.length; i++) {
        if (arreglo[i].val() !== "") {
            for (var j=0; j<arreglo.length; j++) {
                if (arreglo[j].val() === ""){
                    arreglo[j].attr("data-content", requiredFieldMessage);
                    arreglo[j].addClass('input-error');
                    arreglo[j].attr("data-valido", "false");
                    arreglo[j].popover('show');
                    validacion = false;
                    break;
                } else {
                    arreglo[j].removeClass('input-error');
                    arreglo[j].popover('hide');
                }
            }
            break;
        }
    }
    return validacion;
}

function validaTrabajo2() {
    const $fechIn= $('[name="fecha_inicio_2_add"]');
    const $fechFin = $('[name="fecha_final_2_add');
    const $depen = $('[name="dependencia_hist_2_add"]');
    const $org = $('[name="organizacion_2_add"]');
    const $cargo = $('[name="cargo_hist_2_add"]');
    var arreglo = [$fechIn, $fechFin, $depen, $org, $cargo]
    var validacion = true;

    for (var i=0; i<arreglo.length; i++) {
        if (arreglo[i].val() !== "") {
            for (var j=0; j<arreglo.length; j++) {
                if (arreglo[j].val() === ""){
                    arreglo[j].attr("data-content", requiredFieldMessage);
                    arreglo[j].addClass('input-error');
                    arreglo[j].attr("data-valido", "false");
                    arreglo[j].popover('show');
                    validacion = false;
                } else {
                    arreglo[j].removeClass('input-error');
                    arreglo[j].popover('hide');
                }
            }
            break;
        }
    }
    return validacion;
}

function validaTrabajo3() {
    const $fechIn= $('[name="fecha_inicio_3_add"]');
    const $fechFin = $('[name="fecha_final_3_add');
    const $depen = $('[name="dependencia_hist_3_add"]');
    const $org = $('[name="organizacion_3_add"]');
    const $cargo = $('[name="cargo_hist_3_add"]');
    var arreglo = [$fechIn, $fechFin, $depen, $org, $cargo]
    var validacion = true;

    for (var i=0; i<arreglo.length; i++) {
        if (arreglo[i].val() !== "") {
            for (var j=0; j<arreglo.length; j++) {
                if (arreglo[j].val() === ""){
                    arreglo[j].attr("data-content", requiredFieldMessage);
                    arreglo[j].addClass('input-error');
                    arreglo[j].attr("data-valido", "false");
                    arreglo[j].popover('show');
                    validacion = false;
                } else {
                    arreglo[j].removeClass('input-error');
                    arreglo[j].popover('hide');
                }
            }
            break;
        }
    }
    return validacion;
}

function validaTrabajo4() {
    const $fechIn= $('[name="fecha_inicio_4_add"]');
    const $fechFin = $('[name="fecha_final_4_add');
    const $depen = $('[name="dependencia_hist_4_add"]');
    const $org = $('[name="organizacion_4_add"]');
    const $cargo = $('[name="cargo_hist_4_add"]');
    var arreglo = [$fechIn, $fechFin, $depen, $org, $cargo]
    var validacion = true;

    for (var i=0; i<arreglo.length; i++) {
        if (arreglo[i].val() !== "") {
            for (var j=0; j<arreglo.length; j++) {
                if (arreglo[j].val() === ""){
                    arreglo[j].attr("data-content", requiredFieldMessage);
                    arreglo[j].addClass('input-error');
                    arreglo[j].attr("data-valido", "false");
                    arreglo[j].popover('show');
                    validacion = false;
                } else {
                    arreglo[j].removeClass('input-error');
                    arreglo[j].popover('hide');
                }
            }
            break;
        }
    }
    return validacion;
}

function validaTrabajo5() {
    const $fechIn= $('[name="fecha_inicio_5_add"]');
    const $fechFin = $('[name="fecha_final_5_add');
    const $depen = $('[name="dependencia_hist_5_add"]');
    const $org = $('[name="organizacion_5_add"]');
    const $cargo = $('[name="cargo_hist_5_add"]');
    var arreglo = [$fechIn, $fechFin, $depen, $org, $cargo]
    var validacion = true;

    for (var i=0; i<arreglo.length; i++) {
        if (arreglo[i].val() !== "") {
            for (var j=0; j<arreglo.length; j++) {
                if (arreglo[j].val() === ""){
                    arreglo[j].attr("data-content", requiredFieldMessage);
                    arreglo[j].addClass('input-error');
                    arreglo[j].attr("data-valido", "false");
                    arreglo[j].popover('show');
                    validacion = false;
                } else {
                    arreglo[j].removeClass('input-error');
                    arreglo[j].popover('hide');
                }
            }
            break;
        }
    }
    return validacion;
}

function validaFechaInicio1(){
    const $this = $('[name="fecha_inicio_1_add"]');
    if ($this.val() !== ""){
        if (!moment(voltearFecha($this.val())).isSameOrBefore(moment().format("YYYY-MM-DD"))){
            $this.attr("data-content", 'La fecha tiene que ser antes de la fecha de hoy u hoy');
            $this.addClass('input-error');
            $this.attr("data-valido", 'false');
            $this.popover('show');
            return false;
        }
        else{
            $this.removeClass('input-error');
            $this.popover('hide');
            return true;
        }
    } else {
        return true;
    }
}

function validaFechaFin1(){
    const $this = $('[name="fecha_final_1_add"]');
    const fecha_inicio = voltearFecha($('[name="fecha_inicio_1_add"]').val());
    const fecha_final = voltearFecha($this.val());


    if (fecha_inicio !== "" && fecha_final !== "" && (!moment(fecha_inicio).isSameOrBefore(fecha_final) || !moment(fecha_final).isSameOrBefore(moment().format("YYYY-MM-DD")) ) ){
        $this.attr("data-content", "La fecha de egreso tiene que ser despues que la fecha de ingreso o igual a esta");
        $this.addClass('input-error');
        $this.attr("data-valido", 'false');
        $this.popover('show');
        return false
    }
    else{
        $this.removeClass('input-error');
        $this.popover('hide');
        return true;
    }
}

function validaFechaInicio2(){
    const $this = $('[name="fecha_inicio_2_add"]');
    if ($this.val() != ""){
        if (!moment(voltearFecha($this.val())).isSameOrBefore(moment().format("YYYY-MM-DD"))){
            $this.attr("data-content", 'La fecha tiene que ser antes de la fecha de hoy');
            $this.addClass('input-error');
            $this.attr("data-valido", 'false');
            $this.popover('show');
            return false;
        }
        else{
            $this.removeClass('input-error');
            $this.popover('hide');
            return true;
        }
    } else {
        return true;
    }
}

function validaFechaFin2(){
    const $this = $('[name="fecha_final_2_add"]');
    const fecha_inicio = voltearFecha($('[name="fecha_inicio_2_add"]').val());
    const fecha_final = voltearFecha($this.val());

    if (fecha_inicio !== "" && fecha_final !== "" && (!moment(fecha_inicio).isSameOrBefore(fecha_final) || !moment(fecha_final).isSameOrBefore(moment().format("YYYY-MM-DD")) ) ){
        $this.attr("data-content", "La fecha de egreso tiene que ser despues que la fecha de ingreso o igual a esta");
        $this.addClass('input-error');
        $this.attr("data-valido", 'false');
        $this.popover('show');
        return false
    }
    else{
        $this.removeClass('input-error');
        $this.popover('hide');
        return true;
    }
}

function validaFechaInicio3(){
    const $this = $('[name="fecha_inicio_3_add"]');
    if ($this.val() != ""){
        if (!moment(voltearFecha($this.val())).isSameOrBefore(moment().format("YYYY-MM-DD"))){
            $this.attr("data-content", 'La fecha tiene que ser antes de la fecha de hoy');
            $this.addClass('input-error');
            $this.attr("data-valido", 'false');
            $this.popover('show');
            return false;
        }
        else{
            $this.removeClass('input-error');
            $this.popover('hide');
            return true;
        }
    } else {
        return true;
    }
}

function validaFechaFin3(){
    const $this = $('[name="fecha_final_3_add"]');
    const fecha_inicio = voltearFecha($('[name="fecha_inicio_3_add"]').val());
    const fecha_final = voltearFecha($this.val());

    if (fecha_inicio !== "" && fecha_final !== "" && (!moment(fecha_inicio).isSameOrBefore(fecha_final) || !moment(fecha_final).isSameOrBefore(moment().format("YYYY-MM-DD")) ) ){
        $this.attr("data-content", "La fecha de egreso tiene que ser despues que la fecha de ingreso o igual a esta");
        $this.addClass('input-error');
        $this.attr("data-valido", 'false');
        $this.popover('show');
        return false
    }
    else{
        $this.removeClass('input-error');
        $this.popover('hide');
        return true;
    }
}

function validaFechaInicio4(){
    const $this = $('[name="fecha_inicio_4_add"]');
    if ($this.val() != ""){
        if (!moment(voltearFecha($this.val())).isSameOrBefore(moment().format("YYYY-MM-DD"))){
            $this.attr("data-content", 'La fecha tiene que ser antes de la fecha de hoy');
            $this.addClass('input-error');
            $this.attr("data-valido", 'false');
            $this.popover('show');
            return false;
        }
        else{
            $this.removeClass('input-error');
            $this.popover('hide');
            return true;
        }
    } else {
        return true;
    }
}

function validaFechaFin4(){
    const $this = $('[name="fecha_final_4_add"]');
    const fecha_inicio = voltearFecha($('[name="fecha_inicio_4_add"]').val());
    const fecha_final = voltearFecha($this.val());

    if (fecha_inicio !== "" && fecha_final !== "" && (!moment(fecha_inicio).isSameOrBefore(fecha_final) || !moment(fecha_final).isSameOrBefore(moment().format("YYYY-MM-DD")) ) ){
        $this.attr("data-content", "La fecha de egreso tiene que ser despues que la fecha de ingreso o igual a esta");
        $this.addClass('input-error');
        $this.attr("data-valido", 'false');
        $this.popover('show');
        return false
    }
    else{
        $this.removeClass('input-error');
        $this.popover('hide');
        return true;
    }
}

function validaFechaInicio5(){
    const $this = $('[name="fecha_inicio_5_add"]');
    if ($this.val() != ""){
        if (!moment(voltearFecha($this.val())).isSameOrBefore(moment().format("YYYY-MM-DD"))){
            $this.attr("data-content", 'La fecha tiene que ser antes de la fecha de hoy');
            $this.addClass('input-error');
            $this.attr("data-valido", 'false');
            $this.popover('show');
            return false;
        }
        else{
            $this.removeClass('input-error');
            $this.popover('hide');
            return true;
        }
    } else {
        return true;
    }
}

function validaFechaFin5(){
    const $this = $('[name="fecha_final_5_add"]');
    const fecha_inicio = voltearFecha($('[name="fecha_inicio_5_add"]').val());
    const fecha_final = voltearFecha($this.val());

    if (fecha_inicio !== "" && fecha_final !== "" && (!moment(fecha_inicio).isSameOrBefore(fecha_final) || !moment(fecha_final).isSameOrBefore(moment().format("YYYY-MM-DD")) ) ){
        $this.attr("data-content", "La fecha de egreso tiene que ser despues que la fecha de ingreso o igual a esta");
        $this.addClass('input-error');
        $this.attr("data-valido", 'false');
        $this.popover('show');
        return false;
    }
    else{
        $this.removeClass('input-error');
        $this.popover('hide');
        return true;
    }
}

const validadoresQuintoPaso = [
    validaTrabajo1,
    validaTrabajo2,
    validaTrabajo3,
    validaTrabajo4,
    validaTrabajo5,
    validaFechaInicio1,
    validaFechaFin1,
    validaFechaInicio2,
    validaFechaFin2,
    validaFechaInicio3,
    validaFechaFin3,
    validaFechaInicio4,
    validaFechaFin4,
    validaFechaInicio5,
    validaFechaFin5
]

function validaCompetencia(){
    var valid=true;
    for(var i=1; i<11;i++){
        if($('#competencia'+i+'-container').is(':hidden'))
            continue;

        var nombre = $('#competencia'+i+'_nombre');
        var chosenval = $('#competencia'+i+'_categoria').trigger("chosen-updated").val().length;
        chosen_container = $('#competencia'+i+'_categoria_chosen');
        if (chosenval == 0){
            chosen_container.attr("data-content", requiredFieldMessage);
            chosen_container.addClass('input-error');
            chosen_container.attr("data-valido", 'false');
            chosen_container.popover('show');
            valid = valid && false
        }
        else {
            chosen_container.removeClass('input-error');
            chosen_container.popover('hide');
            valid = valid && true;
        }
        if (nombre.val()==='') {
            nombre.attr("data-content", requiredFieldMessage);
            nombre.popover('show');
            nombre.addClass('input-error');
            valid = valid && false;
        }
        else {
            nombre.removeClass('input-error');
            nombre.popover('hide');
            valid = valid && true;
        }
    }
    return valid;

}
const validadoresCuartoPaso = [
    validaCompetencia
]

// ESCRIBE AQUI TUS FUNCIONES

function validaTrabajosDirigidos(){
    var valid=true;
    var yyyy = current_year
    for(var i=1; i<6;i++){
        if($('#trabajo-container'+i).is(':hidden'))
            continue;

        var titulo_trabajo = $('#trabajo'+i+'_titulo_trabajo');
        var anio = $('#trabajo'+i+'_anio');
        var estudiantes = $('#trabajo'+i+'_estudiantes');
        var institucion = $('#trabajo'+i+'_institucion');
        var chosenval = $('#trabajo'+i+'_nivel').trigger("chosen-updated").val().length;
        chosen_container = $('#trabajo'+i+'_nivel_chosen');

        if (chosenval == 0 && titulo_trabajo.val()==='' && anio.val()==='' && estudiantes.val()==='' && institucion.val()===''){
            chosen_container.removeClass('input-error');
            chosen_container.popover('hide');
            titulo_trabajo.removeClass('input-error');
            titulo_trabajo.popover('hide');
            anio.removeClass('input-error');
            anio.popover('hide');
            estudiantes.removeClass('input-error');
            estudiantes.popover('hide');
            institucion.removeClass('input-error');
            institucion.popover('hide');
            valid = valid && true;
            continue;
        }
        else {
            if (chosenval == 0){
                chosen_container.attr("data-content", requiredFieldMessage);
                chosen_container.addClass('input-error');
                chosen_container.attr("data-valido", 'false');
                chosen_container.popover('show');
                valid = valid && false;
            }
            else {
                chosen_container.removeClass('input-error');
                chosen_container.popover('hide');
                valid = valid && true;
            }
            if (titulo_trabajo.val()==='') {
                titulo_trabajo.attr("data-content", requiredFieldMessage);
                titulo_trabajo.popover('show');
                titulo_trabajo.addClass('input-error');
                valid = valid && false;
            }
            else {
                titulo_trabajo.removeClass('input-error');
                titulo_trabajo.popover('hide');
                valid = valid && true;
            }
            if (anio.val()==='') {
                anio.attr("data-content", requiredFieldMessage);
                anio.popover('show');
                anio.addClass('input-error');
                valid = valid && false;
            } else if (anio.val() > yyyy) {
                anio.attr("data-content", 'Ingrese un año menor o igual al actual');
                anio.popover('show');
                anio.addClass('input-error');
                valid = valid && false;
            } else {
                anio.removeClass('input-error');
                anio.popover('hide');
                valid = valid && true;
            }
            if (estudiantes.val()==='') {
                estudiantes.attr("data-content", requiredFieldMessage);
                estudiantes.popover('show');
                estudiantes.addClass('input-error');
                valid = valid && false;
            }
            else {
                estudiantes.removeClass('input-error');
                estudiantes.popover('hide');
                valid = valid && true;
            }
            if (institucion.val()==='') {
                institucion.attr("data-content", requiredFieldMessage);
                institucion.popover('show');
                institucion.addClass('input-error');
                valid = valid && false;
            }
            else {
                institucion.removeClass('input-error');
                institucion.popover('hide');
                valid = valid && true;
            }
        }

    }
    return valid;
}

// Auxiliares
function comparaFechas(fechaini, fechafin) {
    const fecha_inicio = voltearFecha(fechaini);
    const fecha_final = voltearFecha(fechafin);
    if (!fecha_inicio || !fecha_final) return true;
    if( !moment(fecha_inicio).isSameOrBefore(fecha_final) ) {
        return false
    }
    else if (!moment(fecha_final).isSameOrBefore(moment().format("YYYY-MM-DD"))){
        return false
    }
    else {
        return true;
    }
}

function validaEmpty(selector) {
    if ( selector.val()==='' ) {
        selector.attr('data-content', requiredFieldMessage);
        selector.popover('show');
        selector.addClass('input-error');
        return false;
    }
    else {
        selector.removeClass('input-error');
        selector.popover('hide');
        return true;
    }
}

// Sexto paso
function validaAdministrativas(){
    var valid=true;
    for(var i=1; i<6; i++){
        if($('#administrativa'+i+'-container').is(':hidden'))
            continue;
        var desde = $('#administrativa'+i+'_desde');
        var hasta = $('#administrativa'+i+'_hasta');
        var cargo = $('#administrativa'+i+'_cargo');
        var institucion = $('#administrativa'+i+'_institucion');
        valid = validaEmpty(desde) && valid;
        valid = validaEmpty(hasta) && valid;
        valid = validaEmpty(cargo) && valid;
        valid = validaEmpty(institucion) && valid;
        if (!comparaFechas(desde.val(), hasta.val())) {
            hasta.attr("data-content", badYear1)
            hasta.addClass('input-error');
            hasta.popover('toggle');
            valid = false;
        } else if(valid) {
            hasta.removeClass('input-error');
            hasta.popover('hide');
        }

    }
    return valid;

}

// Septimo Paso
function validaExtension(){
    var valid=true;
    for(var i=1; i<6; i++){
        if($('#extension'+i+'-container').is(':hidden'))
            continue;
        var desde = $('#extension'+i+'_desde');
        var hasta = $('#extension'+i+'_hasta');
        var cargo = $('#extension'+i+'_cargo');
        var nombre = $('#extension'+i+'_nombre');
        var institucion = $('#extension'+i+'_institucion');
        var descripcion = $('#extension'+i+'_descripcion');
        valid = validaEmpty(desde) && valid;
        valid = validaEmpty(hasta) && valid;
        valid = validaEmpty(cargo) && valid;
        valid = validaEmpty(nombre) && valid;
        valid = validaEmpty(institucion) && valid;
        valid = validaEmpty(descripcion) && valid;
        if (!comparaFechas(desde.val(), hasta.val())) {
            hasta.attr("data-content", badYear1)
            hasta.addClass('input-error');
            hasta.popover('toggle');
            valid = false;
        } else if(valid) {
            hasta.removeClass('input-error');
            hasta.popover('hide');
        }
        var chosen_container = $('#extension'+i+'_categoria_chosen');
        var chosenval = $('#extension'+i+'_categoria').trigger('chosen-updated').val().length;
        console.log(chosenval);
        if (chosenval == 0){
            chosen_container.attr("data-content", requiredFieldMessage);
            chosen_container.addClass('input-error');
            chosen_container.attr("data-valido", 'false');
            chosen_container.popover('show');
            valid = false;
        }
        else {
            chosen_container.removeClass('input-error');
            chosen_container.popover('hide');
        }
    }
    return valid;

}

function validaCursos(){
    var valid=true;
    for(var i=1; i<11; i++){
        if($('#evento-container'+i).is(':hidden'))
            continue;
        var anio = $('#evento'+i+'_anio');
        var formacion = $('#evento'+i+'_formacion');
        var dictadoPor = $('#evento'+i+'_dictadoPor');
        var horas = $('#evento'+i+'_horas');
        valid = validaEmpty(anio) && valid;
        valid = validaEmpty(formacion) && valid;
        valid = validaEmpty(dictadoPor) && valid;
        valid = validaEmpty(horas) && valid;
        var chosen_container = $('#evento'+i+'_categoria_chosen');
        var chosenval = $('#evento'+i+'_categoria').trigger('chosen-updated').val().length;
        console.log(chosenval);
        if (chosenval == 0){
            chosen_container.attr("data-content", requiredFieldMessage);
            chosen_container.addClass('input-error');
            chosen_container.attr("data-valido", 'false');
            chosen_container.popover('show');
            valid = false;
        }
        else {
            chosen_container.removeClass('input-error');
            chosen_container.popover('hide');
        }
        if (anio.val() > current_year) {
            anio.attr("data-content", 'Ingrese un año menor o igual al actual');
            anio.popover('show');
            anio.addClass('input-error');
            valid = valid && false;
        }
        else {
            anio.removeClass('input-error');
            anio.popover('hide');
            valid = valid && true;
        }

    }
    return valid;

}

function validaEstudios(){
    var valid=true;
    for(var i=1; i<6; i++){
        if($('#estudios-container'+i).is(':hidden'))
            continue;

        var nivel = $('#estudio'+i+'_nivel');
        var anio = $('#estudio'+i+'_anio');
        var titulo_estudio = $('#estudio'+i+'_titulo_estudio');
        var ubicacion = $('#estudio'+i+'_ubicacion');
        var institucion = $('#estudio'+i+'_institucion');
        // var categoria = $('#estudio'+i+'_categoria');
        var area = $('#estudio'+i+'_area');

        // valid = validaEmpty(nivel) && valid;
        valid = validaEmpty(anio) && valid;
        valid = validaEmpty(titulo_estudio) && valid;
        valid = validaEmpty(ubicacion) && valid;
        valid = validaEmpty(institucion) && valid;
        valid = validaEmpty(area) && valid;

        var chosen_container = $('#estudio'+i+'_categoria_chosen');
        var chosenval = $('#estudio'+i+'_categoria').trigger('chosen-updated').val().length;
        console.log(chosenval);
        if (chosenval == 0){
            chosen_container.attr("data-content", requiredFieldMessage);
            chosen_container.addClass('input-error');
            chosen_container.attr("data-valido", 'false');
            chosen_container.popover('show');
            valid = false;
        }
        else {
            chosen_container.removeClass('input-error');
            chosen_container.popover('hide');
        }
        if (anio.val() > current_year) {
            anio.attr("data-content", 'Ingrese un año menor o igual al actual');
            anio.popover('show');
            anio.addClass('input-error');
            valid = valid && false;
        }
        else {
            anio.removeClass('input-error');
            anio.popover('hide');
            valid = valid && true;
        }

    }
    return valid;

}
function validaMaterias(){
    var valid=true;
    for(var i=1; i<6; i++){
        if($('#materia-container'+i).is(':hidden'))
            continue;
        var desde = $('#materia'+i+'_fecha_inicio_materia');
        var hasta = $('#materia'+i+'_fecha_final_materia');
        var codigo = $('#materia'+i+'_codigo');
        var nombre = $('#materia'+i+'_nombre_materia');
        valid = validaEmpty(desde) && valid;
        valid = validaEmpty(hasta) && valid;
        valid = validaEmpty(codigo) && valid;
        valid = validaEmpty(nombre) && valid;
        if (!comparaFechas(desde.val(), hasta.val())) {
            hasta.attr("data-content", badYear1)
            hasta.addClass('input-error');
            hasta.popover('toggle');
            valid = false;
        } else if(valid) {
            hasta.removeClass('input-error');
            hasta.popover('hide');
        }
        var chosen_container = $('#materia'+i+'_area_chosen');
        var chosenval = $('#materia'+i+'_area').trigger('chosen-updated').val().length;
        if (chosenval == 0){
            chosen_container.attr("data-content", requiredFieldMessage);
            chosen_container.addClass('input-error');
            chosen_container.attr("data-valido", 'false');
            chosen_container.popover('show');
            valid = false;
        }
        else {
            chosen_container.removeClass('input-error');
            chosen_container.popover('hide');
        }
    }
    return valid;

}

function validaProyectos(){
    var valid=true;
    for(var i=1; i<11; i++){
        if($('#proyecto'+i+'_container').is(':hidden'))
            continue;
        console.log(i)
        var desde = $('#proyecto'+i+'_desde');
        var hasta = $('#proyecto'+i+'_hasta');
        var titulo = $('#proyecto'+i+'_titulo');
        var resultados = $('#proyecto'+i+'_resultados');
        var institucion = $('#proyecto'+i+'_institucion');
        var responsabilidad = $('#proyecto'+i+'_responsabilidad');
        valid = validaEmpty(desde) && valid;
        valid = validaEmpty(hasta) && valid;
        valid = validaEmpty(titulo) && valid;
        valid = validaEmpty(resultados) && valid;
        valid = validaEmpty(responsabilidad) && valid;
        valid = validaEmpty(institucion) && valid;
        if (!comparaFechas(desde.val(), hasta.val())) {
            hasta.attr("data-content", badYear1)
            hasta.addClass('input-error');
            hasta.popover('toggle');
            valid = false;
        } else if(valid) {
            hasta.removeClass('input-error');
            hasta.popover('hide');
        }
        var chosen_container = $('#proyecto'+i+'_categoria_chosen');
        var chosenval = $('#proyecto'+i+'_categoria').trigger('chosen-updated').val().length;
        if (chosenval == 0){
            chosen_container.attr("data-content", requiredFieldMessage);
            chosen_container.addClass('input-error');
            chosen_container.attr("data-valido", 'false');
            chosen_container.popover('show');
            valid = false;
        }
        else {
            chosen_container.removeClass('input-error');
            chosen_container.popover('hide');
        }
    }
    return valid;

}
const validadoresSextoPaso = [
    validaAdministrativas
]
const validadoresSeptimoPaso = [
    validaExtension
]
const validadoresOctavoPaso = [
    validaEstudios
]
const validadoresNovenoPaso = [
    validaCursos
]
const validadoresDecimoPaso = [
    validaMaterias
]
const validadoresOnceavoPaso = [
    validaTrabajosDirigidos
]
const validadoresDoceavoPaso = [
    validaProyectos
]









// ESCRIBE ALGO COMO
/*
const validadoresSextoPaso = [
]
*/






// Funcion que valida los campos cuando el usuario pasa a llenar otro input
function validacionTiempoReal(){

    // Manejo de error del telefono
    $('[name="telefono_add"]').on('change', validaTelefonoResidencial)

    // Manejo del error de email alternativo
    $('[name="email_alt_add"]').on('change', validaEmailAlternativo)

    // Manejo de error del numero de celular
    $('[name="celular_add"]').on('change', validaCelular);

    // Manejo de error del campo de contacto de emergencia
    $('[name="contacto_emergencia_add"]').on('change', validaContactoEmergencia)

    // Manejo de error del campo de pagina de web
    $('[name="pagina_web_add"]').on('change', validaPaginaWeb)

    $('[name="direccion_add"]').on('change', validaDireccionHab)


    //$('[name="fecha_inicio_1_add"]').on('change', validaFechaInicio)
}

/**
 * Funcion que determina si los validadores pasan o no
 * @param {array_fun} validatorsList Arreglo que tiene funciones validadores. La firma de cada funcion es:
 * () -> bool
 */
function validadoresCorrectos(validatorsList) {
    return validatorsList
        .map(fn => fn())
        .reduce((acc, i) => acc && i, true)
}

$(document).ready(function () {
    $('.fselect').fSelect({
        placeholder: 'Escoja sus ubicaciones',
        numDisplayed: 3,
        overflowText: '{n} ubicaciones',
        searchText: 'Buscar',
        showSearch: true
    })

    new Cleave('[name="telefono_add"]', {
        // delimiter: '-',
        delimiters: ['(', ')', '-'],
        blocks: [0, 4, 3, 4],
    })
    new Cleave('[name="contacto_emergencia_add"]', {
        // delimiter: '-',
        delimiters: ['(', ')', '-'],
        blocks: [0, 4, 3, 4],
    })
    new Cleave('[name="celular_add"]', {
        delimiter: '-',
        blocks: [3, 4]
    })

    $('.registration-form fieldset:first-child').fadeIn('slow');

    $('#sel2').change(function (){
        if ($("#sel2 option:selected").val()==="Fijo") {
            $("#fsalida").hide();
            $('#fingreso').show()
            $('[name="fecha_ingreso_add"]').val('');
            $('[name="fecha_salida_add"]').val('');
        }
        else {
            $("#fsalida").show();
            $("#fingreso").hide();
        };
    });

    //-------------------------------- Primera parte del form agregar -----------------------------------------//

    validacionTiempoReal();

    // next step
    $('.registration-form .btn-next').on('click', function () {

        var parent_fieldset = $(this).parents('fieldset');
        var next_step = true;
        if (parent_fieldset.attr('id') === 'p1') {
            next_step = validadoresCorrectos(validadoresPrimerPaso)
        }
        else if (parent_fieldset.attr('id') === 'p2'){
            if ($('[name="categoria_add"]').val() === 'Fijo'){
                // Vacio los campos de fecha de ingreso y de salida para que no se guarden en la 
                // base de datos 
                $('[name="fecha_ingreso_add"]').val('');
                $('[name="fecha_salida_add"]').val('');

                next_step = validadoresCorrectos(validadoresSegundoPasoFijo)
            }
            else {
                next_step = validadoresCorrectos(validadoresSegundoPaso)
            }
        }
        else if (parent_fieldset.attr('id') === 'p3'){
            next_step = validadoresCorrectos(validadoresTercerPaso)
        }

        else if (parent_fieldset.attr('id') === 'p4'){
            next_step = validadoresCorrectos(validadoresCuartoPaso)
        }

        else if (parent_fieldset.attr('id') === 'p5'){
            next_step = validadoresCorrectos(validadoresQuintoPaso)
        }
        else if (parent_fieldset.attr('id') === 'p6'){
            next_step = validadoresCorrectos(validadoresSextoPaso)
        }
        else if (parent_fieldset.attr('id') === 'p7'){
            next_step = validadoresCorrectos(validadoresSeptimoPaso)
        }
        else if (parent_fieldset.attr('id') === 'p8'){
            next_step = validadoresCorrectos(validadoresOctavoPaso)
        }
        else if (parent_fieldset.attr('id') === 'p9'){
            next_step = validadoresCorrectos(validadoresNovenoPaso)
        }
        else if (parent_fieldset.attr('id') === 'p10'){
            next_step = validadoresCorrectos(validadoresDecimoPaso)
        }

        else if (parent_fieldset.attr('id') === 'p11'){
            next_step = validadoresCorrectos(validadoresOnceavoPaso)
        }





        /* AQUI VAN OTROS ELSE IF CON LOS PASOS POR EJEMPLO
        
        //Paso de Moises
        else if (parent_fieldset.attr('id') === 'p4')
            next_step = validadoresCorrectos(validadoresCuartoPaso)
        
        // Paso de Constanza
        else if(parent_fieldset.attr('id') === 'p5')
            next_step = validadoresCorrectos(validadoresQuintoPaso)

        SI EL TUYO ES EL ULTIMO PASO ANTES DE HACER SUBMMIT NO VA AQUI

        */













        if (next_step) {
            parent_fieldset.fadeOut(400, function () {
                $(this).next().fadeIn();
            });
        }

    });

    // previous step
    $('.registration-form .btn-previous').on('click', function () {
        $(this).parents('fieldset').fadeOut(400, function () {
            $(this).prev().fadeIn();
        });
    });


    // Desaparecer popover
    $(inputSelectorsAll).on('focus change click', function(e){
        $(this).popover('hide');
        $(this).removeClass('input-error');

    })

    $('#formularioCarga').on('keyup keypress', function(e) {
        var keyCode = e.keyCode || e.which;
        if (keyCode === 13) { 
          e.preventDefault();
          return false;
        }
      });
    // submit
    $('.registration-form .btn-submit').on('click', function (e) {
        
        var parent_fieldset = $(this).parents('fieldset');
        
        var enviar = validadoresCorrectos(validadoresDoceavoPaso);




        /* 
        SI TU PASO ES EL ULTIMO ANTES DE HACER SUBMIT ENTONCES COLOCA TUS
        FUNCIONES EN ENVIAR POR EJEMPLO
        var enviar = validadoresCorrectos(validadoresSextoPaso);
        Y LISTO
        */











        console.log(enviar)
        if (enviar){

            $(this).attr("type", "submit");
        }
        else {
            $(this).attr("type", "button");
        }

        parent_fieldset.find('input[type="text"]').each(function () {
            // if (($(this).val() == "") && ($(this).attr('required'))) {
            //     if (($(this).attr('name')=="cargo_add") || ($(this).attr('name')=="cargo_edit")) {
            //         $("#err_cargo").html("Este campo es obligatorio");
            //         $("#err_cargo").show();
            //     }
            //     $(this).addClass('input-error');
            //     e.preventDefault();
            // } else {
            //     if (($(this).attr('name')=="cargo_add") || ($(this).attr('name')=="cargo_edit")) {
            //         if (!($(this).val().match(/^(([a-zA-Z ]+[\-\'\.]?)+[a-zA-Z ]+)+$/))) { // Todo lo que sea nombres (Antes del submit)
            //             $("#err_cargo").html("Introduzca un cargo válido");
            //             $("#err_cargo").show();
            //             $(this).addClass('input-error');
            //             e.preventDefault();
            //         }
            //         else {
            //             $("#err_cargo").hide();
            //             $(this).removeClass('input-error');
            //         }
            //     }
            //     else {
            //         $(this).removeClass('input-error');
            //     }
            // }
        });

    });





});

