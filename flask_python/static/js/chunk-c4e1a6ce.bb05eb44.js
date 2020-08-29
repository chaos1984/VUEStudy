(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-c4e1a6ce"],{"23a7":function(t,e,i){"use strict";i("5803");var s=i("2677"),n=i("cc20"),a=i("80d2"),l=i("d9bd"),o=i("d9f7");e["a"]=s["a"].extend({name:"v-file-input",model:{prop:"value",event:"change"},props:{chips:Boolean,clearable:{type:Boolean,default:!0},counterSizeString:{type:String,default:"$vuetify.fileInput.counterSize"},counterString:{type:String,default:"$vuetify.fileInput.counter"},hideInput:Boolean,placeholder:String,prependIcon:{type:String,default:"$file"},readonly:{type:Boolean,default:!1},showSize:{type:[Boolean,Number],default:!1,validator:t=>"boolean"===typeof t||[1e3,1024].includes(t)},smallChips:Boolean,truncateLength:{type:[Number,String],default:22},type:{type:String,default:"file"},value:{default:void 0,validator:t=>Object(a["H"])(t).every(t=>null!=t&&"object"===typeof t)}},computed:{classes(){return{...s["a"].options.computed.classes.call(this),"v-file-input":!0}},computedCounterValue(){const t=this.isMultiple&&this.lazyValue?this.lazyValue.length:this.lazyValue instanceof File?1:0;if(!this.showSize)return this.$vuetify.lang.t(this.counterString,t);const e=this.internalArrayValue.reduce((t,{size:e=0})=>t+e,0);return this.$vuetify.lang.t(this.counterSizeString,t,Object(a["w"])(e,1024===this.base))},internalArrayValue(){return Object(a["H"])(this.internalValue)},internalValue:{get(){return this.lazyValue},set(t){this.lazyValue=t,this.$emit("change",this.lazyValue)}},isDirty(){return this.internalArrayValue.length>0},isLabelActive(){return this.isDirty},isMultiple(){return this.$attrs.hasOwnProperty("multiple")},text(){return this.isDirty?this.internalArrayValue.map(t=>{const{name:e="",size:i=0}=t,s=this.truncateText(e);return this.showSize?`${s} (${Object(a["w"])(i,1024===this.base)})`:s}):[this.placeholder]},base(){return"boolean"!==typeof this.showSize?this.showSize:void 0},hasChips(){return this.chips||this.smallChips}},watch:{readonly:{handler(t){!0===t&&Object(l["b"])("readonly is not supported on <v-file-input>",this)},immediate:!0},value(t){const e=this.isMultiple?t:t?[t]:[];Object(a["j"])(e,this.$refs.input.files)||(this.$refs.input.value="")}},methods:{clearableCallback(){this.internalValue=this.isMultiple?[]:void 0,this.$refs.input.value=""},genChips(){return this.isDirty?this.text.map((t,e)=>this.$createElement(n["a"],{props:{small:this.smallChips},on:{"click:close":()=>{const t=this.internalValue;t.splice(e,1),this.internalValue=t}}},[t])):[]},genControl(){const t=s["a"].options.methods.genControl.call(this);return this.hideInput&&(t.data.style=Object(o["d"])(t.data.style,{display:"none"})),t},genInput(){const t=s["a"].options.methods.genInput.call(this);return delete t.data.domProps.value,delete t.data.on.input,t.data.on.change=this.onInput,[this.genSelections(),t]},genPrependSlot(){if(!this.prependIcon)return null;const t=this.genIcon("prepend",()=>{this.$refs.input.click()});return this.genSlot("prepend","outer",[t])},genSelectionText(){const t=this.text.length;return t<2?this.text:this.showSize&&!this.counter?[this.computedCounterValue]:[this.$vuetify.lang.t(this.counterString,t)]},genSelections(){const t=[];return this.isDirty&&this.$scopedSlots.selection?this.internalArrayValue.forEach((e,i)=>{this.$scopedSlots.selection&&t.push(this.$scopedSlots.selection({text:this.text[i],file:e,index:i}))}):t.push(this.hasChips&&this.isDirty?this.genChips():this.genSelectionText()),this.$createElement("div",{staticClass:"v-file-input__text",class:{"v-file-input__text--placeholder":this.placeholder&&!this.isDirty,"v-file-input__text--chips":this.hasChips&&!this.$scopedSlots.selection}},t)},genTextFieldSlot(){const t=s["a"].options.methods.genTextFieldSlot.call(this);return t.data.on={...t.data.on||{},click:()=>this.$refs.input.click()},t},onInput(t){const e=[...t.target.files||[]];this.internalValue=this.isMultiple?e:e[0],this.initialValue=this.internalValue},onKeyDown(t){this.$emit("keydown",t)},truncateText(t){if(t.length<Number(this.truncateLength))return t;const e=Math.floor((Number(this.truncateLength)-1)/2);return`${t.slice(0,e)}…${t.slice(t.length-e)}`}}})},2677:function(t,e,i){"use strict";var s=i("8654");e["a"]=s["a"]},5803:function(t,e,i){},"6ca7":function(t,e,i){},8547:function(t,e,i){"use strict";var s=i("2b0e"),n=i("80d2");e["a"]=s["a"].extend({name:"comparable",props:{valueComparator:{type:Function,default:n["j"]}}})},"8adc":function(t,e,i){},ac7c:function(t,e,i){"use strict";i("6ca7"),i("ec29");var s=i("9d26"),n=i("c37a"),a=i("5607"),l=i("2b0e"),o=l["a"].extend({name:"rippleable",directives:{ripple:a["a"]},props:{ripple:{type:[Boolean,Object],default:!0}},methods:{genRipple(t={}){return this.ripple?(t.staticClass="v-input--selection-controls__ripple",t.directives=t.directives||[],t.directives.push({name:"ripple",value:{center:!0}}),t.on=Object.assign({click:this.onChange},this.$listeners),this.$createElement("div",t)):null},onChange(){}}}),r=i("8547"),h=i("58df"),c=Object(h["a"])(n["a"],o,r["a"]).extend({name:"selectable",model:{prop:"inputValue",event:"change"},props:{id:String,inputValue:null,falseValue:null,trueValue:null,multiple:{type:Boolean,default:null},label:String},data(){return{hasColor:this.inputValue,lazyValue:this.inputValue}},computed:{computedColor(){if(this.isActive)return this.color?this.color:this.isDark&&!this.appIsDark?"white":"primary"},isMultiple(){return!0===this.multiple||null===this.multiple&&Array.isArray(this.internalValue)},isActive(){const t=this.value,e=this.internalValue;return this.isMultiple?!!Array.isArray(e)&&e.some(e=>this.valueComparator(e,t)):void 0===this.trueValue||void 0===this.falseValue?t?this.valueComparator(t,e):Boolean(e):this.valueComparator(e,this.trueValue)},isDirty(){return this.isActive},rippleState(){return this.isDisabled||this.validationState?this.validationState:void 0}},watch:{inputValue(t){this.lazyValue=t,this.hasColor=t}},methods:{genLabel(){const t=n["a"].options.methods.genLabel.call(this);return t?(t.data.on={click:t=>{t.preventDefault(),this.onChange()}},t):t},genInput(t,e){return this.$createElement("input",{attrs:Object.assign({"aria-checked":this.isActive.toString(),disabled:this.isDisabled,id:this.computedId,role:t,type:t},e),domProps:{value:this.value,checked:this.isActive},on:{blur:this.onBlur,change:this.onChange,focus:this.onFocus,keydown:this.onKeydown},ref:"input"})},onBlur(){this.isFocused=!1},onChange(){if(!this.isInteractive)return;const t=this.value;let e=this.internalValue;if(this.isMultiple){Array.isArray(e)||(e=[]);const i=e.length;e=e.filter(e=>!this.valueComparator(e,t)),e.length===i&&e.push(t)}else e=void 0!==this.trueValue&&void 0!==this.falseValue?this.valueComparator(e,this.trueValue)?this.falseValue:this.trueValue:t?this.valueComparator(e,t)?null:t:!e;this.validate(!0,e),this.internalValue=e,this.hasColor=e},onFocus(){this.isFocused=!0},onKeydown(t){}}});e["a"]=c.extend({name:"v-checkbox",props:{indeterminate:Boolean,indeterminateIcon:{type:String,default:"$checkboxIndeterminate"},offIcon:{type:String,default:"$checkboxOff"},onIcon:{type:String,default:"$checkboxOn"}},data(){return{inputIndeterminate:this.indeterminate}},computed:{classes(){return{...n["a"].options.computed.classes.call(this),"v-input--selection-controls":!0,"v-input--checkbox":!0,"v-input--indeterminate":this.inputIndeterminate}},computedIcon(){return this.inputIndeterminate?this.indeterminateIcon:this.isActive?this.onIcon:this.offIcon},validationState(){if(!this.isDisabled||this.inputIndeterminate)return this.hasError&&this.shouldValidate?"error":this.hasSuccess?"success":null!==this.hasColor?this.computedColor:void 0}},watch:{indeterminate(t){this.$nextTick(()=>this.inputIndeterminate=t)},inputIndeterminate(t){this.$emit("update:indeterminate",t)},isActive(){this.indeterminate&&(this.inputIndeterminate=!1)}},methods:{genCheckbox(){return this.$createElement("div",{staticClass:"v-input--selection-controls__input"},[this.$createElement(s["a"],this.setTextColor(this.validationState,{props:{dense:this.dense,dark:this.dark,light:this.light}}),this.computedIcon),this.genInput("checkbox",{...this.attrs$,"aria-checked":this.inputIndeterminate?"mixed":this.isActive.toString()}),this.genRipple(this.setTextColor(this.rippleState))])},genDefaultSlot(){return[this.genCheckbox(),this.genLabel()]}}})},b0c0:function(t,e,i){var s=i("83ab"),n=i("9bf2").f,a=Function.prototype,l=a.toString,o=/^\s*function ([^ (]*)/,r="name";s&&!(r in a)&&n(a,r,{configurable:!0,get:function(){try{return l.call(this).match(o)[1]}catch(t){return""}}})},cc20:function(t,e,i){"use strict";i("8adc");var s=i("58df"),n=i("0789"),a=i("9d26"),l=i("a9ad"),o=i("4e82"),r=i("7560"),h=i("f2e7"),c=i("1c87"),u=i("af2b"),p=i("d9bd");e["a"]=Object(s["a"])(l["a"],u["a"],c["a"],r["a"],Object(o["a"])("chipGroup"),Object(h["b"])("inputValue")).extend({name:"v-chip",props:{active:{type:Boolean,default:!0},activeClass:{type:String,default(){return this.chipGroup?this.chipGroup.activeClass:""}},close:Boolean,closeIcon:{type:String,default:"$delete"},disabled:Boolean,draggable:Boolean,filter:Boolean,filterIcon:{type:String,default:"$complete"},label:Boolean,link:Boolean,outlined:Boolean,pill:Boolean,tag:{type:String,default:"span"},textColor:String,value:null},data:()=>({proxyClass:"v-chip--active"}),computed:{classes(){return{"v-chip":!0,...c["a"].options.computed.classes.call(this),"v-chip--clickable":this.isClickable,"v-chip--disabled":this.disabled,"v-chip--draggable":this.draggable,"v-chip--label":this.label,"v-chip--link":this.isLink,"v-chip--no-color":!this.color,"v-chip--outlined":this.outlined,"v-chip--pill":this.pill,"v-chip--removable":this.hasClose,...this.themeClasses,...this.sizeableClasses,...this.groupClasses}},hasClose(){return Boolean(this.close)},isClickable(){return Boolean(c["a"].options.computed.isClickable.call(this)||this.chipGroup)}},created(){const t=[["outline","outlined"],["selected","input-value"],["value","active"],["@input","@active.sync"]];t.forEach(([t,e])=>{this.$attrs.hasOwnProperty(t)&&Object(p["a"])(t,e,this)})},methods:{click(t){this.$emit("click",t),this.chipGroup&&this.toggle()},genFilter(){const t=[];return this.isActive&&t.push(this.$createElement(a["a"],{staticClass:"v-chip__filter",props:{left:!0}},this.filterIcon)),this.$createElement(n["b"],t)},genClose(){return this.$createElement(a["a"],{staticClass:"v-chip__close",props:{right:!0,size:18},on:{click:t=>{t.stopPropagation(),t.preventDefault(),this.$emit("click:close"),this.$emit("update:active",!1)}}},this.closeIcon)},genContent(){return this.$createElement("span",{staticClass:"v-chip__content"},[this.filter&&this.genFilter(),this.$slots.default,this.hasClose&&this.genClose()])}},render(t){const e=[this.genContent()];let{tag:i,data:s}=this.generateRouteLink();s.attrs={...s.attrs,draggable:this.draggable?"true":void 0,tabindex:this.chipGroup&&!this.disabled?0:s.attrs.tabindex},s.directives.push({name:"show",value:this.active}),s=this.setBackgroundColor(this.color,s);const n=this.textColor||this.outlined&&this.color;return t(i,this.setTextColor(n,s),e)}})},d3b2:function(t,e,i){"use strict";i.r(e);var s=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("v-card",[i("v-card-title",[t._v(" Cushion ")]),i("v-card-text",[i("v-checkbox",{staticClass:"shrink mr-2 mt-0",attrs:{"hide-details":"",label:"New Cushion"},model:{value:t.enabled,callback:function(e){t.enabled=e},expression:"enabled"}}),i("v-row",{attrs:{align:"center"}},[i("v-file-input",{attrs:{id:"CushiondwgFile",type:"file",accept:".dwg",disabled:!t.enabled,label:"Cushion dwg file"},on:{change:t.uploadFile}}),i("v-file-input",{attrs:{id:"CushionFoldFile",type:"file",accept:".pdf",disabled:!t.enabled,label:"New cushion folding file"},on:{change:t.uploadFile}})],1),i("v-text-field",{attrs:{type:"text",disabled:t.enabled,label:"Please input your carryover cushion"}})],1)],1)},n=[],a=(i("b0c0"),i("5530")),l=i("2f62"),o={data:function(){return{enabled:!1}},computed:Object(a["a"])({isError:function(){return(""==this.CurrentForm.CushiondwgFile||""==this.CurrentForm.CushionFoldFile)&&""==this.CurrentForm.OldCushion}},Object(l["b"])({CurrentForm:function(t){return t.form}})),methods:{validate:function(){this.$store.commit("nextStep")},onBackStep:function(){this.$store.commit("backStep")},onClearData:function(){this.CurrentForm.CushiondwgFile=[],this.CurrentForm.CushionFoldFile=[],this.CurrentForm.OldCushion=[]},uploadFile:function(t){var e=event.target,i=e.getAttribute("id");console.log(i);var s=new FormData;s.append("file",t),this.filedata=s.get("file"),this.CurrentForm[i]=this.filedata["name"],this.$axios.post("/api/upload",s,{headers:{"Content-Type":"application/x-www-form-urlencoded"}}).then((function(t){console.log(t.data)})).catch((function(t){console.log(t)}))}}},r=o,h=i("2877"),c=i("6544"),u=i.n(c),p=i("b0af"),d=i("99d9"),f=i("ac7c"),v=i("23a7"),m=i("0fd9"),g=i("8654"),b=Object(h["a"])(r,s,n,!1,null,null,null);e["default"]=b.exports;u()(b,{VCard:p["a"],VCardText:d["b"],VCardTitle:d["c"],VCheckbox:f["a"],VFileInput:v["a"],VRow:m["a"],VTextField:g["a"]})},ec29:function(t,e,i){}}]);
//# sourceMappingURL=chunk-c4e1a6ce.bb05eb44.js.map